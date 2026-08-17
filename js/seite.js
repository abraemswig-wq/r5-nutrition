(function(){
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function(v){ return v < 0 ? 0 : v > 1 ? 1 : v; };

  /* ---------- Aufziehen beim Hereinscrollen ---------- */
  /* Gesetzt wird die Marke am Abschnitt, nicht am einzelnen Element: die
     Headline-Bloecke und ihre Nachbarn sollen zusammen aufziehen. */
  var io = new IntersectionObserver(function(eintraege){
    eintraege.forEach(function(e){
      if(!e.isIntersecting) return;
      e.target.setAttribute('data-seen','true');
      var i = 0;
      e.target.querySelectorAll('.rv').forEach(function(el){
        el.style.setProperty('--d', (i++ * 70) + 'ms');
      });
      io.unobserve(e.target);
    });
  }, {rootMargin:'0px 0px -10% 0px', threshold:0.06});
  document.querySelectorAll('[data-abschnitt]').forEach(function(el){ io.observe(el); });

  /* ---------- Aufmacher: Bildwechsel + Takt ---------- */
  var kopf = document.getElementById('kopf');
  if(kopf){
    var bilder = [].slice.call(kopf.querySelectorAll('.kopf__bild'));
    var takt = kopf.querySelector('.kopf__takt i');
    if(bilder.length > 1 && !reduce){
      var n = 0, dauer = 5200;
      setInterval(function(){
        bilder[n].removeAttribute('data-aktiv');
        n = (n + 1) % bilder.length;
        bilder[n].setAttribute('data-aktiv','true');
        if(takt) takt.style.transform = 'scaleX(' + ((n + 1) / bilder.length) + ')';
      }, dauer);
      if(takt) takt.style.transform = 'scaleX(' + (1 / bilder.length) + ')';
    } else if(takt){
      takt.style.transform = 'scaleX(1)';
    }
  }

  /* ---------- Bildstreifen: Parallaxe ---------- */
  var streifen = [].slice.call(document.querySelectorAll('.streifen'));
  if(streifen.length && !reduce){
    var laeuft = false;
    var zeichnen = function(){
      laeuft = false;
      var vh = innerHeight;
      streifen.forEach(function(s){
        var r = s.getBoundingClientRect();
        if(r.bottom < -200 || r.top > vh + 200) return;
        var t = (r.top + r.height / 2 - vh / 2) / vh;
        var img = s.querySelector('img');
        if(img) img.style.transform = 'translate3d(0,' + (t * -60).toFixed(1) + 'px,0)';
      });
    };
    addEventListener('scroll', function(){
      if(!laeuft){ laeuft = true; requestAnimationFrame(zeichnen); }
    }, {passive:true});
    addEventListener('resize', zeichnen);
    zeichnen();
  }

  /* ---------- Menue ---------- */
  var burger = document.getElementById('burger'),
      drawer = document.getElementById('drawer');
  if(burger && drawer){
    var auf = function(offen){
      drawer.setAttribute('data-open', offen ? 'true' : 'false');
      burger.setAttribute('aria-expanded', offen ? 'true' : 'false');
      burger.setAttribute('aria-label', offen ? 'Menü schließen' : 'Menü öffnen');
      document.body.style.overflow = offen ? 'hidden' : '';
    };
    burger.addEventListener('click', function(){
      auf(drawer.getAttribute('data-open') !== 'true');
    });
    drawer.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){ auf(false); });
    });
    addEventListener('keydown', function(e){ if(e.key === 'Escape') auf(false); });
  }

  /* ---------- Waagerechte Leisten ---------- */
  document.querySelectorAll('[data-leiste]').forEach(function(wrap){
    var rail = wrap.querySelector('.rail'),
        fill = wrap.querySelector('.rail__fill'),
        vor  = wrap.querySelector('[data-vor]'),
        zur  = wrap.querySelector('[data-zurueck]');
    if(!rail) return;

    var stand = function(){
      var max = rail.scrollWidth - rail.clientWidth;
      var p = max > 4 ? rail.scrollLeft / max : 1;
      if(fill) fill.style.transform = 'scaleX(' + Math.max(rail.clientWidth / rail.scrollWidth, p) + ')';
      /* Die Blende sitzt nur dort, wo es wirklich weitergeht. */
      rail.style.setProperty('--blende-l', rail.scrollLeft > 4 ? '4rem' : '0px');
      rail.style.setProperty('--blende-r', rail.scrollLeft < max - 4 ? '4rem' : '0px');
      if(zur) zur.disabled = rail.scrollLeft <= 4;
      if(vor) vor.disabled = rail.scrollLeft >= max - 4;
    };
    var schritt = function(richtung){
      var karte = rail.firstElementChild;
      var breite = karte ? karte.getBoundingClientRect().width : rail.clientWidth * 0.8;
      rail.scrollBy({left: richtung * breite, behavior: reduce ? 'auto' : 'smooth'});
    };
    if(vor) vor.addEventListener('click', function(){ schritt(1); });
    if(zur) zur.addEventListener('click', function(){ schritt(-1); });
    rail.addEventListener('scroll', stand, {passive:true});
    addEventListener('resize', stand);
    stand();

    /* Ziehen mit der Maus; Finger und Trackpad wischen ohnehin nativ. */
    var unten = false, startX = 0, startL = 0, weg = 0;
    rail.addEventListener('pointerdown', function(e){
      if(e.pointerType !== 'mouse') return;
      unten = true; weg = 0; startX = e.clientX; startL = rail.scrollLeft;
    });
    rail.addEventListener('pointermove', function(e){
      if(!unten) return;
      var dx = e.clientX - startX;
      weg = Math.max(weg, Math.abs(dx));
      rail.scrollLeft = startL - dx;
    });
    /* Nach echtem Ziehen den folgenden Klick schlucken, sonst loest die Karte
       unter dem Zeiger beim Loslassen aus. */
    rail.addEventListener('click', function(e){
      if(weg > 6){ e.stopPropagation(); e.preventDefault(); weg = 0; }
    }, true);
    ['pointerup','pointerleave','pointercancel'].forEach(function(ev){
      rail.addEventListener(ev, function(){ unten = false; });
    });
  });

  /* ---------- Terminbuchung ---------- */
  /* Einziger Einstiegspunkt. DocMedico oeffnet ueber ?dmropen=1; fuer eine
     programm-spezifische Buchung nur diese Funktion ersetzen. */
  window.nutBooking = window.nutBooking || { open: function(programm){ location.href = '?dmropen=1'; } };
  document.querySelectorAll('[data-programm]').forEach(function(b){
    b.addEventListener('click', function(){ window.nutBooking.open(b.dataset.programm); });
  });

  /* ---------- Karte ---------- */
  /* Die Karte laedt erst auf Klick. Ein eingebettetes Google Maps uebertraegt die
     IP-Adresse an Google, bevor die Besucherin irgendetwas entschieden hat. */
  var karteLaden = document.getElementById('karteLaden');
  if(karteLaden){
    karteLaden.addEventListener('click', function(){
      var f = document.createElement('iframe');
      f.title = 'Google Maps Karte: Weseler Straße 71, Münster';
      f.src = 'https://www.google.com/maps?q=Weseler+Stra%C3%9Fe+71,+48151+M%C3%BCnster&output=embed';
      f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade';
      f.allowFullscreen = true;
      karteLaden.replaceWith(f);
    });
  }

  var jahr = document.getElementById('y');
  if(jahr) jahr.textContent = new Date().getFullYear();
})();
