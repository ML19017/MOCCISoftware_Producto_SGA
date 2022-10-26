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
    if(edad < 18) {
        alert("No se cumplen los requisitos de mayoria de edad: " + edad + " años.");
    }
    }
}

function configurarFechas() {
    var input = document.getElementById("fecha-nacimiento");
    var fechaMaxima = new Date();
    var fechaMinima = new Date(new Date().setFullYear(new Date().getFullYear() - 120));
    var min = fechaMinima.getFullYear() + "-" + (fechaMinima.getMonth() + 1) + "-" + fechaMinima.getDate();
    var max = fechaMaxima.getFullYear() + "-" + (fechaMaxima.getMonth() + 1) + "-" + fechaMaxima.getDate();
    input.setAttribute("min", min);
    input.setAttribute("max", max);
}