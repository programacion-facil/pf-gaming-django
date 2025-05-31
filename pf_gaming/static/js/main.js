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
      toggleBtn.innerHTML = '<i class="fas fa-moon me-2"></i>Modo Oscuro';
      toggleBtn.classList.remove("btn-outline-dark");
      toggleBtn.classList.add("btn-outline-light");
    } else {
      toggleBtn.innerHTML = '<i class="fas fa-sun me-2"></i>Modo Claro';
      toggleBtn.classList.remove("btn-outline-light");
      toggleBtn.classList.add("btn-outline-dark");
    }
  }
});