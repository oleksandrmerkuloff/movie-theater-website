document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById('menuBtn');
  const sideMenu = document.getElementById('sideMenu');
  const closeBtn = document.getElementById('closeBtn');
  const overlay = document.getElementById('overlay');

  if (!menuBtn || !sideMenu) return; // safety check

  menuBtn.addEventListener('click', () => {
    sideMenu.classList.add('open');
    overlay.classList.add('show');
  });

  closeBtn.addEventListener('click', () => {
    sideMenu.classList.remove('open');
    overlay.classList.remove('show');
  });

  overlay.addEventListener('click', () => {
    sideMenu.classList.remove('open');
    overlay.classList.remove('show');
  });
});
