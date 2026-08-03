# Museum Eisenhammer Dorfchemnitz — Website

Statische Website für das Museum Eisenhammer Dorfchemnitz (Erzgebirge).
Kein Framework, kein Build-Schritt, keine externen Dienste: HTML, ein CSS,
ein JavaScript, lokal eingebundene Schriften.

Live: <https://nx7-projects.github.io/Leads/museum-eisenhammer-dorfchemnitz-a319bcfd0e844fb1/>

## Seiten

| Datei | Inhalt |
| --- | --- |
| `index.html` | Auftakt, Besucherleiste, Antrieb, Übertragung, Chronik, Bestand, Veranstaltungen, Besuch |
| `werk.html` | Technik im Einzelnen: Graben, Rad, Daumenwelle, Schwanzhämmer, Erzeugnisse, Gelände |
| `geschichte.html` | Chronik 1365–2013, Brief von 1615, Literatur |
| `besuch.html` | Öffnungszeiten, Preise, Anfahrt, Barrierefreiheit, Termine, Kontakt |
| `foerderverein.html` | Ziele, Veranstaltungen, Schmiedekurse, Spendenkonto |
| `rahmen.html` | Seitenhülle für die Pflichtseiten (Stufe 3), mit `{{TITEL}}` und `<!--PFLICHT-INHALT-->` |

Jede gebaute Seite enthält im Fußbereich `<!--PFLICHTLINKS-->`; Stufe 3 setzt dort
die Linkliste ein und erzeugt Impressum, Datenschutz, Barrierefreiheitserklärung
und Bildnachweis aus `pflichtteile.json`.

## Gestaltung

Die Farbwelt kommt aus dem Haus: Kalkputz der Hammergebäude (`--kalk`), Schieferdach
(`--schiefer`), Ruß im Hammerhaus (`--russ`), glühendes Eisen (`--glut`, `--funke`).
Helle Abschnitte stehen für draußen — Bach, Hof, Jahreszahlen; dunkle Abschnitte
für drinnen — Hammerhaus, Esse, Schlag.

Schriften: **Big Shoulders Display** (schmale Industrie-/Signaturschrift, Entsprechung
zum geschmiedeten Giebelschriftzug) und **Newsreader** (Chronik-Antiqua für 660 Jahre
Betriebsgeschichte). Beide OFL, lokal eingebunden.

Wiederkehrende Motive: der **Hammergraben** als gekerbte Trennlinie (`.graben`), die
**Schlagzahl** der beiden Schwanzhämmer als Animation im belegten Takt (60 bzw. 100
Schläge je Minute), und technische Zahlen als Gestaltungselement (`.kennzahlen`).

Abstände laufen über eine einzige Skala (`--s1` … `--s7` = 8/16/24/40/64/96/144 px).

## Barrierefreiheit

WCAG 2.2 AA angestrebt: Sprungmarke, sichtbarer Fokus, Tastaturbedienung der
Navigation, Kontraste geprüft (heller und dunkler Grund getrennt gesetzt),
`prefers-reduced-motion` schaltet Animation und Sanftscroll ab, Alternativtexte
beschreiben die Motive. Ohne JavaScript ist die Seite vollständig lesbar —
Einblendeffekte greifen nur, wenn `html.js` gesetzt ist.

## Bilder neu erzeugen

`bilder.py` erzeugt alle Varianten aus den vier Originalen von Wikimedia Commons
(Dateinamen siehe Kopf des Skripts):

```sh
python bilder.py <verzeichnis-mit-originalen>
```

## Belege

Jede Tatsachenangabe ist in `QUELLEN.md` mit Quelle und Abrufdatum belegt.
Dort stehen auch die bewusst weggelassenen Angaben.
