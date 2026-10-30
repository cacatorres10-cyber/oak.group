// Coverflow photo carousel for the service pages (same as the home page "Recent Work" one).
// Slides come from window.CF_SLIDES = [{src, title, sub}].
(function(){
  var SLIDES = window.CF_SLIDES || [];
  if(!SLIDES.length || !document.getElementById('cfStage')) return;

  var stage = document.getElementById('cfStage');
  var frame = document.getElementById('cfFrame');
  var titleEl = document.getElementById('cfTitle');
  var subEl = document.getElementById('cfSub');
  var dotsWrap = document.getElementById('cfDots');
  var count = SLIDES.length;

  var cards = SLIDES.map(function(slide){
    var card = document.createElement('div');
    card.className = 'cf-card';
    var img = document.createElement('img');
    img.src = slide.src; img.alt = slide.title; img.draggable = false; img.loading = 'lazy'; img.decoding = 'async';
    card.appendChild(img);
    stage.appendChild(card);
    return card;
  });

  SLIDES.forEach(function(_, i){
    var dot = document.createElement('button');
    dot.setAttribute('aria-label', 'Go to slide '+(i+1));
    dot.addEventListener('click', function(){ goTo(i); });
    dotsWrap.appendChild(dot);
  });
  var dots = Array.prototype.slice.call(dotsWrap.children);

  var pos = 0, target = 0, rafId = null, cardWidth = 0, selected = 0;

  function indexAt(p){ return ((Math.round(p) % count) + count) % count; }

  function paint(){
    if(!cardWidth) return;
    var gap = 0.12;
    var pitch = cardWidth * (1+gap);
    cards.forEach(function(card, i){
      var offset = i - pos;
      offset = ((offset % count) + count) % count;
      if(offset > count/2) offset -= count;
      var distance = Math.abs(offset);
      var ramp = Math.pow(distance, 0.58);
      var tilt = Math.min(46*ramp, 80) * Math.sign(offset);
      card.style.transform = 'translateX(calc(-50% + '+(offset*pitch)+'px)) translateZ('+(-0.62*cardWidth*ramp)+'px) rotateY('+(-tilt)+'deg)';
      var edge = Math.min(1, Math.max(0, count/2 - distance));
      card.style.opacity = String(Math.max(0, 1 - 0.12*distance) * edge);
      card.style.zIndex = String(100 - Math.round(distance));
    });
  }

  function updateCaption(){
    var s = SLIDES[selected];
    titleEl.textContent = s.title;
    subEl.textContent = s.sub;
    dots.forEach(function(d,i){ d.setAttribute('aria-current', i===selected ? 'true':'false'); });
  }

  function settle(t){
    if(rafId) cancelAnimationFrame(rafId);
    target = t;
    selected = indexAt(t);
    updateCaption();
    function step(){
      var remaining = target - pos;
      if(Math.abs(remaining) < 0.0006){ pos = target; paint(); rafId=null; return; }
      pos += remaining * 0.16;
      paint();
      rafId = requestAnimationFrame(step);
    }
    rafId = requestAnimationFrame(step);
  }

  function goTo(i){
    var t = i + Math.round((target - i)/count)*count;
    settle(t);
  }
  function nudge(by){ settle(Math.round(target)+by); }

  function measure(){
    cardWidth = cards[0].offsetWidth;
    paint();
  }
  if('ResizeObserver' in window){
    new ResizeObserver(measure).observe(frame);
  } else {
    window.addEventListener('resize', measure);
  }
  measure();
  updateCaption();

  document.getElementById('cfPrev').addEventListener('click', function(){ nudge(-1); });
  document.getElementById('cfNext').addEventListener('click', function(){ nudge(1); });
  frame.addEventListener('keydown', function(e){
    if(e.key === 'ArrowLeft'){ e.preventDefault(); nudge(-1); }
    if(e.key === 'ArrowRight'){ e.preventDefault(); nudge(1); }
  });

  var drag = null;
  frame.addEventListener('pointerdown', function(e){
    if(rafId) cancelAnimationFrame(rafId);
    frame.setPointerCapture(e.pointerId);
    drag = {id:e.pointerId, x:e.clientX, pos:pos};
    target = pos;
  });
  frame.addEventListener('pointermove', function(e){
    if(!drag || drag.id !== e.pointerId) return;
    var pitch = cardWidth * 1.12;
    if(!pitch) return;
    pos = drag.pos - (e.clientX - drag.x)/pitch;
    var idx = indexAt(pos);
    if(idx !== selected){ selected = idx; updateCaption(); }
    paint();
  });
  function endDrag(e){
    if(!drag || drag.id !== e.pointerId) return;
    drag = null;
    settle(Math.round(pos));
  }
  frame.addEventListener('pointerup', endDrag);
  frame.addEventListener('pointercancel', endDrag);

  // Moves on by itself every few seconds until the visitor touches it
  if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    var auto = setInterval(function(){ if(!drag) nudge(1); }, 4000);
    ['pointerdown','keydown'].forEach(function(ev){ frame.addEventListener(ev, function(){ clearInterval(auto); }); });
    ['cfPrev','cfNext'].forEach(function(id){ document.getElementById(id).addEventListener('click', function(){ clearInterval(auto); }); });
    dots.forEach(function(d){ d.addEventListener('click', function(){ clearInterval(auto); }); });
  }
})();
