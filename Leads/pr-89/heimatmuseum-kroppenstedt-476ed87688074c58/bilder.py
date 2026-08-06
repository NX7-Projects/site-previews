#!/usr/bin/env python3
"""Bildaufbereitung Heimatmuseum Kroppenstedt.

Laedt die Originale von Wikimedia Commons nach raw/ (falls sie fehlen) und
erzeugt daraus die beschnittenen WebP-Varianten samt JPG-Fallback in
assets/img/. Urheber und Lizenz jedes Bildes stehen in QUELLEN.md und in
pflichtteile.json; raw/ selbst wird nicht eingecheckt.

    python bilder.py
"""
import shutil
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
OUT = ROOT / "assets" / "img"

KOPF = {"User-Agent": "heimatmuseum-kroppenstedt-website/1.0 (mail@tobiassteffen.com)"}

# Quelldatei -> Originaladresse auf Wikimedia Commons
QUELLEN = {
    "museum-martini.jpg":
        "https://upload.wikimedia.org/wikipedia/commons/4/44/"
        "Kroppenstedt%2C_Haus_Am_Kirchhof_2_und_Kirche_St.Martin.jpg",
    "museum-stadtmauer.jpg":
        "https://upload.wikimedia.org/wikipedia/commons/5/55/"
        "Kroppenstedt%2C_Haus_Am_Kirchhof_2_%28Museum%29_und_Stadtmauer.jpg",
    "museum-innen.jpg":
        "https://upload.wikimedia.org/wikipedia/commons/a/ae/"
        "Museum_Kroppenstedt_P1110479.jpg",
    "mauer-nischen.jpg":
        "https://upload.wikimedia.org/wikipedia/commons/6/67/"
        "Kroppenstedt%2C_Stadtmauer_am_Heimatmuseum_%282%29_Nischen.jpg",
    "museum-fachwerk.jpg":
        "https://upload.wikimedia.org/wikipedia/commons/2/20/"
        "Kroppenstedt%2C_Heimatmuseum%2C_Am_Kirchhof_2.jpg",
}

# Zielname -> (Quelldatei, Crop-Box oder None, Ziel-Breiten)
JOBS = {
    # Hof mit Stadtmauer und Kirche St. Martin - Kopfbild, kinematisch beschnitten
    "hof-martini": ("museum-martini.jpg", (0, 200, 4947, 2982), [640, 1000, 1600, 2200]),
    # Museumshof mit Stadtmauer, Nischen und Haustafel
    "hof-stadtmauer": ("museum-stadtmauer.jpg", None, [640, 1000, 1600, 2200]),
    # Die Haustafel mit den vier Jahreszahlen (Ausschnitt)
    "tafel-jahre": ("museum-stadtmauer.jpg", (430, 1840, 1070, 2480), [420, 640]),
    # Giebel mit Turm am Kirchhof
    "giebel-ulenturm": ("museum-innen.jpg", (0, 0, 2560, 1900), [640, 1000, 1600, 2200]),
    # Mauernische mit Wagengeraet - das wiederkehrende Formmotiv
    "nische-wagenrad": ("mauer-nischen.jpg", (1000, 100, 2900, 2400), [640, 1000, 1400]),
    # Fachwerk ueber Bruchstein, Eingangsseite
    "fachwerk-eingang": ("museum-fachwerk.jpg", (1200, 0, 4000, 2400), [640, 1000, 1600]),
}

FALLBACK_WIDTH = 1000


def holen(url: str, ziel: Path) -> None:
    """Laedt eine Datei. Faellt auf curl zurueck, wenn Pythons CA-Speicher
    veraltet ist - das ist auf Windows-Buildrechnern der Normalfall."""
    try:
        with urlopen(Request(url, headers=KOPF)) as antwort:
            ziel.write_bytes(antwort.read())
        return
    except Exception as fehler:
        curl = shutil.which("curl")
        if not curl:
            raise
        print(f"  urllib: {fehler} - versuche curl")
        subprocess.run(
            [curl, "-sSfL", "-A", KOPF["User-Agent"], "-o", str(ziel), url],
            check=True,
        )


def laden() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    for name, url in QUELLEN.items():
        ziel = RAW / name
        if ziel.exists():
            continue
        print(f"lade {name} …")
        holen(url, ziel)


def bauen() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (src, box, widths) in JOBS.items():
        im = Image.open(RAW / src).convert("RGB")
        if box:
            im = im.crop(box)
        for w in widths:
            h = round(im.height * w / im.width)
            v = im.resize((w, h), Image.LANCZOS)
            v.save(OUT / f"{name}-{w}.webp", "WEBP", quality=80, method=6)
            if w == FALLBACK_WIDTH or (FALLBACK_WIDTH not in widths and w == widths[-1]):
                v.save(OUT / f"{name}-{w}.jpg", "JPEG", quality=82, optimize=True,
                       progressive=True)
        print(f"{name}: {im.width}x{im.height} -> {widths}")


if __name__ == "__main__":
    laden()
    bauen()
