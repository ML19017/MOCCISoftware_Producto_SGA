//Variables
var nombre = "";
var id = "";
var apellido ="";
var fecha_nacimiento = "";

//Variables de impresion

var nombre_impresion = "";
var id_impresion = "";
var apellido_impresion ="";
var fecha_nacimiento_impresion = "";

//recuperando memoria de storage

if(localStorage.getItem("id")){
    id = localStorage.getItem("id");
    console.log(id);
}
if(localStorage.getItem("nombres")){
    nombre = localStorage.getItem("nombres");
    console.log(nombre);
}
if(localStorage.getItem("apellidos")){
    apellido = localStorage.getItem("apellidos");
    console.log(apellido);
}
if(localStorage.getItem("fechaNacimiento")){
    fecha_nacimiento = localStorage.getItem("fechaNacimiento");
    console.log(fecha_nacimiento);
}

//Cambiando los label para imprimir

id_impresion = document.getElementById("id").innerHTML = id;
nombre_impresion = document.getElementById("nombre").innerHTML = nombre;
apellido_impresion = document.getElementById("apellido").innerHTML = apellido;
fecha_nacimiento_impresion = document.getElementById("fecha_nacimiento").innerHTML = fecha_nacimiento;


