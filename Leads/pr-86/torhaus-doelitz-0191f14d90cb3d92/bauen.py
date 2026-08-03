# -*- coding: utf-8 -*-
"""
Torhaus Doelitz - Seitengenerator.

Diese Seite ist statisches HTML ohne Abhaengigkeiten. Das Skript existiert nur,
damit Kopf, Fuss und Seitenhuelle auf allen Seiten wirklich identisch sind -
es wird einmal ausgefuehrt und schreibt die HTML-Dateien daneben.

    python bauen.py

Die erzeugten Dateien sind eingecheckt; wer nur Text aendert, kann sie auch
direkt bearbeiten - dann aber bitte in allen Dateien gleich.
"""

import io
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------

NAV = [
    ("museum.html", "Ausstellung"),
    ("veranstaltungen.html", "Veranstaltungen"),
    ("geschichte.html", "Geschichte"),
    ("unterstuetzen.html", "Unterstützen"),
    ("besuch.html", "Besuch planen"),
]


def nav_html(aktiv, klasse, praefix=""):
    zeilen = []
    for ziel, name in NAV:
        jetzt = ' aria-current="page"' if ziel == aktiv else ""
        zeilen.append('    <a href="%s%s"%s>%s</a>' % (praefix, ziel, jetzt, name))
    return "\n".join(zeilen)


# ---------------------------------------------------------------------------
# Huelle
# ---------------------------------------------------------------------------

KOPF = u"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{beschreibung}">
<meta name="theme-color" content="#21262b">
<link rel="icon" href="{p}assets/img/marke-torhaus.png" type="image/png">
<link rel="preload" href="{p}assets/fonts/bodoni-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/css/torhaus.css">
<script>document.documentElement.className+=' js';</script>
</head>
<body>

<a class="sprung" href="#inhalt">Zum Inhalt springen</a>

<header class="kopf">
  <div class="wrap kopf__innen">
    <a class="lockup" href="{p}./">
      <img src="{p}assets/img/marke-torhaus.png" alt="" width="284" height="154">
      <span class="lockup__text">
        <span class="lockup__haupt">Torhaus Dölitz</span>
        <span class="lockup__zusatz">Zinnfigurenmuseum Leipzig</span>
      </span>
    </a>
    <nav class="nav" data-nav aria-label="Hauptnavigation">
{nav}
    </nav>
    <button class="menuknopf" type="button" data-menuknopf aria-expanded="false" aria-controls="schublade">
      <span data-menutext>Menü</span>
    </button>
  </div>
  <div class="wrap schublade" id="schublade" data-schublade data-offen="false">
{navmobil}
  </div>
</header>

<main id="inhalt">
"""

FUSS = u"""</main>

<footer class="fuss" data-fuss>
  <div class="wrap">
    <div class="fuss__raster">
      <div>
        <img class="fuss__marke" src="{p}assets/img/marke-torhaus.png" alt="" width="284" height="154">
        <p class="fuss__titel">Torhaus Dölitz</p>
        <ul>
          <li>Helenenstraße 24<br>04279 Leipzig</li>
          <li><a href="tel:+493413389107">0341 3389107</a></li>
          <li><a href="mailto:info@torhaus-doelitz.eu">info@torhaus-doelitz.eu</a></li>
        </ul>
      </div>
      <div>
        <p class="fuss__titel">Geöffnet</p>
        <ul>
          <li>Mittwoch, Samstag, Sonntag<br>und feiertags, 10–17 Uhr</li>
          <li>Letzter Einlass 16.30 Uhr</li>
          <li>Nur Barzahlung möglich</li>
          <li><a href="{p}besuch.html">Zeiten, Preise, Anfahrt</a></li>
        </ul>
      </div>
      <div>
        <p class="fuss__titel">Räume mieten</p>
        <ul>
          <li>Gewölbe und voll ausgestattete Küche</li>
          <li><a href="tel:+491781317071">0178 1317071</a><br>täglich 10–19 Uhr</li>
          <li><a href="mailto:thd-reservierung@leipzig1813.com">thd-reservierung@<wbr>leipzig1813.com</a></li>
          <li><a href="{p}unterstuetzen.html#vermietung">Zur Vermietung</a></li>
        </ul>
      </div>
      <div>
        <p class="fuss__titel">Verbunden</p>
        <ul>
          <li><a href="https://www.leipzig1813.com/" rel="noopener">Verband Jahrfeier 1813 e.&nbsp;V.</a></li>
          <li><a href="https://www.zinnfigurenfreunde-leipzig.de/" rel="noopener">Zinnfigurenfreunde Leipzig</a></li>
          <li><a href="https://www.bv-doelitz-online.de/" rel="noopener">Bürgerverein Dölitz e.&nbsp;V.</a></li>
          <li><a href="https://agra-park.info/" rel="noopener">agra-Park</a></li>
          <li><a href="https://www.leipzig.de/" rel="noopener">Gefördert vom Kulturamt der Stadt Leipzig</a></li>
        </ul>
      </div>
    </div>
    <div class="fuss__unten">
      <p style="margin:0">Betreiber: Verband Jahrfeier Völkerschlacht b. Leipzig 1813 e.&nbsp;V.</p>
      <div class="pflichtlinks"><!--PFLICHTLINKS--></div>
    </div>
  </div>
</footer>

<a class="schwebe" data-schwebe href="{schwebeziel}">
  <span class="schwebe__bogen" aria-hidden="true"></span>
  {schwebetext}
</a>

<script src="{p}assets/js/torhaus.js" defer></script>
</body>
</html>
"""


def seite(datei, titel, beschreibung, koerper, aktiv=None,
          schwebeziel="besuch.html", schwebetext="Besuch planen", praefix=""):
    html = (
        KOPF.format(
            titel=titel,
            beschreibung=beschreibung,
            nav=nav_html(aktiv, "nav", praefix),
            navmobil=nav_html(aktiv, "schublade", praefix),
            p=praefix,
        )
        + koerper.rstrip()
        + "\n\n"
        + FUSS.format(p=praefix, schwebeziel=praefix + schwebeziel, schwebetext=schwebetext)
    )
    with io.open(os.path.join(HIER, datei), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return datei, len(html)


# ---------------------------------------------------------------------------
# Bausteine
# ---------------------------------------------------------------------------

def bild(stem, alt, breite, hoehe, sizes, klasse="bogen", verhaeltnis="4/3",
         laden="lazy", p="", groessen=(640, 1000, 1600)):
    quellen = ", ".join(
        "%sassets/img/%s-%d.webp %dw" % (p, stem, g, g) for g in groessen
    )
    return (
        '<div class="%s" style="aspect-ratio:%s">\n'
        '            <picture>\n'
        '              <source type="image/webp" srcset="%s" sizes="%s">\n'
        '              <img src="%sassets/img/%s-1000.jpg" alt="%s" width="%d" height="%d" loading="%s">\n'
        '            </picture>\n'
        '          </div>'
        % (klasse, verhaeltnis, quellen, sizes, p, stem, alt, breite, hoehe, laden)
    )


def kopfbild(stem, alt, ueber, kicker, vor, breite=1920, hoehe=1440, p="", fokus=None):
    """Kleiner Auftakt fuer die Unterseiten - dieselbe Achse wie der Hero."""
    quellen = ", ".join(
        "%sassets/img/%s-%d.webp %dw" % (p, stem, g, g) for g in (640, 1000, 1600, 1920)
    )
    return u"""  <section class="hero hero--klein">
    <div class="hero__bild">
      <picture>
        <source type="image/webp" srcset="{quellen}" sizes="100vw">
        <img src="{p}assets/img/{stem}-1000.jpg" alt="{alt}" width="{breite}" height="{hoehe}" fetchpriority="high"{fokus}>
      </picture>
    </div>
    <div class="hero__schleier"></div>
    <div class="wrap hero__innen">
      <p class="hero__kicker"><span>{kicker}</span></p>
      <h1 class="t-gross">{ueber}</h1>
      <p class="hero__vor">{vor}</p>
    </div>
  </section>
""".format(quellen=quellen, p=p, stem=stem, alt=alt, breite=breite, hoehe=hoehe,
           kicker=kicker, ueber=ueber, vor=vor,
           fokus=(' style="object-position:%s"' % fokus) if fokus else "")


# ---------------------------------------------------------------------------
# Selbstkontrolle - was hier durchrutscht, sieht der Besucher.
# ---------------------------------------------------------------------------

VERDAECHTIG = [
    ("{'", u"Python-Wörterbuch im HTML gelandet"),
    ('%(', u"unaufgelöster Platzhalter"),
    ('&amp;nbsp;', u"doppelt maskiertes Leerzeichen"),
    ('None', u"None im Text"),
]


def pruefen(dateien):
    fehler = []
    for datei in dateien:
        with io.open(os.path.join(HIER, datei), encoding="utf-8") as f:
            text = f.read()
        for muster, warum in VERDAECHTIG:
            if muster in text:
                fehler.append(u"%s: %s (%s)" % (datei, warum, muster))
        if "<!--PFLICHTLINKS-->" not in text:
            fehler.append(u"%s: <!--PFLICHTLINKS--> fehlt" % datei)
        # Offene Prozentzeichen aus der Formatierung wuerden als %% stehenbleiben
        if re.search(r"%[a-zA-Z(]", re.sub(r"%20|%C3|%[0-9A-F]{2}", "", text)):
            treffer = re.findall(r".{18}%[a-zA-Z(].{12}", text)[:3]
            fehler.append(u"%s: verdächtiges Prozentzeichen: %r" % (datei, treffer))
    return fehler


if __name__ == "__main__":
    import inhalte

    gebaut = inhalte.alles(seite, bild, kopfbild)
    for datei, groesse in gebaut:
        print("%-28s %7d Zeichen" % (datei, groesse))

    probleme = pruefen([d for d, _ in gebaut])
    if probleme:
        print("\nPROBLEME:")
        for p in probleme:
            print("  " + p)
        raise SystemExit(1)
    print("\nAlle Seiten geprüft: keine Platzhalter-Reste, PFLICHTLINKS überall gesetzt.")
