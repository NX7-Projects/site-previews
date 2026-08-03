/* Förderverein Völkerschlachtdenkmal e. V. — Verhalten der Seite.
   Kein Tracker, keine externen Dienste, keine Cookies.
   Alles hier ist Zugabe: ohne JavaScript bleibt die Seite vollständig lesbar. */
(function () {
  'use strict';

  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* --- Kopf: wird fest, sobald der Auftakt verlassen ist --- */
  var kopf = document.querySelector('.kopf');
  var schwebe = document.querySelector('.schwebe');
  var fuss = document.querySelector('.fuss');
  var auftakt = document.querySelector('.auftakt');

  function amKopf() {
    if (!kopf) return;
    var schwelle = auftakt ? Math.min(auftakt.offsetHeight - 90, window.innerHeight * 0.6) : 12;
    kopf.classList.toggle('ist-fest', window.scrollY > schwelle);
  }

  /* --- Schwebender Spendenknopf: blendet am Fuß aus --- */
  function amKnopf() {
    if (!schwebe || !fuss) return;
    var f = fuss.getBoundingClientRect();
    var frueh = window.scrollY < 240;
    schwebe.classList.toggle('ist-weg', f.top < window.innerHeight - 40 || frueh);
  }

  var wartet = false;
  function beimRollen() {
    if (wartet) return;
    wartet = true;
    window.requestAnimationFrame(function () {
      amKopf();
      amKnopf();
      wartet = false;
    });
  }
  window.addEventListener('scroll', beimRollen, { passive: true });
  window.addEventListener('resize', beimRollen);
  beimRollen();

  /* --- Menü auf kleinen Schirmen --- */
  var klapper = document.querySelector('.klapper');
  var wegweiser = document.querySelector('.wegweiser');
  if (klapper && wegweiser) {
    klapper.addEventListener('click', function () {
      var offen = klapper.getAttribute('aria-expanded') === 'true';
      klapper.setAttribute('aria-expanded', String(!offen));
      wegweiser.classList.toggle('ist-offen', !offen);
    });
    wegweiser.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        klapper.setAttribute('aria-expanded', 'false');
        wegweiser.classList.remove('ist-offen');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && wegweiser.classList.contains('ist-offen')) {
        klapper.setAttribute('aria-expanded', 'false');
        wegweiser.classList.remove('ist-offen');
        klapper.focus();
      }
    });
  }

  /* --- Scroll-Reveal: sanftes Einblenden mit leichtem Versatz --- */
  var hebt = document.querySelectorAll('.hebt');
  if (!('IntersectionObserver' in window) || ruhig.matches) {
    Array.prototype.forEach.call(hebt, function (el) { el.classList.add('ist-da'); });
  } else {
    var wache = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('ist-da');
          wache.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    Array.prototype.forEach.call(hebt, function (el) { wache.observe(el); });
  }

  /* --- Zähler: die Summen laufen einmal hoch, wenn sie ins Bild kommen --- */
  function zaehle(el) {
    var ziel = parseFloat(el.getAttribute('data-zahl'));
    var nach = parseInt(el.getAttribute('data-nach') || '0', 10);
    if (isNaN(ziel)) return;
    if (ruhig.matches) { el.textContent = fasse(ziel, nach); return; }
    var dauer = 1300, start = null;
    // Sicherheitsnetz: der Endwert steht in jedem Fall da, auch wenn die
    // Animation unterbrochen wird (Tab im Hintergrund, gedrosselte Frames).
    window.setTimeout(function () { el.textContent = fasse(ziel, nach); }, dauer + 400);
    function schritt(t) {
      if (start === null) start = t;
      var p = Math.min((t - start) / dauer, 1);
      var e = 1 - Math.pow(1 - p, 3);
      el.textContent = fasse(ziel * e, nach);
      if (p < 1) window.requestAnimationFrame(schritt);
      else el.textContent = fasse(ziel, nach);
    }
    window.requestAnimationFrame(schritt);
  }
  function fasse(n, nach) {
    return n.toLocaleString('de-DE', { minimumFractionDigits: nach, maximumFractionDigits: nach });
  }

  var zahlen = document.querySelectorAll('[data-zahl]');
  if (zahlen.length) {
    if (!('IntersectionObserver' in window)) {
      Array.prototype.forEach.call(zahlen, zaehle);
    } else {
      // Der richtige Wert steht im HTML und wird NICHT vorab auf 0 gesetzt:
      // schlägt das Hochzählen fehl, steht trotzdem die richtige Zahl da.
      var zw = new IntersectionObserver(function (eintraege) {
        eintraege.forEach(function (e) {
          if (e.isIntersecting) { zaehle(e.target); zw.unobserve(e.target); }
        });
      }, { threshold: 0.05, rootMargin: '0px 0px -4% 0px' });
      Array.prototype.forEach.call(zahlen, function (el) { zw.observe(el); });
    }
  }

  /* --- Chronik: der Spendenanteil wächst beim Erreichen der Zeile --- */
  var zeilen = document.querySelectorAll('.chronik__zeile');
  if (zeilen.length && 'IntersectionObserver' in window && !ruhig.matches) {
    var cw = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('ist-da'); cw.unobserve(e.target); }
      });
    }, { threshold: 0.35 });
    Array.prototype.forEach.call(zeilen, function (el) { cw.observe(el); });
  } else {
    Array.prototype.forEach.call(zeilen, function (el) { el.classList.add('ist-da'); });
  }

  /* --- Auftakt: das Bild bewegt sich beim Rollen eine Spur langsamer --- */
  var auftaktBild = document.querySelector('.auftakt__bild img');
  if (auftaktBild && !ruhig.matches && window.matchMedia('(min-width: 861px)').matches) {
    var laeuft = false;
    window.addEventListener('scroll', function () {
      if (laeuft) return;
      laeuft = true;
      window.requestAnimationFrame(function () {
        var y = Math.min(window.scrollY, window.innerHeight);
        auftaktBild.style.transform = 'translate3d(0,' + (y * 0.09) + 'px,0) scale(1.06)';
        laeuft = false;
      });
    }, { passive: true });
  }
})();
