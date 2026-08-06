# -*- coding: utf-8 -*-
"""
Torhaus Doelitz - die Texte.

Jede Tatsache hier stammt aus einer abgerufenen Quelle; die Belege stehen in
QUELLEN.md. Was nicht belegt war, steht nicht hier.
"""


def alles(seite, bild, kopfbild):
    raus = []

    # =======================================================================
    # STARTSEITE - Ankommen, Entdecken, Planen, Besuchen
    # =======================================================================

    start = u"""
  <!-- ANKOMMEN ---------------------------------------------------------- -->
  <section class="hero">
    <div class="hero__bild">
      <picture>
        <source type="image/webp" srcset="assets/img/hero-torbogen-640.webp 640w, assets/img/hero-torbogen-1000.webp 1000w, assets/img/hero-torbogen-1600.webp 1600w, assets/img/hero-torbogen-1920.webp 1920w" sizes="100vw">
        <img src="assets/img/hero-torbogen-1000.jpg" alt="Das Torhaus Dölitz: der Rundbogen des Tores, darüber der Barockgiebel, davor die hölzerne Brücke über die Mühlpleiße." width="1920" height="1440" fetchpriority="high">
      </picture>
    </div>
    <div class="hero__schleier"></div>
    <div class="wrap hero__innen">
      <p class="hero__kicker">
        <span>Leipzig&nbsp;· Dölitz</span>
        <span>Torhaus von 1670</span>
        <span>Museum seit 1960</span>
      </p>
      <h1 class="t-riesig">Treten Sie durch das Tor.</h1>
      <p class="hero__vor">
        Dahinter warten über 100.000 Zinnfiguren auf drei Etagen — und ein Schlachtfeld,
        auf dem Sie bereits stehen. Am 16. Oktober 1813 war dieser Hof einer der
        umkämpftesten Orte der Völkerschlacht bei Leipzig.
      </p>
      <p class="hero__tun">
        <a class="knopf knopf--hell" href="besuch.html">Besuch planen <span class="knopf__pfeil" aria-hidden="true">→</span></a>
        <a class="knopf knopf--umriss-hell" href="museum.html">Was Sie sehen</a>
      </p>
      <p class="hero__leiste">
        <span><b>Geöffnet</b> Mi · Sa · So · feiertags, 10–17 Uhr</span>
        <span><b>Einlass bis</b> 16.30 Uhr</span>
        <span><b>Eintritt</b> 5 € · ermäßigt 3 €</span>
        <span><b>Helenenstraße 24</b>, 04279 Leipzig</span>
      </p>
    </div>
  </section>

  <!-- DAS HAUS IN ZAHLEN ------------------------------------------------ -->
  <section class="band" aria-labelledby="zahlen-titel">
    <div class="wrap">
      <p class="schild">Das Haus in Zahlen</p>
      <h2 class="t-mittel" id="zahlen-titel" data-w="20" data-auf>
        Ein Torhaus, das mehr Bewohner hat als mancher Ort.
      </h2>
      <div class="zahlen">
        <div class="nische" data-auf data-gruppe="0">
          <span class="nische__zahl"><span data-zaehlen="100000">100.000</span><span class="nische__einheit">+</span></span>
          <p class="nische__was">Zinnfiguren in der Sammlung</p>
        </div>
        <div class="nische" data-auf data-gruppe="1">
          <span class="nische__zahl"><span data-zaehlen="3">3</span></span>
          <p class="nische__was">Etagen Ausstellung im Barockbau</p>
        </div>
        <div class="nische" data-auf data-gruppe="2">
          <span class="nische__zahl"><span data-zaehlen="25">25</span><span class="nische__einheit">m²</span></span>
          <p class="nische__was">misst das Großdiorama der Völkerschlacht</p>
        </div>
        <div class="nische" data-auf data-gruppe="3">
          <span class="nische__zahl">1670</span>
          <p class="nische__was">erbaut — das älteste Gebäude in Dölitz</p>
        </div>
        <div class="nische" data-auf data-gruppe="4">
          <span class="nische__zahl">5<span class="nische__einheit">€</span></span>
          <p class="nische__was">Eintritt für Erwachsene, ermäßigt 3 €</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ENTDECKEN --------------------------------------------------------- -->
  <section class="abschnitt oeffnung" aria-labelledby="sammlung-titel">
    <div class="wrap zweispalt zweispalt--versatz">
      <div class="stapel-weit">
        <p class="schild" data-auf>Die Dauerausstellung</p>
        <h2 class="t-gross" id="sammlung-titel" data-w="16" data-auf>
          Geschichte in Miniatur, Vitrine für Vitrine.
        </h2>
        <p class="vorspann" data-auf>
          Das Zinnfigurenmuseum im Torhaus Dölitz gehört zu den größten Museen seiner Art
          in Europa. Auf drei Etagen erzählen kunstvoll bemalte Einzelfiguren und ganze
          Dioramen regionale und Weltgeschichte — vom alten Babylon über Ritter und die
          türkische Belagerung Wiens 1683 bis ins Rokoko.
        </p>
        <div class="karten" data-auf>
          <div class="karte">
            <h3 class="t-klein">Wie eine Zinnfigur entsteht</h3>
            <p>Ein eigener Raum zeigt den ganzen Weg: Idee, Zeichnung, Gravur, Guss,
              Bemalung und schließlich der Bau des Dioramas.</p>
          </div>
          <div class="karte">
            <h3 class="t-klein">Leipzig und Dölitz</h3>
            <p>Zwei Räume, mit Unterstützung der LEIPZIGSTIFTUNG neu konzipiert, widmen
              sich der Stadt und dem Dorf, das Goethe als Student gern besuchte.</p>
          </div>
        </div>
        <p data-auf>
          <a class="textlink" href="museum.html">Die Ausstellung im Einzelnen <span aria-hidden="true">→</span></a>
        </p>
      </div>

      <figure data-auf>
        %(bild_portal)s
        <figcaption>
          Das Tor mit dem Giebel im holländischen Barock. Andreas von Winckler ließ es
          1670 errichten. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.
        </figcaption>
      </figure>
    </div>
  </section>

  <!-- DAS GROSSDIORAMA -------------------------------------------------- -->
  <section class="abschnitt flaeche-dunkel" aria-labelledby="diorama-titel">
    <div class="wrap zweispalt zweispalt--kippen">
      <div class="stapel-weit">
        <p class="schild" data-auf>Das Glanzstück</p>
        <h2 class="nur-fuer-screenreader" id="diorama-titel">Das Großdiorama der Völkerschlacht</h2>
        <blockquote class="zitat" data-auf>
          25 Quadratmeter, viele tausend Figuren, ein einziger Tag.
          <span class="zitat__quelle">Das Großdiorama der Völkerschlacht</span>
        </blockquote>
        <p class="notiz" data-auf>
          Das größte Diorama des Hauses zählt 12.126 Figuren. Die Zahl ist genau bekannt,
          weil sie einmal gezählt wurden.
        </p>
      </div>
      <div class="stapel-weit">
        <p class="vorspann" data-auf>
          Es zeigt die Kampfhandlungen des 18. Oktober 1813 auf dem südlichen Schlachtfeld
          der Völkerschlacht bei Leipzig — rund um Dölitz, Probstheida und Holzhausen.
          Wer davor steht, sieht die Ortschaften, in denen er sich gerade befindet.
        </p>
        <p data-auf>
          Der Schwerpunkt der Dauerausstellung liegt auf der napoleonischen Epoche.
          Dazu kommen Dioramen zur Antike, zum Mittelalter und zum 18. Jahrhundert,
          und mehrmals im Jahr wechselnde Sonderausstellungen.
        </p>
        <p data-auf>
          <a class="textlink" href="museum.html#diorama">Mehr über das Großdiorama <span aria-hidden="true">→</span></a>
        </p>
      </div>
    </div>
  </section>

  <!-- 1813, HIER -------------------------------------------------------- -->
  <section class="abschnitt" aria-labelledby="jahr-titel">
    <div class="wrap">
      <p class="schild" data-auf>16. Oktober 1813</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="jahr-titel" data-w="14" data-auf>
          Der Schauplatz ist das Museum.
        </h2>
        <div class="stapel" data-auf>
          <p class="vorspann">
            Der ehemalige Herrensitz Dölitz war am 16. Oktober 1813 eines der Zentren
            der Völkerschlacht. Hier geriet der österreichische General von Merveldt in
            Gefangenschaft — Napoleon schickte ihn mit einem Angebot zur Waffenruhe zu
            den Verbündeten zurück. 26 Gebäude im Ort wurden zerstört.
          </p>
          <p class="notiz">
            Im Torbogen hängen bis heute zwei Gedenktafeln. Sie sind das Erste,
            was Sie sehen, bevor Sie das Museum betreten.
          </p>
        </div>
      </div>

      <div class="zweispalt mt-6">
        <figure data-auf data-gruppe="0">
          %(bild_tafel1)s
          <figcaption>
            „Zur Erinnerung an die ruhmvolle Erstürmung und Verteidigung dieses Herrensitzes
            am 16. Oktober 1813“ — Tafel im Torbogen. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.
          </figcaption>
        </figure>
        <figure data-auf data-gruppe="1">
          %(bild_tafel2)s
          <figcaption>
            Die zweite Tafel erinnert zweisprachig an Fürst Poniatowski und die
            8000 polnischen Soldaten des VIII. Korps. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.
          </figcaption>
        </figure>
      </div>

      <p class="mt-5" data-auf>
        <a class="textlink" href="geschichte.html">Die Geschichte von Dölitz und dem Torhaus <span aria-hidden="true">→</span></a>
      </p>
    </div>
  </section>

  <!-- JETZT IM HAUS ----------------------------------------------------- -->
  <section class="abschnitt flaeche-sand" aria-labelledby="jetzt-titel">
    <div class="wrap">
      <div class="zweispalt">
        <div class="stapel-weit">
          <p class="schild" data-auf>Jetzt im Haus</p>
          <h2 class="t-gross" id="jetzt-titel" data-w="13" data-auf>Historisches Tabletop</h2>
          <p class="vorspann" data-auf>
            Die Sonderausstellung läuft vom 4. April 2026 bis zum 31. März 2027.
            Sie ist im regulären Eintritt enthalten.
          </p>
          <p data-auf>
            <a class="textlink" href="museum.html#sonderausstellung">Zur Sonderausstellung <span aria-hidden="true">→</span></a>
          </p>
        </div>

        <div class="klebrig">
          <p class="schild" data-auf>Die nächsten Termine</p>
          <ul class="termine" data-auf>
            <li><div class="termin">
              <span class="termin__tag">16. Aug<small>2026 · 15.30 Uhr</small></span>
              <span class="termin__was">Kaffeekonzert: Schlager trifft Musical<span>Einlass 14.30 Uhr</span></span>
            </div></li>
            <li><div class="termin">
              <span class="termin__tag">29. Aug<small>2026 · 17–23 Uhr</small></span>
              <span class="termin__was">Lichterfest im agra-Park<span>Eintrittsfrei; im Museum ermäßigter Eintritt für alle</span></span>
              <span class="termin__marke">frei</span>
            </div></li>
            <li><div class="termin">
              <span class="termin__tag">24. Okt<small>2026 · ganztägig</small></span>
              <span class="termin__was">213. Jahrestag der Völkerschlacht<span>Historische Biwaks und Darstellungen, 24. und 25. Oktober</span></span>
            </div></li>
          </ul>
          <p class="mt-4" data-auf>
            <a class="textlink" href="veranstaltungen.html">Alle Termine 2026 <span aria-hidden="true">→</span></a>
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- PLANEN ------------------------------------------------------------ -->
  <section class="abschnitt" aria-labelledby="planen-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Ihr Besuch</p>
        <h2 class="t-gross" id="planen-titel" data-w="12" data-auf>Alles auf einen Blick.</h2>
        <dl class="tafel" data-auf>
          <div>
            <dt>Geöffnet</dt>
            <dd><b>Mittwoch, Samstag, Sonntag und feiertags, 10–17 Uhr</b>
              <small>Ganzjährig. Letzter Einlass 16.30 Uhr.</small></dd>
          </div>
          <div>
            <dt>Eintritt</dt>
            <dd>Erwachsene 5,00 € · ermäßigt 3,00 € · Familienkarte 14,00 €
              <small>Kinder unter 7 Jahren frei. Im Museum ist nur Barzahlung möglich.</small></dd>
          </div>
          <div>
            <dt>Führungen</dt>
            <dd>35,00 € pauschal, rund 60 Minuten
              <small>Drei Themen zur Wahl, auch außerhalb der Öffnungszeiten möglich.</small></dd>
          </div>
          <div>
            <dt>Adresse</dt>
            <dd>Helenenstraße 24, 04279 Leipzig
              <small>Straßenbahn 11 bis Leinestraße, etwa 400 m zu Fuß.</small></dd>
          </div>
          <div>
            <dt>Kontakt</dt>
            <dd><a class="textlink" href="tel:+493413389107">0341 3389107</a><br>
              <a class="textlink" href="mailto:info@torhaus-doelitz.eu">info@torhaus-doelitz.eu</a></dd>
          </div>
        </dl>
        <p data-auf>
          <a class="knopf" href="besuch.html">Zeiten, Preise und Anfahrt <span class="knopf__pfeil" aria-hidden="true">→</span></a>
        </p>
      </div>

      <div class="stapel-weit" data-auf>
        <figure>
          %(bild_allee)s
          <figcaption>
            Der Weg zum Haus führt durch den agra-Park. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.
          </figcaption>
        </figure>
        <p class="notiz">
          Bitte nicht auf den Rasenflächen links und rechts des Weges parken — das
          Ordnungsamt ist dort aktiv. Nutzen Sie den öffentlichen Straßenbereich.
        </p>
      </div>
    </div>
  </section>

  <!-- GETRAGEN VON ------------------------------------------------------ -->
  <section class="abschnitt abschnitt--eng flaeche-sand" aria-labelledby="traeger-titel">
    <div class="wrap zweispalt">
      <div>
        <p class="schild" data-auf>Wer das Haus trägt</p>
        <h2 class="t-mittel" id="traeger-titel" data-w="16" data-auf>
          Ein Verein, kein Konzern.
        </h2>
        <p class="mt-4" data-auf>
          Das Torhaus wird seit Juli 2014 vom Verband Jahrfeier Völkerschlacht b. Leipzig
          1813 e.&nbsp;V. betrieben — gemeinsam mit den Zinnfigurenfreunden Leipzig e.&nbsp;V.,
          gefördert vom Kulturamt der Stadt Leipzig. Ohne diese Zusammenarbeit gäbe es
          das Museum in dieser Form nicht.
        </p>
        <p data-auf>
          <a class="textlink" href="unterstuetzen.html">Patenschaften, Spenden, Shop <span aria-hidden="true">→</span></a>
        </p>
      </div>
      <ul class="verweise" data-auf>
        <li><a href="https://www.leipzig1813.com/" rel="noopener">
          <span class="verweise__name">Verband Jahrfeier 1813</span>
          <span class="verweise__was">Betreiberverein</span></a></li>
        <li><a href="https://www.zinnfigurenfreunde-leipzig.de/" rel="noopener">
          <span class="verweise__name">Zinnfigurenfreunde Leipzig</span>
          <span class="verweise__was">Ausstellungen und Sammlung</span></a></li>
        <li><a href="https://www.bv-doelitz-online.de/" rel="noopener">
          <span class="verweise__name">Bürgerverein Dölitz</span>
          <span class="verweise__was">Stadtteilarbeit und Projekte</span></a></li>
        <li><a href="https://agra-park.info/" rel="noopener">
          <span class="verweise__name">agra-Park</span>
          <span class="verweise__was">50 Hektar vor der Tür</span></a></li>
      </ul>
    </div>
  </section>
""" % {
        "bild_portal": bild(
            "portal-bruecke",
            u"Der Barockgiebel über dem Tor des Torhauses Dölitz, mit Säulen, Voluten und liegenden Figuren im Relief.",
            1920, 2560, "(min-width:900px) 40vw, 92vw",
            klasse="bogen bogen--quader", verhaeltnis="3/4"),
        "bild_tafel1": bild(
            "tafel-1813",
            u"Gedenktafel aus rotem Marmor mit goldener Schrift zur Erstürmung und Verteidigung des Herrensitzes am 16. Oktober 1813.",
            1920, 1440, "(min-width:900px) 55vw, 92vw", klasse="tafelbild"),
        "bild_tafel2": bild(
            "tafel-poniatowski",
            u"Zweisprachige Gedenktafel in Deutsch und Polnisch für Fürst Poniatowski und die 8000 polnischen Soldaten des VIII. Korps.",
            1920, 1440, "(min-width:900px) 38vw, 92vw", klasse="tafelbild"),
        "bild_allee": bild(
            "allee",
            u"Ein Weg durch alte Bäume im agra-Park, an dessen Ende der weiße Torbogen des Torhauses zu sehen ist.",
            1920, 1440, "(min-width:900px) 40vw, 92vw"),
    }

    raus.append(seite(
        "index.html",
        u"Torhaus Dölitz — Zinnfigurenmuseum in Leipzig",
        u"Im Torhaus Dölitz, einem Barockbau von 1670 am agra-Park in Leipzig, zeigen über "
        u"100.000 Zinnfiguren auf drei Etagen Geschichte in Miniatur — darunter ein 25 m² "
        u"großes Diorama der Völkerschlacht bei Leipzig 1813.",
        start, aktiv=None))

    # =======================================================================
    # BESUCH PLANEN
    # =======================================================================

    besuch = kopfbild(
        "torhaus-frontal",
        u"Das Torhaus Dölitz von der Hofseite: weiße Fassade, roter Ziegelwalm, der offene Torbogen in der Mitte.",
        u"Alles, was Sie vorher wissen müssen.",
        u"Besuch planen",
        u"Öffnungszeiten, Eintritt, Führungen und der Weg hierher — auf einer Seite.",
        1920, 1280,
    ) + u"""
  <section class="abschnitt" aria-labelledby="zeiten-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Öffnungszeiten</p>
        <h2 class="t-gross" id="zeiten-titel" data-w="13" data-auf>
          Mittwoch, Samstag, Sonntag.
        </h2>
        <dl class="tafel" data-auf>
          <div>
            <dt>Ganzjährig</dt>
            <dd><b>Mittwoch, Samstag, Sonntag und feiertags, 10–17 Uhr</b>
              <small>Letzter Einlass 16.30 Uhr.</small></dd>
          </div>
          <div>
            <dt>Zusätzlich 2026</dt>
            <dd>Freitag, 15. Mai 2026, 10–17 Uhr</dd>
          </div>
          <div>
            <dt>22.–25. Mai 2026</dt>
            <dd>Zugang nur mit einer Eintrittskarte zum Heidnischen Dorf
              <small>Im Rahmen des Wave-Gotik-Treffens.</small></dd>
          </div>
          <div>
            <dt>Jahreswechsel</dt>
            <dd>Geschlossen vom 24. Dezember 2026 bis 1. Januar 2027
              <small>Gruppenanfragen sind auch in dieser Zeit möglich. Erster regulärer
                Öffnungstag 2027: Freitag, 2. Januar.</small></dd>
          </div>
        </dl>
      </div>

      <div class="stapel-weit klebrig" data-auf>
        <p class="schild schild--blank" style="color:var(--ziegel)">Kurz und wichtig</p>
        <dl class="tafel">
          <div>
            <dt>Zahlung</dt>
            <dd><b>Nur Barzahlung</b><small>Im Museum ist keine Kartenzahlung möglich.</small></dd>
          </div>
          <div>
            <dt>Garderobe</dt>
            <dd>Spinde für Jacken und Taschen stehen bereit.</dd>
          </div>
          <div>
            <dt>Anschrift</dt>
            <dd>Helenenstraße 24<br>04279 Leipzig</dd>
          </div>
          <div>
            <dt>Telefon</dt>
            <dd><a class="textlink" href="tel:+493413389107">0341 3389107</a></dd>
          </div>
          <div>
            <dt>E-Mail</dt>
            <dd><a class="textlink" href="mailto:info@torhaus-doelitz.eu">info@torhaus-doelitz.eu</a></dd>
          </div>
        </dl>
      </div>
    </div>
  </section>

  <section class="abschnitt flaeche-sand" aria-labelledby="preise-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Eintritt</p>
        <h2 class="t-gross" id="preise-titel" data-w="12" data-auf>Was es kostet.</h2>
        <ul class="preise" data-auf>
          <li>
            <span class="preise__was">Erwachsene<small>Gruppen ab 10 Personen: 4,00 €</small></span>
            <span class="preise__punkte" aria-hidden="true"></span>
            <span class="preise__wert">5,00 €</span>
          </li>
          <li>
            <span class="preise__was">Ermäßigt<small>Gruppen ab 10 Personen: 2,50 €</small></span>
            <span class="preise__punkte" aria-hidden="true"></span>
            <span class="preise__wert">3,00 €</span>
          </li>
          <li>
            <span class="preise__was">Familienkarte<small>Zwei Erwachsene und bis zu zwei Kinder</small></span>
            <span class="preise__punkte" aria-hidden="true"></span>
            <span class="preise__wert">14,00 €</span>
          </li>
          <li>
            <span class="preise__was">Kinder unter 7 Jahren</span>
            <span class="preise__punkte" aria-hidden="true"></span>
            <span class="preise__wert">frei</span>
          </li>
          <li>
            <span class="preise__was">Führung<small>Pauschal, unabhängig von der Gruppengröße</small></span>
            <span class="preise__punkte" aria-hidden="true"></span>
            <span class="preise__wert">35,00 €</span>
          </li>
        </ul>
        <p class="notiz mt-4" data-auf>
          Ermäßigt gilt für Kinder ab 7 Jahren, Schülerinnen und Schüler, Auszubildende,
          Studierende, Menschen mit Behinderung und Leipzig-Pass-Inhaber. Ist im
          Behindertenausweis ein „B“ vermerkt, hat die Begleitperson freien Eintritt.
        </p>
      </div>

      <div class="stapel-weit" data-auf>
        <p class="schild">Rabatte</p>
        <dl class="tafel">
          <div>
            <dt>Leipzig Regio Card</dt>
            <dd>0,50 € Rabatt auf den regulären Eintrittspreis</dd>
          </div>
          <div>
            <dt>Konsum-KUSS-Gutschein</dt>
            <dd>10 %% auf den regulären Eintrittspreis
              <small>Zusätzlich 5 € Rabatt auf die Führungspauschale.</small></dd>
          </div>
        </dl>
        <p class="schild mt-6">Nur für Gruppen, auf Vorbestellung</p>
        <dl class="tafel">
          <div>
            <dt>Kaffee und Kuchen</dt>
            <dd>Ein Stück Kuchen und „Kaffee satt“ für 6,00 € pro Person, zwei Stück für 8,00 €
              <small>Serviert im Gewölbe, alternativ auch in der Ausstellung. Zur Wahl:
                Apfelkuchen mit Streusel, Streuselkuchen, gefüllter Bienenstich,
                Mohnkuchen — auch als gemischter Kuchenteller.</small></dd>
          </div>
        </dl>
      </div>
    </div>
  </section>

  <section class="abschnitt" aria-labelledby="fuehrungen-titel">
    <div class="wrap">
      <p class="schild" data-auf>Führungen</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="fuehrungen-titel" data-w="15" data-auf>
          Drei Wege durch das Haus.
        </h2>
        <p class="vorspann" data-auf>
          Alle Führungen sind auf 60 Minuten angelegt und lassen sich nach Ihren
          Wünschen anpassen. Bitte wählen Sie bei der Bestellung ein Thema.
          Führungen sind auch außerhalb der Öffnungszeiten möglich.
        </p>
      </div>
      <div class="karten mt-6">
        <div class="karte" data-auf data-gruppe="0">
          <h3 class="t-klein">Allgemeine Museumsführung</h3>
          <p>Alle Ausstellungsbereiche des Museums, schlaglichtartig beleuchtet.</p>
        </div>
        <div class="karte" data-auf data-gruppe="1">
          <h3 class="t-klein">Geschichte und Herstellung der Zinnfigur</h3>
          <p>Die Spezialführung zum Handwerk: von der Gravur über den Guss bis zur Bemalung.</p>
        </div>
        <div class="karte" data-auf data-gruppe="2">
          <h3 class="t-klein">Völkerschlacht und Napoleon</h3>
          <p>Die Erlebnisführung zur Völkerschlacht bei Leipzig und zum Zeitalter Napoleons —
            an dem Ort, an dem am 16. Oktober 1813 gekämpft wurde.</p>
        </div>
        <div class="karte" data-auf data-gruppe="3">
          <h3 class="t-klein">Anmeldung</h3>
          <p>Telefonisch unter <a class="textlink" href="tel:+493413389107">0341 3389107</a>
            oder per <a class="textlink" href="mailto:info@torhaus-doelitz.eu">E-Mail</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="abschnitt flaeche-dunkel" aria-labelledby="anreise-titel">
    <div class="wrap zweispalt zweispalt--kippen">
      <div class="stapel-weit">
        <p class="schild" data-auf>Lage und Anreise</p>
        <h2 class="t-gross" id="anreise-titel" data-w="14" data-auf>
          An der südlichen Stadtgrenze.
        </h2>
        <p class="vorspann" data-auf>
          Das Torhaus Dölitz ist ein direkter Zugang zum rund 50 Hektar großen agra-Park
          zwischen Leipzig und Markkleeberg. Wer den Park in Richtung Markkleeberg
          verlässt, steht im Leipziger Neuseenland.
        </p>
        <p class="notiz" data-auf>
          Bitte parken Sie nicht auf den Rasenflächen links und rechts des Weges vor
          dem Torhaus — dort wird ein Bußgeld von 35 € erhoben. Nutzen Sie den
          öffentlichen Straßenbereich.
        </p>
      </div>

      <div class="stapel-weit" data-auf>
        <dl class="tafel">
          <div>
            <dt>Straßenbahn</dt>
            <dd><b>Linie 11 bis Leinestraße</b>
              <small>Etwa 400 m Fußweg bis zum Torhaus.</small></dd>
          </div>
          <div>
            <dt>Bus</dt>
            <dd>Linie 79 bis Raschwitzer Straße, dann zwei Haltestellen mit der Linie 11
              bis Leinestraße</dd>
          </div>
          <div>
            <dt>Mit dem Auto</dt>
            <dd>Von der A 38 über die B 2, Abfahrt Goethesteig</dd>
          </div>
          <div>
            <dt>Fahrplan</dt>
            <dd><a class="textlink" href="https://www.l.de/verkehrsbetriebe" rel="noopener">Leipziger Verkehrsbetriebe <span aria-hidden="true">↗</span></a></dd>
          </div>
        </dl>
        <p class="mt-4" data-auf>
          <a class="knopf knopf--hell" href="https://www.openstreetmap.org/?mlat=51.2896&amp;mlon=12.3830#map=17/51.2896/12.3830" rel="noopener">
            Auf der Karte ansehen <span class="knopf__pfeil" aria-hidden="true">↗</span></a>
        </p>
      </div>
    </div>
  </section>

  <section class="abschnitt" aria-labelledby="barriere-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Barrierefreiheit vor Ort</p>
        <h2 class="t-mittel" id="barriere-titel" data-w="18" data-auf>
          Fragen Sie uns vorher — wir sagen Ihnen ehrlich, was geht.
        </h2>
        <p data-auf>
          Das Torhaus ist ein Barockbau von 1670 mit einer Ausstellung auf drei Etagen.
          Zu den baulichen Gegebenheiten im Einzelnen liegen uns keine geprüften Angaben
          vor, die wir hier veröffentlichen könnten. Rufen Sie bitte vor Ihrem Besuch an
          — dann klären wir gemeinsam, was für Sie möglich ist.
        </p>
        <p data-auf>
          <a class="knopf" href="tel:+493413389107">0341 3389107 anrufen <span class="knopf__pfeil" aria-hidden="true">→</span></a>
        </p>
      </div>
      <div class="stapel-weit" data-auf>
        %(bild_apel)s
        <p class="notiz">
          Vor dem Eingang stehen zwei Apelsteine — die Markierungssteine, die seit 1863
          an die Stellungen der Völkerschlacht erinnern. Nummer 33 und 46 gehören zum
          Torhaus.
        </p>
      </div>
    </div>
  </section>

  <section class="abschnitt abschnitt--eng flaeche-sand">
    <div class="wrap zweispalt">
      <div>
        <p class="schild" data-auf>In der Nachbarschaft</p>
        <h2 class="t-mittel" data-w="16" data-auf>Wenn Sie schon da sind.</h2>
      </div>
      <ul class="verweise" data-auf>
        <li><a href="https://agra-park.info/" rel="noopener">
          <span class="verweise__name">agra-Park</span>
          <span class="verweise__was">Landschaftspark, rund 50 Hektar, direkt vor dem Tor</span></a></li>
        <li><a href="https://www.doelitzer-wassermuehle.de/" rel="noopener">
          <span class="verweise__name">Dölitzer Wassermühle</span>
          <span class="verweise__was">Die letzte erhaltene Wassermühle Leipzigs</span></a></li>
        <li><a href="https://www.fotomuseum.eu/" rel="noopener">
          <span class="verweise__name">Deutsches Fotomuseum</span>
          <span class="verweise__was">Markkleeberg, Raschwitzer Straße 11–13</span></a></li>
        <li><a href="https://leipziger-neuseenland.org/" rel="noopener">
          <span class="verweise__name">Leipziger Neuseenland</span>
          <span class="verweise__was">Markkleeberger, Störmthaler und Cospudener See</span></a></li>
      </ul>
    </div>
  </section>
""" % {
        "bild_apel": bild(
            "apelsteine",
            u"Zwei alte Steinstelen mit abgerundeten Köpfen auf dem Pflaster vor dem Torhaus, daneben Holzbänke und eine Infotafel.",
            1920, 1440, "(min-width:900px) 40vw, 92vw"),
    }

    raus.append(seite(
        "besuch.html",
        u"Besuch planen — Torhaus Dölitz",
        u"Öffnungszeiten, Eintrittspreise, Führungen und Anfahrt zum Zinnfigurenmuseum "
        u"im Torhaus Dölitz, Helenenstraße 24 in Leipzig.",
        besuch, aktiv="besuch.html",
        schwebeziel="tel:+493413389107", schwebetext="0341 3389107"))

    # =======================================================================
    # AUSSTELLUNG
    # =======================================================================

    museum = kopfbild(
        "tor-parkseite",
        u"Blick von der Parkseite auf das Torhaus Dölitz: ein Kiesweg führt auf den offenen Torbogen zu.",
        u"Über 100.000 Zinnfiguren.",
        u"Die Ausstellung",
        u"Drei Etagen in einem Barockbau von 1670 — Dauerausstellung, wechselnde "
        u"Sonderausstellungen und das größte Stück des Hauses.",
    ) + u"""
  <section class="abschnitt" aria-labelledby="dauer-titel">
    <div class="wrap">
      <p class="schild" data-auf>Dauerausstellung</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="dauer-titel" data-w="15" data-auf>
          Geschichte in Miniatur.
        </h2>
        <div class="stapel" data-auf>
          <p class="vorspann">
            Das Zinnfigurenmuseum im Torhaus Dölitz gehört zu den größten Museen seiner
            Art in Europa. Auf drei Etagen zeigen kunstvoll gestaltete Einzelfiguren und
            ganze Zinnfigurendioramen regionale und Weltgeschichte. Insgesamt warten
            über 100.000 Zinnfiguren auf ihre Entdeckung.
          </p>
          <p class="notiz">
            Das Torhaus selbst ist über 300 Jahre alt und zählt zu den wenigen
            erhaltenen barocken Gebäuden Leipzigs.
          </p>
        </div>
      </div>

      <div class="karten mt-6">
        <div class="karte" data-auf data-gruppe="0">
          <h3 class="t-klein">Die napoleonische Epoche</h3>
          <p>Der Schwerpunkt der Ausstellung. Die Völkerschlacht bei Leipzig 1813 wird
            hier nicht nur erzählt — sie hat auf diesem Grundstück stattgefunden.</p>
        </div>
        <div class="karte" data-auf data-gruppe="1">
          <h3 class="t-klein">Antike, Mittelalter, Rokoko</h3>
          <p>Dioramen zu Babylon, zu Rittern, zur türkischen Belagerung Wiens 1683
            sowie zu Ereignissen des 18. Jahrhunderts.</p>
        </div>
        <div class="karte" data-auf data-gruppe="2">
          <h3 class="t-klein">Die Zinnfigur selbst</h3>
          <p>Ein eigener Ausstellungsraum zeigt Geschichte und Herstellung: von der Idee
            und der Zeichnung über die Gravur zum Guss, zur Bemalung und zum Dioramenbau.</p>
        </div>
        <div class="karte" data-auf data-gruppe="3">
          <h3 class="t-klein">Leipzig und Dölitz</h3>
          <p>Zwei Räume, mit Unterstützung der LEIPZIGSTIFTUNG neu konzipiert, zeigen,
            wie sich das Stadtbild über die Jahrhunderte verändert hat. Der Dölitz-Raum
            entstand mit Leihgaben und dem Detailwissen des Bürgervereins Dölitz e.&nbsp;V.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="abschnitt flaeche-dunkel" id="diorama" aria-labelledby="gross-titel">
    <div class="wrap">
      <p class="schild" data-auf>Das Glanzstück</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="gross-titel" data-w="13" data-auf>
          Das Großdiorama der Völkerschlacht.
        </h2>
        <div class="stapel" data-auf>
          <p class="vorspann">
            Rund 25 Quadratmeter groß, mit vielen tausend Figuren. Es zeigt die
            Kampfhandlungen des 18. Oktober 1813 auf dem südlichen Schlachtfeld der
            Völkerschlacht bei Leipzig — rund um die Ortschaften Dölitz, Probstheida
            und Holzhausen.
          </p>
          <p class="notiz">
            Das größte Diorama des Hauses zählt 12.126 Figuren.
          </p>
        </div>
      </div>
      <div class="zahlen zahlen--drei zahlen--wenig mt-6">
        <div class="nische" data-auf data-gruppe="0">
          <span class="nische__zahl"><span data-zaehlen="25">25</span><span class="nische__einheit">m²</span></span>
          <p class="nische__was">Fläche des Großdioramas</p>
        </div>
        <div class="nische" data-auf data-gruppe="1">
          <span class="nische__zahl"><span data-zaehlen="12126">12.126</span></span>
          <p class="nische__was">Figuren im größten Diorama des Hauses</p>
        </div>
        <div class="nische" data-auf data-gruppe="2">
          <span class="nische__zahl">18.10.</span>
          <p class="nische__was">der dargestellte Tag im Jahr 1813</p>
        </div>
      </div>
    </div>
  </section>

  <section class="abschnitt" id="sonderausstellung" aria-labelledby="sonder-titel">
    <div class="wrap zweispalt zweispalt--versatz">
      <div class="stapel-weit">
        <p class="schild" data-auf>Sonderausstellung</p>
        <h2 class="t-gross" id="sonder-titel" data-w="13" data-auf>Historisches Tabletop</h2>
        <p class="vorspann" data-auf>
          4. April 2026 bis 31. März 2027. Im regulären Eintritt enthalten.
        </p>
        <p data-auf>
          Alle Sonderausstellungen entstehen in enger Zusammenarbeit mit den
          Zinnfigurenfreunden Leipzig e.&nbsp;V. Dasselbe gilt für die schrittweise
          Modernisierung der Dauerausstellung.
        </p>
        <p data-auf>
          <a class="textlink" href="https://www.zinnfigurenfreunde-leipzig.de/" rel="noopener">
            Zinnfigurenfreunde Leipzig e.&nbsp;V. <span aria-hidden="true">↗</span></a>
        </p>
      </div>
      <figure data-auf>
        %(bild_wiese)s
        <figcaption>
          Das Torhaus von der Wiesenseite. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.
        </figcaption>
      </figure>
    </div>
  </section>

  <section class="abschnitt flaeche-sand" aria-labelledby="frueher-titel">
    <div class="wrap">
      <p class="schild" data-auf>Was hier schon zu sehen war</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="frueher-titel" data-w="14" data-auf>
          Ein Haus, das sich ständig neu sortiert.
        </h2>
        <p class="vorspann" data-auf>
          Seit der Wiedereröffnung 2014 hat das Museum in jedem Jahr mindestens eine
          neue Sonderausstellung gezeigt. Eine Auswahl:
        </p>
      </div>
      <ul class="termine mt-6" data-auf>
        <li><div class="termin">
          <span class="termin__tag">2025/26<small>6. Apr 2025 – 28. Feb 2026</small></span>
          <span class="termin__was">Steffen Jahn — Sammler, Maler und Graveur<span>Zeitgleich: Dioramen und Zinnfiguren aus dem Fundus des Kulturamtes der Stadt Leipzig</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2024/25<small>1. Apr 2024 – 4. Feb 2025</small></span>
          <span class="termin__was">„Es gibt nicht nur Nussknacker und Engel — Geschichte und Geschichten in Zinn“<span>Die KLIO-Landesgruppe Südwest-Sachsen stellt sich vor</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2023/24<small>3. Jun 2023 – 25. Feb 2024</small></span>
          <span class="termin__was">Die Feld-Artillerie der Napoleonischen Kriege<span>Zum 210. Jahrestag der Völkerschlacht. Napoleon selbst war ausgebildeter Artillerie-Offizier.</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2023<small>16. Jul – 11. Okt 2023</small></span>
          <span class="termin__was">Eine Reise nach Aventurien<span>Das Fantasy-Rollenspiel „Das Schwarze Auge“ — die Sammlung Manfred Sebon</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2022/23<small>8. Mai 2022 – 26. Feb 2023</small></span>
          <span class="termin__was">SHOGUN packt aus<span>Die KLIO-Arbeitsgruppe SHOGUN zeigt flache und plastische Figuren, Serien und Dioramen zum alten Japan — vom Bauern über die Samurai bis zum Kaiserhof</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2021/22<small>15. Mai 2021 – 18. Apr 2022</small></span>
          <span class="termin__was">Ulanen, Turkos, Mitrailleusen<span>Eine Zinnfiguren-Zeitreise ins Jahr 1870/71</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2019/20<small>1. Mai 2019 – 29. Feb 2020</small></span>
          <span class="termin__was">Napoleon-Gesichter<span>Kuriositäten, die den Kaiser abbilden, glorifizieren, denunzieren und benutzen</span></span>
        </div></li>
        <li><div class="termin">
          <span class="termin__tag">2018/19<small>2. Jun 2018 – 28. Feb 2019</small></span>
          <span class="termin__was">„Streit um Glauben und Macht“<span>Das Heerwesen im Dreißigjährigen Krieg, zum 400. Jahrestag seines Beginns</span></span>
        </div></li>
      </ul>
    </div>
  </section>

  <section class="abschnitt" aria-labelledby="dunkel-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Nur online</p>
        <h2 class="t-mittel" id="dunkel-titel" data-w="17" data-auf>
          Dioramen aus der Dunkelkammer.
        </h2>
        <p data-auf>
          Während der Schließzeiten 2020 und 2021 hat das Museum Stücke aus dem eigenen
          Magazin gezeigt, die nicht Teil der Dauerausstellung sind — manche davon sind
          höchstens einmal in zehn Jahren in einer Sonderausstellung zu sehen.
        </p>
        <p data-auf>
          <a class="textlink" href="http://www.torhaus-doelitz.eu/dunkelkammer/" rel="noopener">
            Die Sammlungsstücke ansehen <span aria-hidden="true">↗</span></a>
        </p>
      </div>
      <div data-auf>
        <p class="schild">Aus derselben Familie</p>
        <ul class="verweise">
          <li><a href="http://www.sanitaetsmuseum1813.de/" rel="noopener">
            <span class="verweise__name">Sanitäts- und Lazarettmuseum</span>
            <span class="verweise__was">Seifertshain</span></a></li>
          <li><a href="http://www.koernerhaus-leipzig.de/" rel="noopener">
            <span class="verweise__name">Körnerhaus</span>
            <span class="verweise__was">Leipzig-Großzschocher</span></a></li>
          <li><a href="https://www.torhaus-markkleeberg.de/" rel="noopener">
            <span class="verweise__name">Regionalmuseum Torhaus</span>
            <span class="verweise__was">Markkleeberg</span></a></li>
          <li><a href="https://www.stiftung-voelkerschlachtdenkmal-leipzig.de/" rel="noopener">
            <span class="verweise__name">Völkerschlachtdenkmal</span>
            <span class="verweise__was">Stiftung, Leipzig</span></a></li>
        </ul>
        <p class="notiz mt-4">
          Die ersten vier Häuser bilden gemeinsam den Museumsverbund 1813.
        </p>
      </div>
    </div>
  </section>
""" % {
        "bild_wiese": bild(
            "torhaus-wiese",
            u"Das Torhaus Dölitz zwischen alten Pappeln, davor eine Wiese im Sommerlicht.",
            1920, 1440, "(min-width:900px) 40vw, 92vw"),
    }

    raus.append(seite(
        "museum.html",
        u"Die Ausstellung — Torhaus Dölitz",
        u"Dauerausstellung, Großdiorama der Völkerschlacht und Sonderausstellungen im "
        u"Zinnfigurenmuseum Torhaus Dölitz: über 100.000 Zinnfiguren auf drei Etagen.",
        museum, aktiv="museum.html"))

    # =======================================================================
    # GESCHICHTE
    # =======================================================================

    zeitleiste = [
        ("seit dem 7. Jahrhundert", False,
         u"Altsorben besiedeln das Leipziger Land und gründen unter anderem den Ort Dölitz. "
         u"Der Name geht auf das altsorbische <i>dolec</i> zurück und bedeutet so viel wie "
         u"„Ort im Tal“."),
        ("ab 1125", False,
         u"Deutsche Bauern, vor allem Flamen, erschließen das Gebiet weiter. Im westlichen "
         u"und nördlichen Teil der heutigen Helenenstraße entsteht ein Gassendorf."),
        ("1262", False,
         u"Ein Johannes von Doluz wird erwähnt — ein Hinweis darauf, dass bereits im "
         u"13. Jahrhundert ein deutscher Herrensitz in Dölitz bestand."),
        ("1348/49", False,
         u"Dölitz wird im Lehnsbuch des Markgrafen Friedrich des Strengen erstmals "
         u"urkundlich erwähnt."),
        ("1636", False,
         u"Christoph von Crostewitz verkauft Schloss und Rittergut an den Leipziger Kaufmann "
         u"Georg Winckler, der das Renaissanceschloss bis 1640 umbauen lässt."),
        ("1670", True,
         u"Andreas von Winckler lässt das Torhaus des Schlosses im Stil des holländischen "
         u"Barock errichten. Es ist heute das älteste Bauwerk in Dölitz."),
        ("1760–71", False,
         u"Rosine Elisabeth Oeser lässt in Dölitz das Oeser-Haus errichten. Ihr Mann, "
         u"Adam Oeser, Direktor der Leipziger Malakademie, gibt hier zwischen 1766 und 1768 "
         u"dem Studenten Johann Wolfgang Goethe Zeichenunterricht."),
        ("1813", True,
         u"Der ehemalige Herrensitz Dölitz ist am 16. Oktober eines der Zentren der "
         u"Völkerschlacht. Hier gerät der österreichische General von Merveldt in "
         u"Gefangenschaft; Napoleon schickt ihn mit einem Angebot zur Waffenruhe zu den "
         u"Verbündeten zurück. Neben der Mühle werden 26 Gebäude im Ort zerstört."),
        ("1839", False,
         u"Dölitz wird eine selbstständige Gemeinde und damit formal unabhängig vom "
         u"Rittergutsbesitzer."),
        ("1894/95", False,
         u"Nach Probebohrungen beginnt man, auf der Dölitzer Flur einen Braunkohleschacht "
         u"anzulegen."),
        ("um 1900", False,
         u"In Dölitz gibt es acht Gasthäuser. Einige, wie der alte Dorfkretscham „Zum Reiter“ "
         u"und der „Park Dölitz“, sind stadtbekannte Ausflugslokale der Leipziger."),
        ("1910", False,
         u"Dölitz wird nach Leipzig eingemeindet. Mehrere Straßen werden umbenannt — aus der "
         u"Wassergasse wird die Helenenstraße."),
        ("1927", False,
         u"Die Erben der Familie Winckler verkaufen Schloss und Rittergut an die Stadt Leipzig."),
        ("1944–45", False,
         u"Dölitz bleibt von großflächiger Zerstörung verschont, verliert aber Gebäude durch "
         u"Brandbomben und Luftminen. Das Oeser-Haus wird zerstört, das Schloss schwer "
         u"beschädigt."),
        ("1947", False, u"Die Reste des Schlossgebäudes werden gesprengt. Das Torhaus bleibt stehen."),
        ("1960", True,
         u"Im Torhaus des Dölitzer Schlosses wird eine ständige Zinnfigurenausstellung "
         u"eröffnet — der Beginn des Museums."),
        ("1989", False,
         u"Die letzte Landwirtschaftsausstellung der DDR findet auf dem heutigen "
         u"agra-Gelände statt."),
        ("2014", True,
         u"Seit Juli betreibt der Verband Jahrfeier Völkerschlacht b. Leipzig 1813 "
         u"e.&nbsp;V. das Torhaus — gemeinsam mit den Zinnfigurenfreunden Leipzig e.&nbsp;V."),
        ("heute", False,
         u"Dölitz bildet gemeinsam mit Dösen einen Leipziger Ortsteil im Stadtbezirk Süd."),
    ]

    zeilen = []
    for jahr, stark, text in zeitleiste:
        zeilen.append(
            u'        <li%s data-auf>\n'
            u'          <div><span class="leiste__jahr">%s</span></div>\n'
            u'          <div><p>%s</p></div>\n'
            u'        </li>' % (' data-stark="true"' if stark else "", jahr, text)
        )

    geschichte = kopfbild(
        "muehlpleisse",
        u"Das Torhaus Dölitz von der Mühlpleiße aus: die Brücke führt auf den Torbogen zu, darüber der barocke Giebel.",
        u"Vom Rittergut zum Museum.",
        u"Geschichte",
        u"Dölitz ist älter als die Stadt, zu der es gehört. Eine Zeitleiste — von den "
        u"Altsorben bis heute.",
        1920, 2560, fokus="50% 24%",
    ) + u"""
  <section class="abschnitt" aria-labelledby="leiste-titel">
    <div class="wrap">
      <p class="schild" data-auf>Zeitleiste</p>
      <h2 class="t-gross" id="leiste-titel" data-w="16" data-auf>
        Was auf diesem Grundstück geschah.
      </h2>
      <ul class="leiste mt-6">
%(zeilen)s
      </ul>
      <p class="notiz mt-5" data-auf>
        Mehr zur Geschichte von Ort und Gut Dölitz erfahren Sie in der Dauerausstellung.
      </p>
    </div>
  </section>

  <section class="abschnitt flaeche-dunkel" aria-labelledby="tafeln-titel">
    <div class="wrap">
      <p class="schild" data-auf>Im Torbogen</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="tafeln-titel" data-w="13" data-auf>
          Zwei Tafeln, zwei Erinnerungen.
        </h2>
        <p class="vorspann" data-auf>
          Wer durch das Tor geht, kommt an ihnen vorbei. Die eine erinnert an die
          Erstürmung und Verteidigung des Herrensitzes am 16. Oktober 1813 und an
          Oberst Samuel von Reissenfels, der hier fiel. Die andere, in Deutsch und
          Polnisch, an Fürst Poniatowski und die 8000 polnischen Soldaten des
          VIII. Korps.
        </p>
      </div>
      <div class="zweispalt mt-6">
        <figure data-auf data-gruppe="0">
          %(bild_t1)s
          <figcaption>Gedenktafel im Torbogen. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.</figcaption>
        </figure>
        <figure data-auf data-gruppe="1">
          %(bild_t2)s
          <figcaption>Die polnisch-deutsche Tafel. Foto: Bybbisch94, CC&nbsp;BY&nbsp;4.0.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="abschnitt flaeche-sand" aria-labelledby="umgebung-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Ringsum</p>
        <h2 class="t-mittel" id="umgebung-titel" data-w="16" data-auf>
          Der Stadtteil gehört dazu.
        </h2>
        <p data-auf>
          Das Torhaus ist ein Eingang in den über 50 Hektar großen agra-Park, der den
          historischen Herfurthschen Landschaftspark, das Dölitzer Holz und den
          ehemaligen Schlossgarten umfasst. Seine Geschichte beginnt um 1890.
        </p>
        <p data-auf>
          Eines der bedeutendsten historischen Gebäude von Dölitz ist die Wassermühle —
          die letzte erhaltene Wassermühle Leipzigs. In den Kämpfen der Völkerschlacht
          1813 abgebrannt, wurde sie schon 1814 wieder aufgebaut.
        </p>
        <p data-auf>
          2023 wurde am Ufer der Mühlpleiße der Verweilort „Mühlenblick“ eingeweiht;
          entlang des Ufers verläuft ein 1986 angelegter und 2022 erneuerter
          Vogellehrpfad mit rund 100 Nistkästen, die Kinder beim Torhausfest gebaut haben.
        </p>
      </div>
      <ul class="verweise" data-auf>
        <li><a href="https://agra-park.info/" rel="noopener">
          <span class="verweise__name">agra-Park</span>
          <span class="verweise__was">Geschichte, Angebote, Veranstaltungen</span></a></li>
        <li><a href="https://www.doelitzer-wassermuehle.de/" rel="noopener">
          <span class="verweise__name">Dölitzer Wassermühle</span>
          <span class="verweise__was">Grün-Alternatives Zentrum Leipzig e.&nbsp;V.</span></a></li>
        <li><a href="https://www.bv-doelitz-online.de/" rel="noopener">
          <span class="verweise__name">Bürgerverein Dölitz e.&nbsp;V.</span>
          <span class="verweise__was">Stadtteilarbeit, Dölitz-Flyer</span></a></li>
        <li><a href="https://www.leipzig.de/kultur-und-freizeit/sehenswuerdigkeiten/torhaus-doelitz" rel="noopener">
          <span class="verweise__name">Stadt Leipzig über das Torhaus</span>
          <span class="verweise__was">leipzig.de</span></a></li>
      </ul>
    </div>
  </section>
""" % {
        "zeilen": "\n".join(zeilen),
        "bild_t1": bild(
            "tafel-1813",
            u"Gedenktafel aus rotem Marmor mit goldener Schrift zur Erstürmung und Verteidigung des Herrensitzes am 16. Oktober 1813.",
            1920, 1440, "(min-width:900px) 55vw, 92vw", klasse="tafelbild"),
        "bild_t2": bild(
            "tafel-poniatowski",
            u"Zweisprachige Gedenktafel in Deutsch und Polnisch für Fürst Poniatowski und die 8000 polnischen Soldaten des VIII. Korps.",
            1920, 1440, "(min-width:900px) 38vw, 92vw", klasse="tafelbild"),
    }

    raus.append(seite(
        "geschichte.html",
        u"Geschichte — Torhaus Dölitz",
        u"Von den Altsorben über das Rittergut und die Völkerschlacht 1813 bis zum "
        u"Zinnfigurenmuseum: die Geschichte von Dölitz und dem Torhaus in einer Zeitleiste.",
        geschichte, aktiv="geschichte.html"))

    # =======================================================================
    # VERANSTALTUNGEN
    # =======================================================================

    termine = [
        (u"16. Aug", u"2026 · 15.30 Uhr",
         u"Kaffeekonzert am Torhaus: Schlager trifft Musical",
         u"Bei Kaffee und Kuchen musikalische Töne bekannter Schlager und Musicals, "
         u"dargeboten von einem Duo. Einlass 14.30 Uhr.", None),
        (u"29. Aug", u"2026 · 17–23 Uhr",
         u"Lichterfest im agra-Park",
         u"Mit Live-Musik von Old Way LE, Neil-Young-Covern und mehr. Für das Museum gilt "
         u"an diesem Tag ermäßigter Eintritt für alle.", u"eintritt frei"),
        (u"13. Sep", u"2026 · 10–17 Uhr",
         u"Tag des offenen Denkmals",
         u"Das Torhaus nimmt teil. Ermäßigter Eintritt im Museum für alle.", None),
        (u"24.–25. Okt", u"2026 · ganztägig",
         u"213. Jahrestag der Völkerschlacht",
         u"Historische Biwaks und Darstellungen auf dem Gelände.", None),
        (u"7. Nov", u"2026 · 10–14 Uhr",
         u"Flohmarkt kulturhistorischer Zinnfiguren",
         u"Ermäßigter Eintritt im Museum.", None),
        (u"11. Nov", u"2026 · 17 Uhr",
         u"Martinfest",
         u"", u"eintritt frei"),
        (u"19. Dez", u"2026 · 17–20 Uhr",
         u"Winterzauber am Torhaus",
         u"Weihnachtslieder mit Nadine Hammer, bekannt aus „Best of Musical“.", u"eintritt frei"),
    ]

    tzeilen = []
    for tag, zeit, was, dazu, marke in termine:
        tzeilen.append(
            u'        <li data-auf>\n'
            u'          <div class="termin">\n'
            u'            <span class="termin__tag">%s<small>%s</small></span>\n'
            u'            <span class="termin__was">%s%s</span>\n'
            u'            %s\n'
            u'          </div>\n'
            u'        </li>' % (
                tag, zeit, was,
                (u'<span>%s</span>' % dazu) if dazu else u"",
                (u'<span class="termin__marke">%s</span>' % marke) if marke else u"",
            )
        )

    veranstaltungen = kopfbild(
        "allee",
        u"Ein Weg durch alte Bäume im agra-Park, an dessen Ende der weiße Torbogen des Torhauses zu sehen ist.",
        u"Was hier stattfindet.",
        u"Veranstaltungen",
        u"Konzerte, Biwaks, Flohmarkt, Martinfest — das Torhaus ist kein Ort, an dem "
        u"nur Vitrinen stehen.",
    ) + u"""
  <section class="abschnitt" aria-labelledby="termine-titel">
    <div class="wrap">
      <p class="schild" data-auf>Termine 2026</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="termine-titel" data-w="12" data-auf>
          Der Kalender des Hauses.
        </h2>
        <p class="vorspann" data-auf>
          Alle Angaben nach dem Stand der Veranstaltungsübersicht des Hauses.
          Bei Fragen zu einzelnen Terminen hilft ein Anruf unter
          <a class="textlink" href="tel:+493413389107">0341 3389107</a>.
        </p>
      </div>
      <ul class="termine mt-6">
%(tzeilen)s
      </ul>
    </div>
  </section>

  <section class="abschnitt flaeche-dunkel" aria-labelledby="laufend-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Ganzjährig</p>
        <h2 class="t-gross" id="laufend-titel" data-w="13" data-auf>
          Historisches Tabletop
        </h2>
        <p class="vorspann" data-auf>
          Die aktuelle Sonderausstellung läuft vom 4. April 2026 bis zum 31. März 2027
          und ist im regulären Eintritt enthalten.
        </p>
        <p data-auf>
          <a class="textlink" href="museum.html#sonderausstellung">Zur Ausstellung <span aria-hidden="true">→</span></a>
        </p>
      </div>
      <div class="stapel-weit" data-auf>
        <p class="schild">Gut zu wissen</p>
        <dl class="tafel">
          <div>
            <dt>Zusätzlich offen</dt>
            <dd>Freitag, 15. Mai 2026, 10–17 Uhr</dd>
          </div>
          <div>
            <dt>22.–25. Mai 2026</dt>
            <dd>Zugang nur mit Eintrittskarte zum Heidnischen Dorf (Wave-Gotik-Treffen)</dd>
          </div>
          <div>
            <dt>Jahreswechsel</dt>
            <dd>24. Dezember 2026 bis 1. Januar 2027 geschlossen
              <small>Gruppenanfragen sind auch in dieser Zeit möglich.</small></dd>
          </div>
        </dl>
      </div>
    </div>
  </section>

  <section class="abschnitt abschnitt--eng flaeche-sand">
    <div class="wrap zweispalt">
      <div>
        <p class="schild" data-auf>Rundherum</p>
        <h2 class="t-mittel" data-w="18" data-auf>
          Veranstaltungen der Nachbarn.
        </h2>
        <p class="mt-4" data-auf>
          Viele Termine entstehen gemeinsam mit dem Bürgerverein Dölitz, den
          Zinnfigurenfreunden und dem agra-Park.
        </p>
      </div>
      <ul class="verweise" data-auf>
        <li><a href="https://agra-park.info/" rel="noopener">
          <span class="verweise__name">agra-Park</span>
          <span class="verweise__was">Lichterfest und mehr</span></a></li>
        <li><a href="https://www.bv-doelitz-online.de/" rel="noopener">
          <span class="verweise__name">Bürgerverein Dölitz e.&nbsp;V.</span>
          <span class="verweise__was">Stadtteilarbeit</span></a></li>
        <li><a href="https://www.leipzig1813.com/" rel="noopener">
          <span class="verweise__name">Verband Jahrfeier 1813 e.&nbsp;V.</span>
          <span class="verweise__was">Jahrestag der Völkerschlacht</span></a></li>
      </ul>
    </div>
  </section>
""" % {"tzeilen": "\n".join(tzeilen)}

    raus.append(seite(
        "veranstaltungen.html",
        u"Veranstaltungen — Torhaus Dölitz",
        u"Termine 2026 am Torhaus Dölitz: Kaffeekonzert, Lichterfest im agra-Park, "
        u"Tag des offenen Denkmals, 213. Jahrestag der Völkerschlacht, Zinnfiguren-Flohmarkt, "
        u"Martinfest und Winterzauber.",
        veranstaltungen, aktiv="veranstaltungen.html"))

    # =======================================================================
    # UNTERSTUETZEN
    # =======================================================================

    unterstuetzen = kopfbild(
        "torhaus-wiese",
        u"Das Torhaus Dölitz zwischen alten Pappeln, davor eine Wiese im Sommerlicht.",
        u"Ein Verein hält dieses Haus.",
        u"Unterstützen",
        u"Patenschaften, Spenden, der Museumsshop und die Vermietung des Gewölbes — "
        u"davon lebt das Torhaus.",
    ) + u"""
  <section class="abschnitt" aria-labelledby="paten-titel">
    <div class="wrap">
      <p class="schild" data-auf>Patenschaften</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="paten-titel" data-w="14" data-auf>
          Ein Diorama, ein Haus, ein Baum.
        </h2>
        <p class="vorspann" data-auf>
          Drei Wege, das Torhaus dauerhaft zu unterstützen. Bei allen dreien wird der
          Name der Patin oder des Paten sichtbar — im Haus, am Objekt oder am Baum.
        </p>
      </div>
      <div class="karten mt-6">
        <div class="karte" data-auf data-gruppe="0">
          <h3 class="t-klein">Dioramenpatenschaft</h3>
          <p>Paten gestalten „ihr“ Diorama mit. Sie erhalten eine Patenurkunde, eine
            dauerhafte Namensnennung sowie eine Ehrenplakette direkt beim Diorama in
            der Ausstellung. Für die Dauer der Patenschaft haben Pate und eine
            Begleitperson freien Eintritt.</p>
        </div>
        <div class="karte" data-auf data-gruppe="1">
          <h3 class="t-klein">Torhauspatenschaft</h3>
          <p>Sie unterstützt den Erhalt des Gebäudes selbst — eines der wenigen
            erhaltenen barocken Häuser Leipzigs — und damit auch den des Museums.</p>
        </div>
        <div class="karte" data-auf data-gruppe="2">
          <h3 class="t-klein">Baumpatenschaft</h3>
          <p>Für das Außengelände. Zu jedem Baum gehört eine Patenplakette. Die
            Patenschaft ist allein durch die Lebensdauer des Baumes begrenzt.
            Bisher gepflanzt: Winterlinde, Sommerlinde, Wildapfel, Wildbirne,
            Traubenkirsche, Vogelkirsche, Blutpflaume, Eberesche.</p>
        </div>
        <div class="karte" data-auf data-gruppe="3">
          <h3 class="t-klein">Ansprechen</h3>
          <p>Für alle drei Patenschaften genügt eine Nachricht an
            <a class="textlink" href="mailto:info@torhaus-doelitz.eu">info@torhaus-doelitz.eu</a>
            oder ein Anruf unter <a class="textlink" href="tel:+493413389107">0341 3389107</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="abschnitt flaeche-dunkel" aria-labelledby="spende-titel">
    <div class="wrap zweispalt zweispalt--kippen">
      <div class="stapel-weit">
        <p class="schild" data-auf>Das virtuelle Diorama</p>
        <h2 class="nur-fuer-screenreader" id="spende-titel">Das virtuelle Diorama — die Spendenaktion</h2>
        <blockquote class="zitat" data-auf>
          Eine Figur kostet einen Euro.
          <span class="zitat__quelle">Die Spendenaktion seit April 2020</span>
        </blockquote>
        <p class="notiz" data-auf>
          Ab zehn erworbenen Figuren fließen 10 % in ein sozial-ökologisches Projekt
          im Stadtteil Dölitz, ausgewählt gemeinsam mit dem Bürgerverein.
        </p>
      </div>
      <div class="stapel-weit">
        <p class="vorspann" data-auf>
          In den Schließzeiten ab März 2020 brachen dem Museum Eintrittsgelder und
          viele weitere Einnahmen weg. Das Ziel der Aktion: die Figurenzahl des größten
          Dioramas im Haus zu überbieten — 12.126 Figuren. Wer mitmacht, wird im Museum
          genannt.
        </p>
        <div class="zahlen zahlen--paar zahlen--wenig">
          <div class="nische" data-auf data-gruppe="0">
            <span class="nische__zahl"><span data-zaehlen="11185">11.185</span></span>
            <p class="nische__was">virtuelle Figuren bereits erworben</p>
          </div>
          <div class="nische" data-auf data-gruppe="1">
            <span class="nische__zahl"><span data-zaehlen="12126">12.126</span></span>
            <p class="nische__was">Figuren im größten Diorama — das Ziel</p>
          </div>
        </div>
        <dl class="tafel mt-5" data-auf>
          <div>
            <dt>Empfänger</dt>
            <dd>Torhaus Dölitz — VJV b. Leipzig 1813 e.&nbsp;V.</dd>
          </div>
          <div>
            <dt>IBAN</dt>
            <dd>DE61 8605 5592 1090 0870 51<br><small>BIC: WELADE8LXXX</small></dd>
          </div>
          <div>
            <dt>Verwendungszweck</dt>
            <dd>„Virtuelles Diorama“ — Erhalt Torhaus Dölitz mit Museum und Parkanlage
              <small>Bitte angeben, ob der Name genannt werden darf. Spendenquittungen
                sind möglich — dazu bitte zusätzlich eine E-Mail an
                info@torhaus-doelitz.eu.</small></dd>
          </div>
        </dl>
      </div>
    </div>
  </section>

  <section class="abschnitt" id="shop" aria-labelledby="shop-titel">
    <div class="wrap">
      <p class="schild" data-auf>Museumsshop</p>
      <div class="zweispalt">
        <h2 class="t-gross" id="shop-titel" data-w="13" data-auf>
          Etwas mitnehmen.
        </h2>
        <p class="vorspann" data-auf>
          Alle Artikel sind im Museum erhältlich oder können per Brief oder E-Mail
          bestellt und zugeschickt werden — bei Abholung entfallen die Versandkosten.
          Gutscheine gibt es in frei wählbarer Höhe.
        </p>
      </div>
      <ul class="preise mt-6" data-auf>
        <li>
          <span class="preise__was">Dölitz in der Völkerschlachtzeit<small>Buch, Lieferung zzgl. 3,50 € Versand</small></span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">24,00 €</span>
        </li>
        <li>
          <span class="preise__was">Rommé Bonaparte<small>Kartendeck des Leipziger Illustrators André Martini, 3. Auflage mit 110 Motiven — jede Karte anders</small></span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">18,00 €</span>
        </li>
        <li>
          <span class="preise__was">Das Belagerungsspiel — Völkerschlacht bei Leipzig 1813<small>2. Auflage</small></span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">15,00 €</span>
        </li>
        <li>
          <span class="preise__was">Gedenkmedaillen zur Völkerschlacht<small>Jahrgänge 2014 bis 2017</small></span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">je 12,00 €</span>
        </li>
        <li>
          <span class="preise__was">Europa und Bonaparte<small>Bilder aus einer schicksalhaften Epoche, 44 Seiten, DIN A4 quer</small></span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">10,00 €</span>
        </li>
        <li>
          <span class="preise__was">Tasse</span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">8,50 €</span>
        </li>
        <li>
          <span class="preise__was">Malheft „Napoleons Armee — Uniformen zum Ausmalen“</span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">4,90 €</span>
        </li>
        <li>
          <span class="preise__was">Magnete<small>Motive: Blücher, Larrey, Luther, Napoleon, St. Helena, Völkerschlachtdenkmal, Torhaus, Comic, Van Gogh</small></span>
          <span class="preise__punkte" aria-hidden="true"></span>
          <span class="preise__wert">je 3,00 €</span>
        </li>
      </ul>
      <p class="mt-5" data-auf>
        <a class="knopf" href="mailto:info@torhaus-doelitz.eu?subject=Bestellung%20Museumsshop">
          Per E-Mail bestellen <span class="knopf__pfeil" aria-hidden="true">→</span></a>
      </p>
      <p class="notiz mt-4" data-auf>
        Rommé Bonaparte entstand unter dem Label „Edition Torhaus Dölitz“ zusammen mit
        der Altenburger Tourismus GmbH; das MDR-Fernsehen hat darüber berichtet.
      </p>
    </div>
  </section>

  <section class="abschnitt flaeche-sand" id="vermietung" aria-labelledby="miete-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Vermietung</p>
        <h2 class="t-gross" id="miete-titel" data-w="14" data-auf>
          Feiern Sie im Gewölbe.
        </h2>
        <p class="vorspann" data-auf>
          Das Torhaus vermietet seinen Gewölberaum samt voll ausgestatteter Küche —
          in U-Form oder anderer Bestuhlung — sowie das Gelände. Jede Vermietung
          hilft dem Haus.
        </p>
        <p data-auf>
          Ist Ihr Wunschtermin belegt, fragen Sie den Seminarraum der benachbarten
          Dölitzer Wassermühle an: 0341 3389352 oder GAZ-Leipzig@t-online.de.
        </p>
      </div>
      <div data-auf>
        <dl class="tafel">
          <div>
            <dt>Anfragen</dt>
            <dd><a class="textlink" href="tel:+491781317071">0178 1317071</a>
              <small>Täglich 10–19 Uhr.</small></dd>
          </div>
          <div>
            <dt>E-Mail</dt>
            <dd><a class="textlink" href="mailto:thd-reservierung@leipzig1813.com">thd-reservierung@leipzig1813.com</a></dd>
          </div>
          <div>
            <dt>Räume</dt>
            <dd>Gewölbe mit Bestuhlung nach Wunsch, voll ausgestattete Küche, Außengelände</dd>
          </div>
        </dl>
      </div>
    </div>
  </section>

  <section class="abschnitt" aria-labelledby="danke-titel">
    <div class="wrap zweispalt">
      <div class="stapel-weit">
        <p class="schild" data-auf>Partner und Förderer</p>
        <h2 class="t-mittel" id="danke-titel" data-w="16" data-auf>
          Ohne sie stünde hier weniger.
        </h2>
        <p data-auf>
          Dem Kulturamt der Stadt Leipzig gilt der Dank für die stetige Unterstützung.
          Die LEIPZIGSTIFTUNG hat 2016 und 2019 große Teile der Dauerausstellung neu
          ermöglicht; 2014 haben die Sparkasse Leipzig und Saturn im Leipziger
          Hauptbahnhof geholfen.
        </p>
        <p class="notiz" data-auf>
          Das Torhaus gehört gemeinsam mit dem Sanitäts- und Lazarettmuseum
          Seifertshain, dem Körnerhaus Leipzig und dem Regionalmuseum Torhaus
          Markkleeberg zum Museumsverbund 1813.
        </p>
      </div>
      <ul class="verweise" data-auf>
        <li><a href="https://www.leipzig.de/" rel="noopener">
          <span class="verweise__name">Kulturamt der Stadt Leipzig</span>
          <span class="verweise__was">Förderung</span></a></li>
        <li><a href="https://www.leipzigstiftung.de/" rel="noopener">
          <span class="verweise__name">LEIPZIGSTIFTUNG</span>
          <span class="verweise__was">Neukonzeption der Dauerausstellung</span></a></li>
        <li><a href="https://www.zinnfigurenfreunde-leipzig.de/" rel="noopener">
          <span class="verweise__name">Zinnfigurenfreunde Leipzig e.&nbsp;V.</span>
          <span class="verweise__was">Ausstellungen und Sammlung</span></a></li>
        <li><a href="https://www.stiftung-voelkerschlachtdenkmal-leipzig.de/" rel="noopener">
          <span class="verweise__name">Stiftung Völkerschlachtdenkmal</span>
          <span class="verweise__was">Leipzig</span></a></li>
        <li><a href="http://www.sanitaetsmuseum1813.de/" rel="noopener">
          <span class="verweise__name">Sanitäts- und Lazarettmuseum</span>
          <span class="verweise__was">Seifertshain</span></a></li>
        <li><a href="https://www.torhaus-markkleeberg.de/" rel="noopener">
          <span class="verweise__name">Regionalmuseum Torhaus Markkleeberg</span>
          <span class="verweise__was">Museumsverbund 1813</span></a></li>
        <li><a href="http://www.koernerhaus-leipzig.de/" rel="noopener">
          <span class="verweise__name">Körnerhaus Leipzig</span>
          <span class="verweise__was">Museumsverbund 1813</span></a></li>
      </ul>
    </div>
  </section>
"""

    raus.append(seite(
        "unterstuetzen.html",
        u"Unterstützen — Torhaus Dölitz",
        u"Patenschaften, das virtuelle Diorama, der Museumsshop und die Vermietung des "
        u"Gewölbes: So wird das vereinsgetragene Torhaus Dölitz getragen.",
        unterstuetzen, aktiv="unterstuetzen.html"))

    # =======================================================================
    # RAHMEN fuer die Pflichtseiten (Stufe 3 setzt hier ein)
    # =======================================================================

    rahmen = u"""
  <section class="wrap">
    <article class="rechtstext">
<!--PFLICHT-INHALT-->
    </article>
  </section>
"""

    datei, groesse = seite(
        "rahmen.html", u"{{TITEL}}",
        u"Rechtliche Angaben zum Torhaus Dölitz mit Zinnfigurenmuseum in Leipzig.",
        rahmen, aktiv=None)
    raus.append((datei, groesse))

    return raus
