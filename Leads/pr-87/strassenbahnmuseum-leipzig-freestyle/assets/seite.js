/* Straßenbahnmuseum Leipzig — kleine Verbesserungen.
   Die Seite funktioniert vollständig ohne JavaScript; dieses Skript
   blendet nur die Navigation auf kleinen Bildschirmen ein und hebt den
   nächsten Öffnungstag hervor. Keine externen Aufrufe, kein Tracking. */

(function () {
  "use strict";

  /* --- Navigation auf kleinen Bildschirmen --- */

  var schalter = document.querySelector(".navi__schalter");
  var navi = document.getElementById("hauptnavigation");

  if (schalter && navi) {
    /* Erst wenn dieses Skript läuft, darf die Navigation eingeklappt werden. */
    document.documentElement.classList.add("navi-bereit");
    schalter.hidden = false;
    schalter.addEventListener("click", function () {
      var offen = navi.getAttribute("data-offen") === "ja";
      navi.setAttribute("data-offen", offen ? "nein" : "ja");
      schalter.setAttribute("aria-expanded", offen ? "false" : "true");
    });

    navi.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        navi.setAttribute("data-offen", "nein");
        schalter.setAttribute("aria-expanded", "false");
        schalter.focus();
      }
    });
  }

  /* --- Nächster Öffnungstag --- */

  var termine = Array.prototype.slice.call(
    document.querySelectorAll(".termin[data-datum]")
  );
  if (!termine.length) return;

  var heute = new Date();
  heute.setHours(0, 0, 0, 0);

  var naechster = null;

  termine.forEach(function (termin) {
    var teile = termin.getAttribute("data-datum").split("-");
    var datum = new Date(+teile[0], +teile[1] - 1, +teile[2]);
    datum.setHours(0, 0, 0, 0);

    if (datum < heute) {
      termin.setAttribute("data-vergangen", "ja");
      return;
    }
    if (!naechster) {
      naechster = { element: termin, datum: datum };
    }
  });

  if (naechster) {
    var marke = document.createElement("span");
    marke.className = "termin__marke";
    marke.textContent = "Nächster Termin";
    var ziel = naechster.element.querySelector(".termin__was");
    if (ziel) {
      ziel.parentNode.insertBefore(marke, ziel);
    } else {
      naechster.element.appendChild(marke);
    }
  }

  var anzeige = document.querySelector("[data-naechster-termin]");
  if (!anzeige) return;

  if (!naechster) {
    anzeige.textContent = "Termine 2027 folgen";
    var zusatz = document.querySelector("[data-naechster-termin-zusatz]");
    if (zusatz) {
      zusatz.textContent =
        "Die Termine der nächsten Saison gibt der Verein rechtzeitig bekannt.";
    }
    return;
  }

  var format = new Intl.DateTimeFormat("de-DE", {
    day: "numeric",
    month: "long",
    year: "numeric"
  });
  anzeige.textContent = format.format(naechster.datum);

  var zeit = naechster.element.getAttribute("data-zeit");
  var zusatzfeld = document.querySelector("[data-naechster-termin-zusatz]");
  if (zeit && zusatzfeld) {
    zusatzfeld.textContent = zeit;
  }
})();
