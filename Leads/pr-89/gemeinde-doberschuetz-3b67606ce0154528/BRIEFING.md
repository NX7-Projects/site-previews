# Briefing: neue Website Gemeinde Doberschütz

Stand: 2026-08-06 · deterministisch erzeugt aus dem Signal (Stufe 1 der Freestyle-Baulane).
Dieses Dokument ist ein KONZEPT-Briefing, keine Bauvorlage. Es sagt, WORUM es geht
und WORAN gemessen wird - nicht, wie die Seite aufgebaut zu sein hat.

## 1. Das Haus

- **Objekt:** Gemeinde Doberschütz
- **Ort:** Doberschütz (Landkreis Nordsachsen, Sachsen)
- **Bisherige Website:** https://www.doberschuetz.de/
- **Anlass:** Kleine Landgemeinde mit acht Ortsteilen (Battaune, Doberschütz, Mörtitz, Rote Jahne, Paschwitz, Bunitz/Mölbitz, Sprotta, Wöllnau) im Landkreis Nordsachsen - genau das Zielsegment: eigene Verwaltung, keine kreisfreie Stadt, Vergabe in dieser Größe typischerweise freihändig. Einwohnerzahl unter 10.000 plausibel, aber nicht belegt (unverifiziert). Auf der Seite läuft aktuell eine kommunale Wärmeplanung mit eigenem Unterbereich inkl. FAQ - erkennbarer Bedarf, Bürgerinformation verständlich zu transportieren. Kein Hinweis auf eine laufende öffentliche Ausschreibung für die Website gefunden (Rubrik "öffentliche Ausschreibungen" existiert, Inhalt nicht geprüft).
- **Zielordner im Repo:** gemeinde-doberschuetz-3b67606ce0154528
- **Spaetere Adresse:** https://nx7-projects.github.io/Leads/gemeinde-doberschuetz-3b67606ce0154528/

## 2. Ist-Stand und Messlatte

Befund zur bisherigen Seite (aus der Recherche, MATERIAL):

> Technisch veraltetes Weblication-CMS mit statischen .php-Seiten und navid-Parametern in den Links; Layout mit Slider-Thumbnails und "Druckansicht" entspricht dem Stand der frühen 2010er. Domain-Bruch: Einstieg über doberschuetz.de, alle Inhalte liegen auf doberschuetz.eu - schlecht für Vertrauen, Auffindbarkeit und Verlinkung durch Bürger. Cookie-Hinweis arbeitet mit Zustimmungsfiktion ("Durch die Nutzung der Webseite stimmen Sie der Verwendung von Cookies zu") statt mit echter Einwilligung. Inhalte teils nur als PDF (z.B. Belegungsplan Turnhalle) statt als barrierefreie HTML-Seite. Eine Barrierefreiheitserklärung ist verlinkt, ihr Inhalt war beim Abruf jedoch nicht als Text auslesbar - Hinweise auf Leichte Sprache oder Gebärdensprache (BITV-Pflicht für öffentliche Stellen) waren nicht auffindbar; ob sie fehlen, ist unverifiziert.

**Die Abnahme misst genau eine Frage:** Sieht die neue Seite besser aus als https://www.doberschuetz.de/?
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
- Traegerschaft: eigenstaendige Gemeinde, Ortsteil einer groesseren Gemeinde, Mitgliedsgemeinde einer Verwaltungsgemeinschaft oder eines Amtes? Wer betreibt die Website tatsaechlich?
- Einwohnerzahl mit Stichtag und Quelle (bestimmt spaeter die Preisstufe).
- Rathaus / Buergerbuero: Anschrift, Telefon, E-Mail, Oeffnungs- und Sprechzeiten, abweichende Zeiten.
- Buergermeisterin oder Buergermeister: Name, Amtsbezeichnung, Sprechstunde.
- Die drei bis fuenf haeufigsten Anliegen: An- und Ummeldung, Personalausweis, Hundesteuer, Abfallkalender, Gewerbeanmeldung, Standesamt - welche gelten fuer DIESE Gemeinde?
- Amtliche Bekanntmachungen: wo werden sie heute veroeffentlicht (Amtsblatt, Aushang, Website), wie oft?
- Gremien: Gemeinderat, Ausschuesse, Sitzungstermine, Protokolle - oeffentlich einsehbar?
- Einrichtungen vor Ort: Kita, Schule, Feuerwehr, Bibliothek, Sporthalle, Friedhof, Aerzte.
- Vereine und regelmaessige Veranstaltungen.
- Abfallkalender und Entsorgung: wer ist zustaendig (meist der Landkreis), gibt es eine verlinkbare Quelle?
- Anfahrt, Parken, oeffentlicher Nahverkehr.
- Gibt es auf der bestehenden Seite eine Barrierefreiheitserklaerung? (Meist nicht - das ist der staerkste Befund.)
- Frei lizenziertes Bildmaterial der Gemeinde: Urheber, Lizenz, Quelle. Ortsansichten, Wahrzeichen, Rathaus.

## 4. Ton, Referenzklasse, Publikum

- **Ton:** Sachlich, freundlich, kurze Saetze. Eine Verwaltung, die klingt wie eine Werbeagentur, verliert Vertrauen - kein Marketing-Ton, keine Superlative, keine Ausrufezeichen. Amtsdeutsch ist aber genauso falsch: schreibe so, wie eine hilfsbereite Person am Buergerbuero-Schalter spricht.
- **Referenzklasse:** NICHT die mutige Studio-Arbeit aus der Kultur-Kampagne. Vorbild sind gut gemachte oeffentliche Digitalangebote: ruhig, kontraststark, grosse gut lesbare Schrift, sehr klare Informationsarchitektur, viel Weissraum, wenige Farben. Die Qualitaet zeigt sich hier in der Ordnung, nicht in der Geste. Eine Gemeindeseite darf langweilig aussehen, solange sie souveraen aussieht - sie darf nie billig oder improvisiert aussehen.
- **Publikum:** Einwohnerinnen und Einwohner mit einem konkreten Anliegen (Oeffnungszeiten, Formular, Muellabfuhr, Ansprechpartner, Termin) - das ist die grosse Mehrheit der Aufrufe. Dahinter: Zugezogene und Auswaertige, die sich orientieren, sowie Presse und Vereine, die Bekanntmachungen und Termine suchen.

Was diese Seite fuer das Haus leisten soll:
- Barrierefreiheit ist fuer oeffentliche Stellen seit 2019 Pflicht (BITV 2.0). Die meisten kleinen Gemeindeseiten erfuellen sie nicht und haben nicht einmal die vorgeschriebene Erklaerung.
- Die drei haeufigsten Anliegen sind in einem Blick erreichbar - das entlastet das Buergerbuero am Telefon.
- Auf dem Telefon genauso benutzbar wie am Rechner.
- Gehostet in Deutschland, Betrieb und Pflege inklusive.

- Die Gemeinde ist noch kein Kunde und sieht diese Seite, bevor sie zahlt. Qualitaet entscheidet ueber den Verkauf.
- Der haeufigste Fehler kommunaler Seiten ist nicht Haesslichkeit, sondern Suchen: alles ist da, aber niemand findet es. Wenn du zwischen schoener und auffindbarer entscheiden musst, entscheide fuer auffindbar.
- Eine Verwaltungsgemeinschaft traegt oft mehrere Orte. Pruefe, ob die Seite fuer EINE Gemeinde oder fuer den Verbund gedacht ist - das aendert die gesamte Struktur.
- Design-Anspruch bleibt hoch: lieber eine Sektion weniger, die dafuer sitzt.

## 4b. Handwerk: woran diese Seite gemessen wird

**Gestaltung**

- EIGENSTAENDIGKEIT (oberste Regel): Die Seite muss aussehen, als waere sie fuer genau dieses Haus entworfen. Der Test: Tauscht man Texte und Logo aus, darf das Design NICHT fuer ein beliebiges anderes Haus weiterfunktionieren. Farbwelt, Schriftwahl und Layout-Motive begruenden sich aus dem Gegenstand - aus Material, Ort, Geschichte und Arbeit des Hauses. Ein Dachdeckerbetrieb braucht eine andere, geerdetere Seite als eine Anwaltskanzlei.
- KEIN NAHELIEGENDER GRIFF: Bei einem Sanierungsziel wie "altes Gebaeude, Fachwerk oder Backstein" ist die naheliegende Antwort ein warmer Kalk-Weiss-Ton plus Ziegelrot - GENAU DESHALB ist sie meistens die falsche. Bevor du eine Materialfarbe setzt: was ist an DIESEM Gebaeude untypisch fuer seine Bauzeit/Region (eine bestimmte Steinsorte, ein ungewoehnlicher Anstrich, eine Epoche, ein Handwerk, das nicht "historisch" ist)? Zwei Haeuser mit aehnlicher Bausubstanz muessen zu ERKENNBAR verschiedenen Paletten kommen - sonst ist "aus dem Material abgeleitet" nur ein neuer Automatismus.
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
- ENTWURFS-KENNZEICHNUNG, PFLICHT AUF JEDER SEITE: Ein deutlich sichtbarer Hinweis, der nicht wegscrollt und nicht wegklickbar ist - "Unverbindlicher Entwurf. Dies ist NICHT die amtliche Website der Gemeinde {objekt}." mit Link auf {alte_url}. Er gehoert an den oberen Rand, in ausreichendem Kontrast, und er ist Teil des Designs statt ein aufgeklebtes Banner. Diese Regel ist nicht verhandelbar: ohne sie ist die Seite eine Kopie unter fremdem Namen.
- KEIN Hoheitszeichen. Wappen, Dienstsiegel und Amtsschilder der Gemeinde werden NICHT nachgebaut oder uebernommen - ihre Fuehrung ist rechtlich geregelt. Arbeite mit Ortsansicht, Typografie und Farbwelt.
- BARRIEREFREIHEIT IST DER VERKAUFSHEBEL, also bau sie sichtbar richtig: Kontrastverhaeltnis mindestens 4,5:1 fuer Fliesstext, jedes Bedienelement per Tastatur erreichbar mit sichtbarem Fokus, echte Ueberschriften-Hierarchie, Alt-Texte, Schriftgroesse ab 18px im Fliesstext, kein reines Grau-auf-Grau.
- SCHWEBENDER KONTAKTKNOPF unten rechts, dezent und immer sichtbar (Rathaus / Kontakt / Termin - was fuer diese Gemeinde zaehlt). Blendet sich am Fuss aus. Verdeckt auf dem Telefon nie den Inhalt.
- Jeder Anker muss ein Ziel haben: zu jedem href="#x" gehoert ein Element mit id="x". Am 05.08.2026 zweimal derselbe Fehler live gefunden.

**Inhalt und Verweise**

- EXTERNE LINKS DES HAUSES UEBERNEHMEN: Was die bisherige Seite verlinkt und weiterhin gilt, gehoert auch auf die neue - Shop, Foerderkreis, Traeger, Dachverband, Partner, Social-Profile, Spendenseite. Pruefen, ob der Link noch lebt; tote Links weglassen. Diese Verweise sind fuer das Haus oft eine Einnahmequelle - sie zu verlieren ist ein echter Schaden.
- LOGO: das ECHTE Logo/Wappen des Hauses verwenden, wenn es frei verfuegbar ist (Website, Wikimedia, Pressebereich) - Quelle im Bildnachweis. Nur wenn es keins gibt, eine eigene Wortmarke setzen und das im Bericht vermerken.
- KONTAKTWEGE VOLLSTAENDIG: Telefon, E-Mail, Anschrift, Anfahrt mit oeffentlichem Nahverkehr - so wie das Haus sie selbst angibt.
- NICHTS ERFINDEN: Was nicht belegt ist, faellt weg - und wird im Bericht als Luecke genannt, nicht stillschweigend uebergangen.
- BELEGPFLICHT, haerter als bei Kultur: Oeffnungszeiten, Gebuehren, Zustaendigkeiten und Fristen sind Amtsangaben. Eine falsche Amtsangabe schickt Menschen vor eine verschlossene Tuer. Was nicht belegt ist, wird weggelassen - niemals geraten, niemals geschaetzt, niemals "ueblicherweise".
- AMTLICHE BEKANNTMACHUNGEN UND GEBUEHREN NUR ALS PLATZHALTER. Baue den Ort dafuer (Struktur, Datum, Aufbau), aber uebernimm keine echten Bekanntmachungstexte und keine echten Gebuehrensaetze aus der alten Seite in den Entwurf. Sie haben Rechtswirkung und gehoeren der Verwaltung, nicht uns.
- Der erste Bildschirm gehoert dem Buergerservice, nicht dem Ortsbild. Ein schoenes Bild darf da sein - aber Oeffnungszeiten, Kontakt und die haeufigsten Anliegen muessen ohne Scrollen erreichbar sein.
- Verlinke ehrlich nach aussen, wo die Zustaendigkeit aussen liegt (Landkreis, Verwaltungsgemeinschaft, Buergerportal des Landes). Eine Gemeindeseite, die so tut, als koenne sie alles selbst, ist schlechter als eine, die klar weiterleitet.
- Keine erfundenen Personen, keine erfundenen Vereine, keine erfundenen Termine.

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
3. **Sieht sie besser aus als https://www.doberschuetz.de/?** - das ist das eigentliche Kriterium.
