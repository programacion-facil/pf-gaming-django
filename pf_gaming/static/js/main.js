document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("theme-toggle");
  const htmlElement = document.documentElement;

  // Leer el tema guardado o usar el tema actual del HTML o default 'dark'
  const savedTheme = localStorage.getItem("theme");
  const initialTheme = savedTheme || htmlElement.getAttribute("data-bs-theme") || "dark";

  // Establecer el tema y actualizar el botón al cargar
  htmlElement.setAttribute("data-bs-theme", initialTheme);
  updateButton(initialTheme);

  // Cambiar tema al hacer clic
  toggleBtn.addEventListener("click", function () {
    const currentTheme = htmlElement.getAttribute("data-bs-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    htmlElement.setAttribute("data-bs-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateButton(newTheme);
  });

  // Actualizar el contenido del botón
  function updateButton(theme) {
    toggleBtn.innerHTML = theme === "dark" ?
      '<i class="fa-solid fa-moon icon-moon"></i>' :
      '<i class="fa-solid fa-sun icon-sun"></i>';
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