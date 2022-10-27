/*
    SCRIPT: calcula la edad del solicitante
*/
function calcularEdad() {
    var input = document.getElementById("fecha-nacimiento").value;
    var dob = new Date(input);
    if(input == null || input == '') {
      alert("Escoja una fecha por favor!");
      input.value = "";
      return false; 
    }
    else {
        var diferencia_meses = Date.now() - dob.getTime();
        var edad_dt = new Date(diferencia_meses); 
        var anio = edad_dt.getUTCFullYear();
        var edad = Math.abs(anio - 1970);
    if(edad < 16) {
        alert("No se cumplen los requisitos de edad: " + edad + " años.\nDebes ser mayor de 16 años.");
    }
    }
}