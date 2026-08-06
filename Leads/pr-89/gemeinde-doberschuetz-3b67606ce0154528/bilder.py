# Bildaufbereitung fuer die Entwurfsseite Gemeinde Doberschuetz.
# Quelle aller Originale: Wikimedia Commons (Nachweis in QUELLEN.md und pflichtteile.json).
# Aufruf: python bilder.py  (erwartet die Originale in ./_original/)
import os
from PIL import Image

BILDER = {
    "wegestein-bunitz": "wegestein.jpg",
    "anger-doberschuetz": "anger.jpg",
    "muehle-paschwitz": "muehle.jpg",
    "kirche-battaune": "kirche.jpg",
    "denkmalswald-winkelmuehle": "wald.jpg",
    "haltepunkt-doberschuetz": "bahnhof.jpg",
    "gut-heideck-sprotta": "heideck.jpg",
}
BREITEN = (1600, 900, 520)
ZIEL = os.path.join("assets", "bilder")

os.makedirs(ZIEL, exist_ok=True)
for stamm, datei in BILDER.items():
    pfad = os.path.join("_original", datei)
    if not os.path.exists(pfad):
        print("fehlt:", pfad)
        continue
    original = Image.open(pfad).convert("RGB")
    for breite in BREITEN:
        if original.width < breite:
            continue
        hoehe = round(original.height * breite / original.width)
        kopie = original.resize((breite, hoehe), Image.LANCZOS)
        name = "%s-%d.jpg" % (stamm, breite)
        kopie.save(os.path.join(ZIEL, name), "JPEG", quality=82, optimize=True, progressive=True)
        print(name, kopie.size)
