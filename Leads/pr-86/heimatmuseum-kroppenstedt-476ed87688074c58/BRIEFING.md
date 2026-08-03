# Briefing: neue Website Heimatmuseum Kroppenstedt

Stand: 2026-08-03 · deterministisch erzeugt aus dem Signal (Stufe 1 der Freestyle-Baulane).
Dieses Dokument ist ein KONZEPT-Briefing, keine Bauvorlage. Es sagt, WORUM es geht
und WORAN gemessen wird - nicht, wie die Seite aufgebaut zu sein hat.

## 1. Das Haus

- **Objekt:** Heimatmuseum Kroppenstedt
- **Ort:** Kroppenstedt
- **Bisherige Website:** https://www.westlicheboerde.de/verzeichnis/objekt.php?mandat=142886
- **Anlass:** Ehrenamtliches Heimatmuseum der Boerde; von der Recherche als Kandidat mit sichtbarem Handlungsbedarf eingestuft (Nachschub-Recherche 03.08.2026)
- **Zielordner im Repo:** heimatmuseum-kroppenstedt-476ed87688074c58
- **Spaetere Adresse:** https://nx7-projects.github.io/Leads/heimatmuseum-kroppenstedt-476ed87688074c58/

## 2. Ist-Stand und Messlatte

Befund zur bisherigen Seite (aus der Recherche, MATERIAL):

> Kein eigener Auftritt: der Museumsinhalt haengt als Unterseite in der Behoerden-Navigation der Verbandsgemeinde (Buergerservice, Wahlen, Bekanntmachungen), Cookie-Hinweis vor dem Inhalt, Parameter-URL, kein Museums-Branding - firecrawl-geprueft

**Die Abnahme misst genau eine Frage:** Sieht die neue Seite besser aus als https://www.westlicheboerde.de/verzeichnis/objekt.php?mandat=142886?
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
- **Referenzklasse:** Preisverdaechtige Studio-Arbeit (Awwwards/Webflow-Showcase-Niveau, z.B. 5sdesign.art): mutige, grosszuegige Layouts, sehr grosse Typografie, viel Weissraum, ein starkes Bild statt vieler kleiner. Handgemacht wirkend, nie nach Baukasten. Der erste Bildschirm entscheidet.
- **Publikum:** Menschen, die einen Besuch planen (Zeiten, Preise, Anfahrt, Barrierefreiheit) und Menschen, die zum ersten Mal von dem Haus hoeren.

Was diese Seite fuer das Haus leisten soll:
- Die wichtigste Besucherinformation ist in einem Blick erfassbar.
- Das Haus sieht aus wie das, was es tatsaechlich leistet.
- Auf dem Telefon genauso benutzbar wie am Rechner.
- Barrierefrei - das ist bei oeffentlich getragenen Haeusern Pflicht und wird selten eingeloest.

- Das Haus ist noch kein Kunde und sieht diese Seite, bevor es zahlt. Qualitaet entscheidet ueber den Verkauf.
- Die Seite erzaehlt beim Scrollen eine Geschichte (Ankommen -> Entdecken -> Planen -> Besuchen) statt Informationen zu stapeln.
- Design-Anspruch ist das Unterscheidungsmerkmal: Der Inhalt sitzt meistens beim ersten Versuch, das Design entscheidet ueber den Verkauf. Lieber eine Sektion weniger, die dafuer sitzt.

## 4b. Handwerk: woran diese Seite gemessen wird

**Gestaltung**

- EIGENSTAENDIGKEIT (oberste Regel): Die Seite muss aussehen, als waere sie fuer genau dieses Haus entworfen. Der Test: Tauscht man Texte und Logo aus, darf das Design NICHT fuer ein beliebiges anderes Haus weiterfunktionieren. Farbwelt, Schriftwahl und Layout-Motive begruenden sich aus dem Gegenstand - aus Material, Ort, Geschichte und Arbeit des Hauses. Ein Dachdeckerbetrieb braucht eine andere, geerdetere Seite als eine Anwaltskanzlei.
- KEINE KI-REFLEXE: Die immergleichen Automatik-Muster sind nur erlaubt, wenn ein Grund aus dem Haus sie traegt - sonst weg: dunkles Theme als Ausgangspunkt, Violett-/Neon-Verlaeufe und Glow-Effekte, drei identische Kacheln nebeneinander, derselbe Eckenradius an jedem Element, der zentrierte Einheits-Hero (Riesenueberschrift, Unterzeile, zwei Knoepfe), Emojis als Icons. Wer eines dieser Mittel einsetzt, muss sagen koennen, warum es aus DIESEM Haus kommt.
- EIN SYSTEM: Eine Farbwelt aus dem Material und der Welt des Hauses, zwei Schriften, eine feste Abstandsskala - jede Unterseite traegt erkennbar dieselbe Handschrift. Einzigartig heisst EIN eigenes, durchgezogenes System, nicht viele Einfaelle nebeneinander.
- TYPOGRAFIE ALS ENTSCHEIDUNG: Schriftwahl ist Gestaltung, kein Default. Eigene Schriften lokal einbinden, Mut zu sehr grossen Ueberschriften und bewussten Gewichten. Die Schrift muss zum Charakter des Hauses passen und begruendbar sein - eine austauschbare Standardschrift fuer alles ist ein Rueckfall in die Vorlage.
- MIKRO-DETAILS: Handgemacht wirkt eine Seite durch kleine, bewusste Entscheidungen - Hover-Zustaende, die antworten; kurze Subtexte und Randnotizen an unerwarteten Stellen; asymmetrische Raster, wo der Inhalt sie traegt; ein wiederkehrendes Motiv aus der Welt des Hauses. Mindestens zwei solcher Details je Seite, die es nur fuer DIESES Haus geben kann. Das ist ein Werkzeugkasten, keine Checkliste - alles ueberall ist so schlimm wie nichts.
- ERZAEHLUNG: Visuell erzaehlen statt mit Text zuzufuellen - kurze Textbloecke, starke Bilder, Zahlen als Gestaltungselemente. Niemand liest Absaetze, alle lesen Ueberschriften.
- AUSRICHTUNG: Text konsequent linksbuendig an EINER Achse. Ueberschrift, Unterzeile und Knopf beginnen exakt an derselben Kante - auch wenn ein Hintergrundbild dahinterliegt. Zentrierter Text nur, wenn ein Block bewusst als Ausnahme gesetzt ist (Zitat, Zahlenreihe), nie im Hero.
- ABSTAENDE: EINE Skala fuer alles (z.B. 8/16/24/40/64/96 px), keine krummen Einzelwerte. Gleiche Bausteine haben ueberall denselben Innen- und Aussenabstand. Ungleiche Abstaende sind der haeufigste Grund, warum eine Seite billig aussieht.
- BEWEGUNG: Scroll-Reveals fuer jeden groesseren Abschnitt (sanftes Einblenden mit leichtem Versatz), dazu gezielt Zaehler, Parallax oder Sticky-Elemente, wo sie die Geschichte tragen. Nie ruckelig, nie Selbstzweck, immer mit prefers-reduced-motion abschaltbar.
- RESPONSIV: Auf dem Telefon zuerst denken. Kein horizontales Scrollen, Schrift skaliert fluid (clamp), Bilder mit srcset, Tabellen/Zahlenreihen brechen sauber um. Touch-Ziele mindestens 44 px.
- SAUBERE ADRESSEN: Interne Links NIE auf "index.html" zeigen - die Startseite ist "./" bzw. "../". Unterseiten bleiben sprechend (besuch.html). Keine Dateiendung im sichtbaren Text.
- BILDER: eher wenige, dafuer gross und gut. Ein schwaches Bild klein zu setzen macht es nicht besser - dann lieber typografisch loesen.
- SCHWEBENDER KONTAKTKNOPF: unten rechts ein dezenter, immer sichtbarer Knopf (Kontakt/Anfahrt/Termine - was fuer dieses Haus zaehlt). Blendet sich aus, sobald der Fuss erreicht ist. Auf dem Telefon nicht den Inhalt verdecken.

**Inhalt und Verweise**

- EXTERNE LINKS DES HAUSES UEBERNEHMEN: Was die bisherige Seite verlinkt und weiterhin gilt, gehoert auch auf die neue - Shop, Foerderkreis, Traeger, Dachverband, Partner, Social-Profile, Spendenseite. Pruefen, ob der Link noch lebt; tote Links weglassen. Diese Verweise sind fuer das Haus oft eine Einnahmequelle - sie zu verlieren ist ein echter Schaden.
- LOGO: das ECHTE Logo/Wappen des Hauses verwenden, wenn es frei verfuegbar ist (Website, Wikimedia, Pressebereich) - Quelle im Bildnachweis. Nur wenn es keins gibt, eine eigene Wortmarke setzen und das im Bericht vermerken.
- KONTAKTWEGE VOLLSTAENDIG: Telefon, E-Mail, Anschrift, Anfahrt mit oeffentlichem Nahverkehr - so wie das Haus sie selbst angibt.
- NICHTS ERFINDEN: Was nicht belegt ist, faellt weg - und wird im Bericht als Luecke genannt, nicht stillschweigend uebergangen.

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
3. **Sieht sie besser aus als https://www.westlicheboerde.de/verzeichnis/objekt.php?mandat=142886?** - das ist das eigentliche Kriterium.
