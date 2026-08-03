# Briefing: neue Website Straßenbahnmuseum Leipzig

Stand: 2026-08-02 · deterministisch erzeugt aus dem Signal (Stufe 1 der Freestyle-Baulane).
Dieses Dokument ist ein KONZEPT-Briefing, keine Bauvorlage. Es sagt, WORUM es geht
und WORAN gemessen wird - nicht, wie die Seite aufgebaut zu sein hat.

## 1. Das Haus

- **Objekt:** Straßenbahnmuseum Leipzig
- **Ort:** Leipzig
- **Bisherige Website:** http://www.strassenbahnmuseum.de/
- **Anlass:** Vereinsmuseum Leipzig, Maps 4,7 bei 351 Bewertungen, starke Reputation ohne digitale Entsprechung, Nahbereich Agentur
- **Zielordner im Repo:** strassenbahnmuseum-leipzig-freestyle
- **Spaetere Adresse:** https://nx7-projects.github.io/Leads/strassenbahnmuseum-leipzig-freestyle/

## 2. Ist-Stand und Messlatte

Befund zur bisherigen Seite (aus der Recherche, MATERIAL):

> Seite liefert nur Hinweis auf veralteten Browser statt Inhalt; Inhalte an Alt-JavaScript gebunden, 1px-Platzhalterbilder, kein maschinenlesbarer Text, keine Öffnungszeiten im Quelltext, nicht responsiv

**Die Abnahme misst genau eine Frage:** Sieht die neue Seite besser aus als http://www.strassenbahnmuseum.de/?
Ruf die alte Seite auf, bevor du anfaengst. Was sie richtig macht, uebernimmst du;
was sie falsch macht, ist deine Chance. "Besser" heisst hier: fuer den Besucher
des Hauses besser - schneller zur Information, verstaendlicher, ansehnlicher.

## 3. Recherche - du recherchierst SELBST

Du darfst und sollst eigenstaendig recherchieren: Websuche, die alte Seite, oeffentliche
Quellen, Karten- und Bewertungsportale, Presse. Das ist ausdruecklich Teil des Auftrags.

**Belegpflicht (die einzige harte Recherche-Regel):** keine Oeffnungszeit, kein Preis,
keine Trager- oder Jahresangabe ohne abgerufene Quelle. Unbelegtes wird WEGGELASSEN,
nie geraten. Jede uebernommene Tatsache mit Quellen-URL in `QUELLEN.md` im Zielordner.

Fragen, die diese Kampagne beantwortet haben will:
- Wer traegt das Haus (Verein, Kommune, Stiftung, privat)?
- Oeffnungszeiten, Saison, Schliesstage, Eintrittspreise - mit Quelle.
- Was ist die eine Sache, die dieses Haus einzigartig macht?
- Was steht an: Veranstaltungen, Jubilaeen, Sonderausstellungen?
- Welches frei lizenzierte Bildmaterial gibt es (Urheber, Lizenz, Quelle)?
- Anfahrt, Parken, oeffentlicher Nahverkehr, Barrierefreiheit vor Ort.

## 4. Ton, Referenzklasse, Publikum

- **Ton:** Einladend und selbstbewusst, ohne Werbesprache. Das Haus spricht ueber sich, nicht ueber uns. Kurze Saetze, konkrete Zahlen, keine Superlative ohne Beleg.
- **Referenzklasse:** Websites gut gefuehrter Haeuser und Studios: grosse Bilder, grosse Typografie, viel Ruhe, ein klarer Weg zur wichtigsten Information.
- **Publikum:** Menschen, die einen Besuch planen (Zeiten, Preise, Anfahrt, Barrierefreiheit) und Menschen, die zum ersten Mal von dem Haus hoeren.

Was diese Seite fuer das Haus leisten soll:
- Die wichtigste Besucherinformation ist in einem Blick erfassbar.
- Das Haus sieht aus wie das, was es tatsaechlich leistet.
- Auf dem Telefon genauso benutzbar wie am Rechner.
- Barrierefrei - das ist bei oeffentlich getragenen Haeusern Pflicht und wird selten eingeloest.

- Das Haus ist noch kein Kunde und sieht diese Seite, bevor es zahlt. Qualitaet entscheidet ueber den Verkauf.
- Lieber wenige, gute Bilder als viele beliebige. Ohne passendes Bild: typografisch stark und bildarm.

## 5. Deine Freiheit (das ist der Kern dieses Briefings)

Es gibt KEINE Struktur-, Seitenzahl- oder Bausteinvorgaben. Konkret:

- so viele Seiten, wie gut ist - es gibt keine Obergrenze
- eigene Schriften (lokal eingebunden), eigenes CSS, eigenes JavaScript
- eigene Sektionen, eigene Interaktion, eigene Bildsprache
- kein Baukasten, keine Bausteinliste, kein vorgegebenes Layout
- keine harten Build-Budgets: Performance ist spaetere Optimierung, keine Bauvorgabe

Was trotzdem gilt, weil es das Haus sonst Geld oder Ruf kostet:

- barrierefrei (WCAG 2.2 AA): Kontraste, Fokus sichtbar, Tastaturbedienung,
  `prefers-reduced-motion`, sinnvolle Alternativtexte
- nur frei lizenziertes oder eigenes Bildmaterial, jedes Bild mit Nachweis-Angabe
- kein Tracker, keine externen Schriften/CDNs, kein Cookie-Banner (es gibt nichts einzuwilligen)
- kein Platzhaltertext, keine erfundenen Fakten

## 6. Was du fuer Stufe 3 hinterlegst (Pflichtteile)

Impressum, Datenschutz, Barrierefreiheitserklaerung und Bildnachweis schreibst du
NICHT selbst - die setzt Stufe 3 deterministisch obendrauf, aus geprueften Vorlagen.
Damit sie in DEIN Design passen, brauchst du genau zwei Dinge:

1. **`rahmen.html`** im Zielordner: eine vollstaendige HTML-Seite in deinem Design
   (Kopf, Navigation, Fuss) mit dem Platzhalter `<!--PFLICHT-INHALT-->` an der Stelle, an der
   der Fliesstext steht, und `<title>{{TITEL}}</title>` im Kopf. Style dabei die
   Klasse `.rechtstext` (h1/h2/p/ul/a im Fliesstext) mit - die Pflichtseiten benutzen sie.
2. **`pflichtteile.json`** im Zielordner: die recherchierten Angaben als JSON
   (Schema unten). Was du nicht belegen kannst, laesst du weg - Stufe 3 meldet die
   Luecke, statt sie zu erfinden.

Ausserdem setzt du in JEDE gebaute HTML-Seite (auch die Startseite) den Platzhalter
`<!--PFLICHTLINKS-->` an die Stelle im Fussbereich, an der die Pflicht-Links stehen
sollen. Stufe 3 ersetzt ihn durch die fertige Linkliste samt Bildnachweis.

```json
{
  "haus": {
    "name": "Name des Traegers, genau wie im Register",
    "rechtsform": "Rechtsform, falls vorhanden",
    "adresse": {
      "strasse": "Musterweg 1",
      "plz": "00000",
      "ort": "Musterstadt"
    },
    "vertretung": "vertretungsberechtigte Person(en)",
    "telefon": "+49 000 000000",
    "email": "info@example.org",
    "register": "Registergericht und -nummer, falls eingetragen",
    "verantwortlich": "inhaltlich verantwortliche Person nach § 18 Abs. 2 MStV"
  },
  "datenschutz": {
    "hoster": "GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, USA",
    "kontaktformular": false
  },
  "barrierefreiheit": {
    "vereinbarkeit": "teilweise",
    "einschraenkungen": [
      "Historische PDF-Dokumente sind nicht barrierefrei."
    ]
  },
  "bilder": [
    {
      "stamm": "hero-aussenansicht",
      "datei": "Beispielbild.jpg",
      "urheber": "Vorname Nachname",
      "lizenz": "CC BY-SA 4.0",
      "lizenzUrl": "https://creativecommons.org/licenses/by-sa/4.0/",
      "quelle": "Wikimedia Commons",
      "seite": "https://commons.wikimedia.org/wiki/File:Beispielbild.jpg"
    }
  ]
}
```

`bilder` beschreibt jedes verwendete Bild (Dateistamm ohne Endung). Ohne diesen
Nachweis ist die Nutzung von CC-BY-Material unlizenziert - das ist kein Formalismus.

## 7. Abnahme

Nach dem Bau prueft ein unabhaengiger Pruefer (Altair):

1. Sind alle Pflichtteile vorhanden und von jeder Seite aus verlinkt?
2. Hat die Seite eine gute User Experience?
3. **Sieht sie besser aus als http://www.strassenbahnmuseum.de/?** - das ist das eigentliche Kriterium.
