// Datos de Genero
function selectGenero() {
  const genero = document.getElementById("id_genero");
  const form_apellido_casada = document.getElementById("form_apellido_casada");
  const apellido_casada = document.getElementById("id_apellido_casada");
  const estado_familiar = document.getElementById("id_estado_familiar");

  if(genero.value == 1 && estado_familiar.value == 2) {
    form_apellido_casada.style.display = "inline-flex";
  }
  else {
    apellido_casada.style.value = "";
    form_apellido_casada.style.display = "none";
  }
}

function selectPaisNacimiento() {
  const pais_nacimiento = document.getElementById("id_pais_nacimiento");
  const match_nacionalidad = document.getElementById("id_match_nacionalidad");
  const form_documentos_obligatorios = document.getElementById("form_documentos_obligatorios");

  if(pais_nacimiento.value == match_nacionalidad.value) {
    form_documentos_obligatorios.style.display = "inline-flex";
    document.getElementById("id_isss").required = true;
    document.getElementById("id_nit").required = true;
    document.getElementById("id_nup").required = true;
  }
  else {
    form_documentos_obligatorios.style.display = "none";
    document.getElementById("id_isss").removeAttribute("required");
    document.getElementById("id_nit").removeAttribute("required");
    document.getElementById("id_nup").removeAttribute("required");
  }
}

// Datos de Estado Civil
function selectEstadoCivil() {
  const estado_familiar = document.getElementById("id_estado_familiar");
  const form_datos_conyuge = document.getElementById("form_datos_conyuge");

  if(estado_familiar.value == 2) {
    form_datos_conyuge.style.display = "inline-flex";
    document.getElementById("id_nombres_conyuge").required = true;
    document.getElementById("id_apellidos_conyuge").required = true;
    document.getElementById("id_fecha_nacimiento_conyuge").required = true;
    document.getElementById("id_empresa").required = true;
    document.getElementById("id_cargo").required = true;
    document.getElementById("id_nacionalidad_conyuge").required = true;
    document.getElementById("id_tipo_documento_conyuge").required = true;
    document.getElementById("id_numero_documento_conyuge").required = true;
    document.getElementById("id_telefono_personal_conyuge").required = true;
    document.getElementById("id_telefono_oficina_conyuge").required = true;
    document.getElementById("id_correo").required = true;
    selectGenero();
  }
  else {
    form_datos_conyuge.style.display = "none";
    document.getElementById("id_nombres_conyuge").removeAttribute("required");
    document.getElementById("id_apellidos_conyuge").removeAttribute("required");
    document.getElementById("id_fecha_nacimiento_conyuge").removeAttribute("required");
    document.getElementById("id_empresa").removeAttribute("required");
    document.getElementById("id_cargo").removeAttribute("required");
    document.getElementById("id_nacionalidad_conyuge").removeAttribute("required");
    document.getElementById("id_tipo_documento_conyuge").removeAttribute("required");
    document.getElementById("id_numero_documento_conyuge").removeAttribute("required");
    document.getElementById("id_telefono_personal_conyuge").removeAttribute("required");
    document.getElementById("id_telefono_oficina_conyuge").removeAttribute("required");
    document.getElementById("id_correo").removeAttribute("required");
    selectGenero();
  }
}

// Datos de Tipo de Trabajador
function selectTipoTrabajador() {
  const tipo_trabajador = document.getElementById("id_tipo_trabajador");
  const form_referencias = document.getElementById("form_referencias");
  const form_rubro = document.getElementById("form_rubro");

  if(tipo_trabajador.value == 2 || tipo_trabajador.value == 3) {
    form_rubro.style.display = "inline-flex";
    form_referencias.style.display = "inline-flex";
    document.getElementById("id_rubro").required = true;
    document.getElementById("id_nombre_primera_referencia_personal").required = true;
    document.getElementById("id_telefono_primera_referencia_personal").required = true;
    document.getElementById("id_correo_primera_referencia_personal").required = true;
    document.getElementById("id_nombre_segunda_referencia_personal").required = true;
    document.getElementById("id_telefono_segunda_referencia_personal").required = true;
    document.getElementById("id_correo_segunda_referencia_personal").required = true;
    document.getElementById("id_nombre_primera_referencia_familiar").required = true;
    document.getElementById("id_telefono_primera_referencia_familiar").required = true;
    document.getElementById("id_correo_primera_referencia_familiar").required = true;
    document.getElementById("id_nombre_segunda_referencia_familiar").required = true;
    document.getElementById("id_telefono_segunda_referencia_familiar").required = true;
    document.getElementById("id_correo_segunda_referencia_familiar").required = true;
  }
  else {
    form_rubro.style.display = "none";
    form_referencias.style.display = "none";
    document.getElementById("id_nombre_primera_referencia_personal").removeAttribute("required");
    document.getElementById("id_nombre_primera_referencia_personal").removeAttribute("required");
    document.getElementById("id_telefono_primera_referencia_personal").removeAttribute("required");
    document.getElementById("id_correo_primera_referencia_personal").removeAttribute("required");
    document.getElementById("id_nombre_segunda_referencia_personal").removeAttribute("required");
    document.getElementById("id_telefono_segunda_referencia_personal").removeAttribute("required");
    document.getElementById("id_correo_segunda_referencia_personal").removeAttribute("required");
    document.getElementById("id_nombre_primera_referencia_familiar").removeAttribute("required");
    document.getElementById("id_telefono_primera_referencia_familiar").removeAttribute("required");
    document.getElementById("id_correo_primera_referencia_familiar").removeAttribute("required");
    document.getElementById("id_nombre_segunda_referencia_familiar").removeAttribute("required");
    document.getElementById("id_telefono_segunda_referencia_familiar").removeAttribute("required");
    document.getElementById("id_correo_segunda_referencia_familiar").removeAttribute("required");
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

  if(edad < 16) {
    input.value = "";
    alert("No se cumplen los requisitos de edad: " + edad + " años.\nDebes ser mayor de 16 años.");
  }
}

function hideForms() {
  // Tomando los datos por IDs
  const form_datos_conyuge = document.getElementById("form_datos_conyuge");
  const form_apellido_casada = document.getElementById("form_apellido_casada");
  const form_documentos_obligatorios = document.getElementById("form_documentos_obligatorios");
  const form_referencias = document.getElementById("form_referencias");
  const form_rubro = document.getElementById("form_rubro");
  // Ocultando los formularios al inicio
  form_datos_conyuge.style.display = "none";
  form_apellido_casada.style.display = "none";
  form_documentos_obligatorios.style.display = "none";
  form_referencias.style.display = "none";
  form_rubro.style.display = "none";
}

// Init onload
function _init_() {
  const phoneInputsField = document.querySelectorAll('input[type="tel"]');
  for(var i = 0; i < phoneInputsField.length; i++) {
    const phoneInput = window.intlTelInput(phoneInputsField[i], {utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    phoneInputsField[i].className = "input";
	}
  clearFocus();
  hideForms();
}

function clearFocus() {
  document.getElementById("id_apellido_casada").removeAttribute("required");
  document.getElementById("id_nombre_primera_referencia_personal").removeAttribute("required");
  document.getElementById("id_nombre_primera_referencia_personal").removeAttribute("required");
  document.getElementById("id_telefono_primera_referencia_personal").removeAttribute("required");
  document.getElementById("id_correo_primera_referencia_personal").removeAttribute("required");
  document.getElementById("id_nombre_segunda_referencia_personal").removeAttribute("required");
  document.getElementById("id_telefono_segunda_referencia_personal").removeAttribute("required");
  document.getElementById("id_correo_segunda_referencia_personal").removeAttribute("required");
  document.getElementById("id_nombre_primera_referencia_familiar").removeAttribute("required");
  document.getElementById("id_telefono_primera_referencia_familiar").removeAttribute("required");
  document.getElementById("id_correo_primera_referencia_familiar").removeAttribute("required");
  document.getElementById("id_nombre_segunda_referencia_familiar").removeAttribute("required");
  document.getElementById("id_telefono_segunda_referencia_familiar").removeAttribute("required");
  document.getElementById("id_correo_segunda_referencia_familiar").removeAttribute("required");
  document.getElementById("id_nombres_conyuge").removeAttribute("required");
  document.getElementById("id_apellidos_conyuge").removeAttribute("required");
  document.getElementById("id_fecha_nacimiento_conyuge").removeAttribute("required");
  document.getElementById("id_empresa").removeAttribute("required");
  document.getElementById("id_cargo").removeAttribute("required");
  document.getElementById("id_nacionalidad_conyuge").removeAttribute("required");
  document.getElementById("id_tipo_documento_conyuge").removeAttribute("required");
  document.getElementById("id_numero_documento_conyuge").removeAttribute("required");
  document.getElementById("id_telefono_personal_conyuge").removeAttribute("required");
  document.getElementById("id_telefono_oficina_conyuge").removeAttribute("required");
  document.getElementById("id_correo").removeAttribute("required");
  document.getElementById("id_isss").removeAttribute("required");
  document.getElementById("id_nit").removeAttribute("required");
  document.getElementById("id_nup").removeAttribute("required");
}