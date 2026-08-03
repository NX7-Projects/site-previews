# Torhaus Dölitz mit Zinnfigurenmuseum — Website

Statische Website, kein Framework, kein Build-Schritt beim Ausliefern.
Öffnen genügt: `index.html`.

## Seiten

| Datei | Inhalt |
|---|---|
| `index.html` | Startseite: Ankommen → Entdecken → Planen → Besuchen |
| `besuch.html` | Öffnungszeiten, Eintritt, Führungen, Anfahrt, Barrierefreiheit |
| `museum.html` | Dauerausstellung, Großdiorama, Sonderausstellungen |
| `geschichte.html` | Zeitleiste Dölitz und Torhaus, die Gedenktafeln |
| `veranstaltungen.html` | Termine 2026 |
| `unterstuetzen.html` | Patenschaften, Spende, Shop, Vermietung, Partner |
| `rahmen.html` | Hülle für die Pflichtseiten (siehe unten) |

## Pflichtteile

Impressum, Datenschutz, Barrierefreiheitserklärung und Bildnachweis werden
nicht hier geschrieben, sondern in der nächsten Stufe deterministisch erzeugt.
Dafür liegen bereit:

- **`rahmen.html`** — vollständige Seite im Design des Hauses, mit
  `<title>{{TITEL}}</title>` und `<!--PFLICHT-INHALT-->` an der Stelle des
  Fließtexts. Die Klasse `.rechtstext` ist gestaltet (h1/h2/h3/p/ul/ol/a/dl/table).
- **`pflichtteile.json`** — die recherchierten Angaben, inklusive vollständigem
  Bild- und Schriftnachweis. Nicht belegbare Felder fehlen absichtlich; welche
  das sind, steht am Ende von `QUELLEN.md`.
- **`<!--PFLICHTLINKS-->`** steht im Fußbereich **jeder** Seite.

## Gestaltung

Alles ist aus dem Haus abgeleitet, nicht aus einer Vorlage:

- **Farbe** — Kalkputz der Fassade, Zinn (das Material der Figuren),
  Dachziegel, Sandstein der Bogenquader.
- **Schrift** — *Bodoni Moda* für alles Große: die Antiqua der Epoche, von der
  dieses Haus erzählt; Giambattista Bodoni starb 1813. *Archivo* für Lesetext
  und Beschriftung, ruhig und gut in kleinen Graden wie ein Objektschild.
  Beide OFL 1.1, lokal unter `assets/fonts/` — kein externes CDN.
- **Motiv** — der Rundbogen. Das Torhaus *ist* ein Durchgang; der Bogen ist die
  einzige runde Form im ganzen System. Alles andere hat Kanten.
- **Abstände** — eine Skala: 4 / 8 / 16 / 24 / 40 / 64 / 96 / 160 px.
- **Achse** — Überschrift, Vorspann und Knopf beginnen an derselben Kante.

Kein Tracker, kein Cookie-Banner (es gibt nichts einzuwilligen), keine externen
Ressourcen. Ohne JavaScript ist die Seite vollständig lesbar und bedienbar.

## Bearbeiten

Kopf, Fuß und Seitenhülle sind auf allen Seiten identisch. Damit das so bleibt,
werden die HTML-Dateien aus zwei Python-Dateien erzeugt:

```
python bauen.py
```

- `bauen.py` — Hülle, Navigation, Bausteine, Selbstkontrolle
- `inhalte.py` — sämtliche Texte

Das Skript prüft nach dem Schreiben, ob Platzhalter aufgelöst wurden und
`<!--PFLICHTLINKS-->` auf jeder Seite steht, und bricht sonst ab.
Wer nur einen Text ändern will, kann das auch direkt im HTML tun — dann aber
in allen betroffenen Dateien gleich.

Bilder in `assets/img/` liegen als WebP in 640 / 1000 / 1600 (Vollbildbilder
zusätzlich 1920) plus ein JPEG mit 1000 px als Rückfallebene.

## Belege

Jede Zahl, jede Öffnungszeit und jeder Preis auf dieser Seite ist in
`QUELLEN.md` mit Quelle und Abrufdatum belegt. Dort steht auch, was sich nicht
belegen ließ und deshalb bewusst fehlt.
