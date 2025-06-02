document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("theme-toggle");
  const htmlElement = document.documentElement;

  // Leer el tema guardado
  const savedTheme = localStorage.getItem("theme");

  // Establecer el tema si estaba guardado
  if (savedTheme) {
    htmlElement.setAttribute("data-bs-theme", savedTheme);
    updateButton(savedTheme);
  }

  // Cambiar tema al hacer clic
  toggleBtn.addEventListener("click", function () {
    const currentTheme = htmlElement.getAttribute("data-bs-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    htmlElement.setAttribute("data-bs-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateButton(newTheme);
  });

  // Actualizar el texto y estilo del botón
  function updateButton(theme) {
    if (theme === "dark") {
      toggleBtn.innerHTML = '🌙';
    } else {
      toggleBtn.innerHTML = '☀️';
    }
  }

  // Mostrar los mensajes Toast con autohide y delay de 7 segundos
  const toastElList = [].slice.call(document.querySelectorAll('.toast'));
  toastElList.forEach(toastEl => {
    const toast = new bootstrap.Toast(toastEl, {
      autohide: true,
      delay: 7000
    });
    toast.show();
  });
});