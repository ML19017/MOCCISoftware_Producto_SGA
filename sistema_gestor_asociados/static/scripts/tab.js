function abrirTab(evt, tabName) {
  // Declaracion de variables
  var i, tabcontent, tablinks;

  // Toma todos los elementos que tengan class="tabcontent" y los oculta
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Toma todos los elementos que tengan class="tablinks" y remueve class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Muestra la tab actual, y añade "active" class al boton cuando la tab esta abierta
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}