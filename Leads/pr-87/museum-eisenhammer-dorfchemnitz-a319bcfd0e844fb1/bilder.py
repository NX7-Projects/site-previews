# Erzeugt die Bildvarianten fuer die Website aus den Originalen von Wikimedia Commons.
# Quellen und Lizenzen: siehe QUELLEN.md und pflichtteile.json
#
#   python bilder.py <verzeichnis-mit-originalen>
#
# Originale (Dateinamen wie hier erwartet):
#   b-gesamtansicht.jpg  -> Eisenhammer Dorfchemnitz Gesamtansicht.jpg  (Miebner, CC BY-SA 3.0)
#   c-hammergeruest.jpg  -> Eisenhammer Dorfchemnitz Hammergeruest.jpg  (Miebner, CC BY-SA 3.0)
#   d-eisenhammer.jpg    -> Eisenhammer Dorfchemnitz.jpg               (Miebner, CC BY-SA 3.0)
#   a-eisenhammer01.jpg  -> Dorfchemnitz Eisenhammer 01.JPG            (Norbert Kaiser, CC BY-SA 2.5)

import os
import sys

from PIL import Image, ImageEnhance

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "img")

# stamm, quelldatei, (linker Rand, oberer Rand, rechter Rand, unterer Rand) relativ, Breiten, JPG-Fallbackbreite
PLAN = [
    ("hammerhaus", "b-gesamtansicht.jpg", (0.00, 0.02, 1.00, 0.96), [2400, 1600, 1000, 640], 1600),
    ("hammerhaus-hoch", "b-gesamtansicht.jpg", (0.37, 0.02, 0.87, 1.00), [1100, 760, 560], 760),
    ("hammergeruest", "c-hammergeruest.jpg", (0.02, 0.00, 1.00, 1.00), [1900, 1300, 900, 640], 1300),
    ("wasserrad", "d-eisenhammer.jpg", (0.00, 0.00, 0.78, 1.00), [1500, 1000, 700, 520], 1000),
    ("hammerhof", "a-eisenhammer01.jpg", (0.06, 0.05, 1.00, 0.94), [1500, 1000, 700, 520], 1000),
]


def beschnitt(im, box):
    b, h = im.size
    l, o, r, u = box
    return im.crop((int(l * b), int(o * h), int(r * b), int(u * h)))


def main():
    quelle = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(ZIEL, exist_ok=True)
    for stamm, datei, box, breiten, jpgbreite in PLAN:
        pfad = os.path.join(quelle, datei)
        if not os.path.exists(pfad):
            print("fehlt:", pfad)
            continue
        original = beschnitt(Image.open(pfad).convert("RGB"), box)
        # Die Originale sind Kompaktkamera-Aufnahmen: minimal nachschaerfen und
        # den Kontrast leicht anziehen, damit sie gross gesetzt bestehen.
        original = ImageEnhance.Contrast(original).enhance(1.06)
        original = ImageEnhance.Color(original).enhance(1.04)
        for breite in breiten:
            if breite > original.width:
                continue
            hoehe = round(original.height * breite / original.width)
            bild = original.resize((breite, hoehe), Image.LANCZOS)
            bild.save(os.path.join(ZIEL, "%s-%d.webp" % (stamm, breite)), "WEBP", quality=82, method=6)
            if breite == jpgbreite:
                bild.save(os.path.join(ZIEL, "%s-%d.jpg" % (stamm, breite)), "JPEG", quality=84, optimize=True, progressive=True)
            print("%s-%d" % (stamm, breite), bild.size)


if __name__ == "__main__":
    main()
