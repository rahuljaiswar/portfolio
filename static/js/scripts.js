  document.addEventListener('contextmenu', function (e) {
    if (e.target.tagName === 'IMG', 'video') {
      e.preventDefault();
    }
  });

  