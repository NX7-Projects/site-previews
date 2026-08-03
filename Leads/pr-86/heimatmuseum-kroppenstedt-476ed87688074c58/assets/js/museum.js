/* Heimatmuseum Kroppenstedt - Bewegung.
   Alles hier ist Zugabe: ohne JavaScript bleibt die Seite vollstaendig
   lesbar und bedienbar (die Klasse "js" setzt erst dieses Skript). */
(function () {
  "use strict";

  var ruhig = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* --- Kopf wird fest, sobald das Kopfbild verlassen ist ----------------- */
  var kopf = document.querySelector(".kopf");
  var aufschlag = document.querySelector(".aufschlag");

  function kopfPruefen() {
    if (!kopf) return;
    if (!aufschlag) {
      /* Seiten ohne Kopfbild (Pflichtseiten) tragen den festen Kopf immer. */
      kopf.classList.add("ist-fest");
      return;
    }
    kopf.classList.toggle("ist-fest", window.scrollY > aufschlag.offsetHeight - 90);
  }

  /* --- Sanfter Versatz der Kopf- und Streifenbilder ---------------------- */
  var parallax = [].slice.call(
    document.querySelectorAll(".aufschlag__bild, .streifen__bild")
  );

  function parallaxSetzen() {
    if (ruhig.matches) return;
    var fensterHoehe = window.innerHeight;
    parallax.forEach(function (bild) {
      var kasten = bild.parentElement.getBoundingClientRect();
      if (kasten.bottom < 0 || kasten.top > fensterHoehe) return;
      var lauf = (kasten.top + kasten.height / 2 - fensterHoehe / 2) / fensterHoehe;
      var versatz = Math.max(-70, Math.min(70, lauf * -60));
      bild.style.transform = "translate3d(0," + versatz.toFixed(2) + "px,0)";
    });
  }

  var wartet = false;
  function beimScrollen() {
    if (wartet) return;
    wartet = true;
    window.requestAnimationFrame(function () {
      kopfPruefen();
      parallaxSetzen();
      wartet = false;
    });
  }

  window.addEventListener("scroll", beimScrollen, { passive: true });
  window.addEventListener("resize", beimScrollen, { passive: true });
  kopfPruefen();
  parallaxSetzen();

  /* --- Abschnitte blenden beim Scrollen ein ------------------------------ */
  var zuDecken = [].slice.call(document.querySelectorAll(".aufdecken"));

  if (!("IntersectionObserver" in window) || ruhig.matches) {
    zuDecken.forEach(function (el) { el.classList.add("ist-da"); });
  } else {
    var beobachter = new IntersectionObserver(
      function (eintraege) {
        eintraege.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add("ist-da");
          beobachter.unobserve(e.target);
        });
      },
      { rootMargin: "0px 0px -12% 0px", threshold: 0.08 }
    );
    zuDecken.forEach(function (el) { beobachter.observe(el); });

    /* Sicherheitsnetz: was nach 4 Sekunden noch versteckt ist, wird gezeigt. */
    window.setTimeout(function () {
      zuDecken.forEach(function (el) { el.classList.add("ist-da"); });
    }, 4000);
  }

  /* --- Schwebender Knopf verschwindet am Fuss ---------------------------- */
  var knopf = document.querySelector(".schwebt");
  var fuss = document.querySelector(".fuss");

  if (knopf && fuss && "IntersectionObserver" in window) {
    new IntersectionObserver(
      function (eintraege) {
        eintraege.forEach(function (e) {
          knopf.classList.toggle("ist-weg", e.isIntersecting);
        });
      },
      { rootMargin: "0px 0px -20px 0px", threshold: 0 }
    ).observe(fuss);
  }
})();
