  document.addEventListener('contextmenu', function (e) {
    if (e.target.tagName === 'IMG') {
      e.preventDefault();
    }
  });

  document.getElementById('video').addEventListener('contextmenu', function(e) {
    e.preventDefault();
  });