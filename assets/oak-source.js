// Where did this visitor come from? Remembered for 30 days so the quote message can say "I found you on Google".
(function(){
  var KEY = 'oak_src', src = '';
  try {
    var q = new URLSearchParams(window.location.search);
    var utm = (q.get('utm_source') || '').toLowerCase();
    if(q.get('gclid') || q.get('gbraid') || q.get('wbraid') || utm === 'google') src = 'google_ads';
    else if(/(^|\.)google\./.test((document.referrer.split('/')[2] || ''))) src = 'google';
    else if(utm) src = utm;
    var saved = JSON.parse(localStorage.getItem(KEY) || 'null');
    if(src){ localStorage.setItem(KEY, JSON.stringify({ s: src, t: Date.now() })); }
    else if(saved && Date.now() - saved.t < 30 * 864e5){ src = saved.s; }
  } catch(e){}
  window.OAK_SRC = src;
  window.oakFoundVia = function(){
    return (src === 'google' || src === 'google_ads') ? 'on Google' : 'on your website';
  };
  window.oakSourceLabel = function(){
    return { google_ads: 'Google (ad)', google: 'Google (search)' }[src] || (src ? src : 'Website');
  };
  // Google Ads conversions: WhatsApp, email and call clicks
  var CONV = {
    whatsapp: 'AW-18524409646/RoJhCOWW27EdEK6ekIFF',
    email:    'AW-18524409646/Z9vbCM6d27EdEK6ekIFF',
    call:     'AW-18524409646/jRY_CNGd27EdEK6ekIFF'
  };
  window.oakConv = function(kind){
    try { if(window.gtag && CONV[kind]) gtag('event', 'conversion', { send_to: CONV[kind], value: 1.0, currency: 'GBP' }); } catch(e){}
  };
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href]');
    if(!a) return;
    var h = a.getAttribute('href') || '';
    if(h.indexOf('https://wa.me/') === 0) window.oakConv('whatsapp');
    else if(h.indexOf('tel:') === 0) window.oakConv('call');
    else if(h.indexOf('mailto:') === 0 || /mail\.google\.com|outlook\.(live|office)\.com|mail\.yahoo\.com/.test(h)) window.oakConv('email');
  }, true);

  // Static WhatsApp links on the service pages
  function fixLinks(){
    if(window.oakFoundVia() === 'on your website') return;
    document.querySelectorAll('a[href^="https://wa.me/"]').forEach(function(a){
      a.href = a.href.replace('found%20you%20on%20your%20website', 'found%20you%20on%20Google');
    });
  }
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', fixLinks); else fixLinks();
})();
