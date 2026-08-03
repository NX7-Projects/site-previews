/* Museum Eisenhammer Dorfchemnitz - Verhalten der Seite.
   Kein Tracker, keine externen Dienste. Alles ist ohne JavaScript benutzbar. */
(function () {
  "use strict";

  var ruhig = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* --- Navigation auf kleinen Bildschirmen ------------------------ */
  var schalter = document.querySelector(".nav__schalter");
  var nav = document.getElementById("hauptnavigation");
  if (schalter && nav) {
    schalter.addEventListener("click", function () {
      var offen = nav.getAttribute("data-offen") === "ja";
      nav.setAttribute("data-offen", offen ? "nein" : "ja");
      schalter.setAttribute("aria-expanded", offen ? "false" : "true");
      schalter.textContent = offen ? "Menü" : "Schließen";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && nav.getAttribute("data-offen") === "ja") {
        nav.setAttribute("data-offen", "nein");
        schalter.setAttribute("aria-expanded", "false");
        schalter.textContent = "Menü";
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-offen") === "ja") {
        nav.setAttribute("data-offen", "nein");
        schalter.setAttribute("aria-expanded", "false");
        schalter.textContent = "Menü";
        schalter.focus();
      }
    });
  }

  /* --- Kopf: Linie erst zeigen, wenn gescrollt wurde -------------- */
  var kopf = document.querySelector(".kopf");
  var auftakt = document.querySelector(".auftakt");

  /* --- Einblenden der Abschnitte ---------------------------------- */
  var aufbau = document.querySelectorAll(".auf");
  if ("IntersectionObserver" in window && aufbau.length) {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("auf--da");
          beobachter.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
    Array.prototype.forEach.call(aufbau, function (el) { beobachter.observe(el); });
  } else {
    Array.prototype.forEach.call(aufbau, function (el) { el.classList.add("auf--da"); });
  }

  /* --- Zahlen zaehlen hoch ---------------------------------------- */
  var zahlen = document.querySelectorAll("[data-zaehler]");
  if ("IntersectionObserver" in window && zahlen.length && !ruhig.matches) {
    var zObs = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        zObs.unobserve(e.target);
        var el = e.target;
        var ziel = parseFloat(el.getAttribute("data-zaehler"));
        var komma = (el.getAttribute("data-komma") || "0") | 0;
        var start = null;
        var dauer = 1100;
        function schritt(t) {
          if (start === null) start = t;
          var p = Math.min((t - start) / dauer, 1);
          var e2 = 1 - Math.pow(1 - p, 3);
          var wert = (ziel * e2).toFixed(komma);
          el.textContent = String(wert).replace(".", ",");
          if (p < 1) requestAnimationFrame(schritt);
        }
        requestAnimationFrame(schritt);
      });
    }, { threshold: 0.4 });
    Array.prototype.forEach.call(zahlen, function (el) { zObs.observe(el); });
  }

  /* --- Auftaktbild: sehr leichte Tiefenwirkung -------------------- */
  var bild = document.querySelector(".auftakt__bild");
  var schwebe = document.querySelector(".schwebe");
  var fuss = document.querySelector(".fuss");
  var laeuft = false;

  function messen() {
    var y = window.pageYOffset || document.documentElement.scrollTop;

    if (kopf) {
      kopf.classList.toggle("kopf--gescrollt", y > 12);
      if (auftakt) {
        var grenze = auftakt.offsetTop + auftakt.offsetHeight - kopf.offsetHeight;
        kopf.classList.toggle("kopf--auf-dunkel", y < grenze);
      }
    }

    if (bild && !ruhig.matches) {
      var h = auftakt ? auftakt.offsetHeight : 0;
      if (y < h) bild.style.transform = "translate3d(0," + (y * 0.16).toFixed(1) + "px,0)";
    }

    if (schwebe && fuss) {
      // Verschwindet am Fuss - und zeigt sich erst, wenn der Auftakt
      // vorbei ist: dort steht der Knopf ohnehin schon gross im Bild.
      var fussOben = fuss.getBoundingClientRect().top;
      var imAuftakt = auftakt && auftakt.getBoundingClientRect().bottom > window.innerHeight * 0.6;
      schwebe.classList.toggle("schwebe--weg", fussOben < window.innerHeight - 40 || imAuftakt);
    }

    laeuft = false;
  }

  function anstossen() {
    if (laeuft) return;
    laeuft = true;
    requestAnimationFrame(messen);
  }

  window.addEventListener("scroll", anstossen, { passive: true });
  window.addEventListener("resize", anstossen, { passive: true });
  messen();

  /* --- Hinweis, ob das Museum gerade in der Saison ist ------------
     Belegte Regel: Mai bis Oktober, Donnerstag bis Sonntag, 13 bis 16 Uhr.
     Es wird nur die Saison benannt, keine Tagesaussage erfunden. */
  var saison = document.querySelector("[data-saison]");
  if (saison) {
    var m = new Date().getMonth() + 1;
    saison.textContent = m >= 5 && m <= 10 ? "Saison läuft" : "Winterpause";
  }
})();
