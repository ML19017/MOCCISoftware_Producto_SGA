var boton = document.getElementById("carnetBoton");
boton.addEventListener("click",Crearcarnet,false);

var boton2 = document.getElementById("DocumentoBoton");
boton2.addEventListener("click",Crearcarnet,false);

//Obteniendo datos a traves de IDs


function Crearcarnet(){

    //Dato del ID
    var id = document.getElementById("info_id");
    var idValor = parseInt(id.innerHTML);

    //Dato del Nombre
    var nombre = document.getElementById("info_nombres").innerText;

    //Dato del Apellido
    var apellido = document.getElementById("info_apellidos").innerText;

    //Dato de la Fecha de Nacimiento
    var fechaNacimiento = document.getElementById("info_fecha").innerText;

    //Dato de nacionalidad
    var nacionalidad = document.getElementById("info_pais").innerHTML;
    //Prueba en la consola

    console.log(idValor);
    console.log(nombre);
    console.log(apellido)
    console.log(fechaNacimiento);
    console.log(nacionalidad);

    //Guardando Datos en Local Storage
    localStorage.setItem("id", idValor);
    localStorage.setItem("nombres", nombre);
    localStorage.setItem("apellidos", apellido);
    localStorage.setItem("fechaNacimiento", fechaNacimiento);
    localStorage.setItem("nacionalidad", nacionalidad);
}