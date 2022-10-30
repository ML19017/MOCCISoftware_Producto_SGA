function calcularPago(){
    //Datos del formulario
    const PORCENTAJEPARAUNIRSE = 0.16;
    var sueldo = document.getElementById("IngresosSolicitante").value;
    var porcentaje = document.getElementById("porcentajeAhorro").value;
    var mostrarCantidadAhorro = document.getElementById("CantidadAhorro");
    var imprimirCostoParaUnirse = document.getElementById("CostoParaUnirse");
    var imprimirCostoTotal = document.getElementById("CostoTotal");
    //Variables de operacion
    var cantidadAhorro = "";
    var costoParaUnirse = "";
    var costoTotal = "";
    //Operaciones
    if(sueldo > 0){
        cantidadAhorro = Math.round(sueldo * porcentaje);
        costoParaUnirse = Math.round(sueldo * PORCENTAJEPARAUNIRSE);
        costoTotal = cantidadAhorro + costoParaUnirse;
    }else{
        alert("Ingrese una cantidad valida")
    }
    //Impresion del resultado de las operaciones en el html
    mostrarCantidadAhorro.innerHTML = "$" + cantidadAhorro; 
    imprimirCostoParaUnirse.innerHTML = "$" + costoParaUnirse;
    imprimirCostoTotal.innerHTML = "$" + costoTotal;
}