/* Torhaus Dölitz — Bewegung.
   Alles hier ist Zugabe: ohne JavaScript ist die Seite vollstaendig lesbar
   und bedienbar. Nichts blendet dauerhaft aus, nichts wird nachgeladen.
   Wer prefers-reduced-motion gesetzt hat, bekommt keine Animation. */

(function () {
  'use strict';

  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* --- Menue fuer schmale Fenster ---------------------------------------- */

  var knopf = document.querySelector('[data-menuknopf]');
  var schublade = document.querySelector('[data-schublade]');

  if (knopf && schublade) {
    knopf.addEventListener('click', function () {
      var offen = schublade.getAttribute('data-offen') === 'true';
      schublade.setAttribute('data-offen', String(!offen));
      knopf.setAttribute('aria-expanded', String(!offen));
      knopf.querySelector('[data-menutext]').textContent = offen ? 'Menü' : 'Schließen';
    });

    schublade.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        schublade.setAttribute('data-offen', 'false');
        knopf.setAttribute('aria-expanded', 'false');
        knopf.querySelector('[data-menutext]').textContent = 'Menü';
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && schublade.getAttribute('data-offen') === 'true') {
        schublade.setAttribute('data-offen', 'false');
        knopf.setAttribute('aria-expanded', 'false');
        knopf.querySelector('[data-menutext]').textContent = 'Menü';
        knopf.focus();
      }
    });
  }

  /* --- Abschnitte blenden beim Scrollen ein ------------------------------ */

  var zuOeffnen = Array.prototype.slice.call(document.querySelectorAll('[data-auf]'));

  if (ruhig.matches || !('IntersectionObserver' in window)) {
    zuOeffnen.forEach(function (el) { el.setAttribute('data-auf', 'ja'); });
  } else {
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.setAttribute('data-auf', 'ja');
        beobachter.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });

    zuOeffnen.forEach(function (el, i) {
      /* Geschwister versetzt einblenden - der Blick laeuft mit. */
      var gruppe = el.getAttribute('data-gruppe');
      if (gruppe) el.style.setProperty('--verzug', (parseInt(gruppe, 10) * 90) + 'ms');
      beobachter.observe(el);
    });
  }

  /* --- Zahlen zaehlen hoch ----------------------------------------------- */

  function formatiere(n, muster) {
    var s = String(n);
    if (muster.indexOf('.') === -1) return s;
    return s.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  }

  var zahlen = Array.prototype.slice.call(document.querySelectorAll('[data-zaehlen]'));

  if (zahlen.length && !ruhig.matches && 'IntersectionObserver' in window) {
    var zaehlBeobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        zaehlBeobachter.unobserve(el);

        var ziel = parseInt(el.getAttribute('data-zaehlen'), 10);
        var muster = el.textContent.trim();
        var dauer = 1400;
        var start = null;

        function schritt(zeit) {
          if (start === null) start = zeit;
          var t = Math.min((zeit - start) / dauer, 1);
          var e2 = 1 - Math.pow(1 - t, 3);           /* easeOutCubic */
          el.textContent = formatiere(Math.round(ziel * e2), muster);
          if (t < 1) requestAnimationFrame(schritt);
          else el.textContent = muster;
        }
        requestAnimationFrame(schritt);
      });
    }, { threshold: 0.5 });

    zahlen.forEach(function (el) { zaehlBeobachter.observe(el); });
  }

  /* --- Der Torbogen oeffnet sich beim Scrollen --------------------------- */

  var oeffnungen = Array.prototype.slice.call(document.querySelectorAll('.oeffnung'));

  if (oeffnungen.length && !ruhig.matches) {
    var laueft = false;

    var rechne = function () {
      laueft = false;
      var vh = window.innerHeight;
      oeffnungen.forEach(function (el) {
        var r = el.getBoundingClientRect();
        /* 0 = Abschnitt kommt gerade ins Bild, 1 = mittig angekommen */
        var p = 1 - Math.max(0, Math.min(1, (r.top - vh * 0.12) / (vh * 0.72)));
        el.style.setProperty('--auf', p.toFixed(3));
      });
    };

    var beiScroll = function () {
      if (laueft) return;
      laueft = true;
      requestAnimationFrame(rechne);
    };

    window.addEventListener('scroll', beiScroll, { passive: true });
    window.addEventListener('resize', beiScroll);
    rechne();
  }

  /* --- Schwebender Knopf blendet am Fuss aus ----------------------------- */

  var schwebe = document.querySelector('[data-schwebe]');
  var fuss = document.querySelector('[data-fuss]');

  if (schwebe && fuss && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        schwebe.setAttribute('data-weg', String(e.isIntersecting));
      });
    }, { rootMargin: '0px 0px -40px 0px' }).observe(fuss);
  }

  /* --- Aktuelle Seite in der Navigation markieren ------------------------ */

  var hier = window.location.pathname.replace(/index\.html$/, '').replace(/\/+$/, '/');
  Array.prototype.forEach.call(document.querySelectorAll('[data-nav] a'), function (a) {
    var ziel = a.getAttribute('href');
    if (!ziel || ziel.charAt(0) === '#' || ziel.indexOf('http') === 0) return;
    var voll = new URL(ziel, window.location.href).pathname
      .replace(/index\.html$/, '').replace(/\/+$/, '/');
    if (voll === hier) a.setAttribute('aria-current', 'page');
  });
})();
