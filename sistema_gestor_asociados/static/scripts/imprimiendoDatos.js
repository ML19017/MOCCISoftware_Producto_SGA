
//Variables
var nombre = "";
var id = "";
var apellido ="";
var fecha_nacimiento = "";
var nacionalidad = "";

//Variables de impresion

var nombre_impresion = "";
var id_impresion = "";
var apellido_impresion ="";
var fecha_nacimiento_impresion = "";
var nacionalidad_impresion ="";

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
if(localStorage.getItem("nacionalidad")){
    nacionalidad = localStorage.getItem("nacionalidad");
    console.log(nacionalidad);
}

//Cambiando los label para imprimir

id_impresion = document.getElementById("id").innerHTML = id;
nombre_impresion = document.getElementById("nombre").innerHTML = nombre;
apellido_impresion = document.getElementById("apellido").innerHTML = apellido;
fecha_nacimiento_impresion = document.getElementById("fecha_nacimiento").innerHTML = fecha_nacimiento;
id_impresion = document.getElementById("id").innerHTML = id;
nacionalidad_impresion = document.getElementById("nacionalidad").innerHTML = nacionalidad;


