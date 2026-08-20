(function () {
  if (document.querySelector('.wa-float')) return;

  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.href = 'assets/css/whatsapp-float.css';
  document.head.appendChild(link);

  var a = document.createElement('a');
  a.className = 'wa-float';
  a.href = 'https://wa.me/254111224952?text=' + encodeURIComponent('Hi Stephen, I found your portfolio and would like to chat.');
  a.target = '_blank';
  a.rel = 'noopener noreferrer';
  a.setAttribute('aria-label', 'Chat on WhatsApp');
  a.title = 'Chat on WhatsApp';
  a.innerHTML = '<i class="bi bi-whatsapp" aria-hidden="true"></i>';
  document.body.appendChild(a);
})();
