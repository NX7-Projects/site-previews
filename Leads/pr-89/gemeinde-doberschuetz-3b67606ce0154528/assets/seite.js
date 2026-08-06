/* Gemeinde Doberschuetz - Entwurf. Kein Tracker, keine externen Aufrufe.
   Vier kleine Dinge: Navigation auf dem Telefon, Einblenden beim Scrollen,
   der Status "Rathaus jetzt geoeffnet?" und der schwebende Kontaktknopf. */
(function () {
  "use strict";

  /* --- Navigation auf schmalen Geraeten --------------------------------- */
  var schalter = document.querySelector(".nav-schalter");
  var nav = document.getElementById("hauptnavigation");
  if (schalter && nav) {
    schalter.addEventListener("click", function () {
      var offen = nav.classList.toggle("ist-offen");
      schalter.setAttribute("aria-expanded", offen ? "true" : "false");
    });
    nav.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        nav.classList.remove("ist-offen");
        schalter.setAttribute("aria-expanded", "false");
        schalter.focus();
      }
    });
  }

  /* --- Sanftes Einblenden ----------------------------------------------- */
  var reduziert = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var einblenden = document.querySelectorAll(".auf");
  if (reduziert || !("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(einblenden, function (el) {
      el.classList.add("ist-da");
    });
  } else {
    var beobachter = new IntersectionObserver(
      function (eintraege) {
        eintraege.forEach(function (eintrag) {
          if (eintrag.isIntersecting) {
            eintrag.target.classList.add("ist-da");
            beobachter.unobserve(eintrag.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.05 }
    );
    Array.prototype.forEach.call(einblenden, function (el) {
      beobachter.observe(el);
    });
  }

  /* --- Rathaus: geoeffnet oder nicht? -----------------------------------
     Quelle der Zeiten: doberschuetz.eu/dob/rathaus/oeffnungszeiten.php
     Feiertage sind hier nicht hinterlegt; darauf weist die Seite im Text hin. */
  var OEFFNUNG = {
    1: [[540, 720]],
    2: [
      [540, 720],
      [780, 1050]
    ],
    4: [
      [540, 720],
      [780, 900]
    ]
  };
  var TAGE = [
    "Sonntag",
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag"
  ];

  function uhr(minuten) {
    var h = Math.floor(minuten / 60);
    var m = minuten % 60;
    return h + ":" + (m < 10 ? "0" + m : m);
  }

  function naechsteOeffnung(tag, minute) {
    for (var i = 0; i < 8; i++) {
      var t = (tag + i) % 7;
      var spannen = OEFFNUNG[t];
      if (!spannen) continue;
      for (var j = 0; j < spannen.length; j++) {
        if (i > 0 || spannen[j][0] > minute) {
          return { tag: t, start: spannen[j][0], heute: i === 0 };
        }
      }
    }
    return null;
  }

  var status = document.querySelector("[data-status]");
  if (status) {
    var jetzt = new Date();
    var tag = jetzt.getDay();
    var minute = jetzt.getHours() * 60 + jetzt.getMinutes();
    var spannen = OEFFNUNG[tag] || [];
    var offen = null;
    for (var i = 0; i < spannen.length; i++) {
      if (minute >= spannen[i][0] && minute < spannen[i][1]) offen = spannen[i];
    }
    var text = status.querySelector("[data-status-text]");
    if (offen) {
      status.setAttribute("data-offen", "ja");
      text.textContent = "Jetzt geöffnet – noch bis " + uhr(offen[1]) + " Uhr";
    } else {
      var naechste = naechsteOeffnung(tag, minute);
      status.setAttribute("data-offen", "nein");
      if (naechste && naechste.heute) {
        text.textContent = "Gerade geschlossen – heute wieder ab " + uhr(naechste.start) + " Uhr";
      } else if (naechste) {
        text.textContent =
          "Gerade geschlossen – wieder am " +
          TAGE[naechste.tag] +
          " ab " +
          uhr(naechste.start) +
          " Uhr";
      } else {
        text.textContent = "Öffnungszeiten siehe Tabelle";
      }
    }
    var heutigeZeile = document.querySelector('[data-tag="' + tag + '"]');
    if (heutigeZeile) heutigeZeile.setAttribute("data-heute", "ja");
  }

  /* --- Kontaktknopf blendet sich am Fuss aus ----------------------------- */
  var knopf = document.querySelector(".kontaktknopf");
  var fuss = document.querySelector(".fuss");
  if (knopf && fuss && "IntersectionObserver" in window) {
    new IntersectionObserver(
      function (eintraege) {
        eintraege.forEach(function (e) {
          knopf.classList.toggle("ist-versteckt", e.isIntersecting);
        });
      },
      { rootMargin: "0px 0px -20% 0px" }
    ).observe(fuss);
  }
})();
