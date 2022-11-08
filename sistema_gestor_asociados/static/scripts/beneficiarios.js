/* 
    Calcular Porcentaje
*/

let porcentaje_disponible = 0;

function calcularRestante() {
    const beneficiarios = document.getElementsByClassName("item_beneficiario");
    var restante = 100;

    if(beneficiarios != null) {
        for(var i = 0; i < beneficiarios.length; i++) {
            restante -= parseInt(beneficiarios[i].getElementsByClassName("porcentaje")[0].innerHTML); 
        }
    }
    porcentaje_disponible = restante;
}

function updateParentescos() {
    const select_parentesco = document.getElementById("id_parentesco");
    const beneficiarios = document.getElementsByClassName("item_beneficiario");
    const parentescos = select_parentesco.getElementsByTagName("option");
    var beneficiario = null;

    if(beneficiarios != null) {
        for(var i = 0; i < beneficiarios.length; i++) {
            beneficiario = beneficiarios[i].getElementsByClassName("parentesco")[0];
            if(beneficiario.innerHTML === 'Madre' || beneficiario.innerHTML === "Padre" || beneficiario.innerHTML === "Esposo/a") {
                for(var e = 0; e < parentescos.length; e++) {
                    if(parentescos[e].value == toParentesco(beneficiario.innerHTML))
                        select_parentesco.removeChild(parentescos[e]);
                }
            }
        }
    }
}

function resetForm() {
    const nombres = document.getElementById("id_nombres");
    const apellidos = document.getElementById("id_apellidos");
    const fecha = document.getElementById("id_fecha_nacimiento");
    const porcentaje = document.getElementById("id_porcentaje");

    nombres.value = "";
    apellidos.value = "";
    fecha.value = "";
    porcentaje.value = 1;
}

function validarPorcentaje(value) {
    if(value <= porcentaje_disponible) {
        return true;
    }
    else {
        return false;
    }
}

// Calcular Edad
function calcularEdad() {
    var input = document.getElementById("id_fecha_nacimiento");
    var fecha = new Date(input.value);
    var hoy = new Date();
    var fecha_nacimiento = new Date(fecha);
    var edad = hoy.getFullYear() - fecha_nacimiento.getFullYear();
    var m = hoy.getMonth() - fecha_nacimiento.getMonth();
  
    if (m < 0 || (m === 0 && hoy.getDate() < fecha_nacimiento.getDate())) {
        edad--;
    }
    return edad;
}

function getParentesco(id) {
    const select_parentesco = document.getElementById("id_parentesco");
    const parentescos = select_parentesco.getElementsByTagName("option");

    for(var i = 0; i < parentescos.length; i++) {
        if(parentescos[i].value == id)
            return parentescos[i].innerHTML;
    }
    return id;
}

function removeParentesco(id) {
    const select_parentesco = document.getElementById("id_parentesco");
    const parentescos = select_parentesco.getElementsByTagName("option");

    for(var e = 0; e < parentescos.length; e++) {
        if(parentescos[e].value == id)
            select_parentesco.removeChild(parentescos[e]);
    }
}

function eliminar(boton) {
    const tabla = document.getElementById("id_tabla_beneficiarios");
    const tabla_body = tabla.getElementsByTagName("tbody")[0];
    const select_parentesco = document.getElementById("id_parentesco");
    var currentRow = boton.closest("tr");
    var parentesco = currentRow.getElementsByClassName("parentesco")[0];

    if(parentesco.innerHTML === 'Madre') {
        var option = document.createElement("option");
        option.setAttribute("value", 1);
        option.innerHTML = parentesco.innerHTML;
        select_parentesco.appendChild(option);
    }
    if(parentesco.innerHTML === "Padre") {
        var option = document.createElement("option");
        option.setAttribute("value", 2);
        option.innerHTML = parentesco.innerHTML;
        select_parentesco.appendChild(option);
    }
    if(parentesco.innerHTML === "Esposo/a") {
        var option = document.createElement("option");
        option.setAttribute("value", 5);
        option.innerHTML = parentesco.innerHTML;
        select_parentesco.appendChild(option);
    }
    tabla_body.removeChild(currentRow);
    calcularRestante();
}

function agregarBeneficiario() {
    const porcentaje = document.getElementById("id_porcentaje");
            
    if(validarPorcentaje(porcentaje.value)) {
        if(validarForm()) {
            const parentesco = document.getElementById("id_parentesco");
            const tabla = document.getElementById("id_tabla_beneficiarios");
            const tabla_body = tabla.getElementsByTagName("tbody");
            const nombres = document.getElementById("id_nombres");
            const apellidos = document.getElementById("id_apellidos");
            const edad = calcularEdad();
            var row = document.createElement("tr");
            row.setAttribute('class','item_beneficiario' );
            row.innerHTML = "<td class='action'><button type='button' onclick='eliminar(this)'>Eliminar</button></td>"
                +"<td class='nombres'>" + nombres.value + "</td>"
                +"<td class='apellidos'>" + apellidos.value + "</td>"
                +"<td class='edad'>" + edad + "</td>"
                +"<td class='parentesco'>" + getParentesco(parentesco.value) + "</td>"
                +"<td class='porcentaje'>" + porcentaje.value + "</td>";
            tabla_body[0].appendChild(row);
            if(validarParentesco(parentesco.value))
                removeParentesco(parentesco.value);
            calcularRestante();
            resetForm();
        }
    }
    else {
        alert("El porcentaje introducido para el beneficiario (ACTUAL), supera el porcentaje disponible!\n\nPorcentaje Disponible: " + 
            porcentaje_disponible + "%\n\nConsidere suprimir y reasignar porcentajes!");
    }
}

function validarParentesco(parentesco) {
    if(parentesco == 1 || parentesco == 2 || parentesco == 5)
        return true;
    return false;
}

function validarForm() {
    const form = document.getElementById("form_beneficiarios");
    return form.checkValidity();
}

function enviarBeneficiarios() {
    var beneficiarios = document.getElementsByClassName("item_beneficiario");
    const csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    const id = document.getElementById("info_id").innerHTML;
    
    if(beneficiarios[0] != null) {
        
        var data = [];

        for (var i = 0; i < beneficiarios.length; i++) { 
            var tableRow = beneficiarios[i].getElementsByTagName("td");
            var rowData = [];
            for (var j=1; j<tableRow.length; j++) {
                if(tableRow[j].getAttribute("class") === "parentesco")
                    rowData.push(toParentesco(tableRow[j].innerHTML).toString());
                else
                    rowData.push(tableRow[j].innerHTML);
            } 
            data.push(rowData); 
        }
        console.log(JSON.stringify(data) + csrfmiddlewaretoken);
        
        fetch("/sistema_gestor_asociados/escritorio/beneficiarios/",
        {
            headers: {
                'X-CSRFToken': csrfmiddlewaretoken,
                'Accept': 'application/json',
                'Content-type': 'application/json; charset=UTF-8',
            },
            method:"post", 
            body: JSON.stringify({'id': id,'data':data})
        });
    }
    else {
        alert("Por favor ingrese un beneficiario!");
    }
}

function _init_() {
    calcularRestante();
    updateParentescos();
}