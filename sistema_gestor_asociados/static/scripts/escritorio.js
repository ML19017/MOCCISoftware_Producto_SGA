/* Script de control de escritorio */

function beneficiarios() {
	changeAction("form_solicitudes", "/sistema_gestor_asociados/escritorio/beneficiarios/");
}

function generarDocumentos() {
	changeAction("form_solicitudes","/sistema_gestor_asociados/escritorio/hojaLegal/");
}

function generarRecibo() {
	changeAction("form_solicitudes", "/sistema_gestor_asociados/escritorio/generar_recibo/");
}

function anexarDocumentos() {
	changeAction("form_solicitudes", "/sistema_gestor_asociados/escritorio/anexo_documentacion/");
}

function aprobar() {
	changeAction("form_solicitudes", "/sistema_gestor_asociados/escritorio/aprobar_solicitud/");
}
function carnet() {
	changeAction("form_solicitudes", "/sistema_gestor_asociados/escritorio/carnet/");
}

function getInfo(element) {
	var currentRow = element.closest('tr');
	document.getElementsByClassName('info_id')[0].innerHTML = currentRow.getElementsByClassName('id')[0].innerHTML;
	document.getElementsByClassName('info_nombres')[0].innerHTML = currentRow.getElementsByClassName('nombres')[0].innerHTML;
	document.getElementsByClassName('info_apellidos')[0].innerHTML = currentRow.getElementsByClassName('apellidos')[0].innerHTML;
	document.getElementsByClassName('info_fecha')[0].innerHTML = currentRow.getElementsByClassName('fecha_nacimiento')[0].innerHTML;
	document.getElementsByClassName('info_pais')[0].innerHTML = currentRow.getElementsByClassName('nacionalidad')[0].innerHTML;
}

function changeAction(form_class_name, action) {
	const form = document.getElementsByClassName(form_class_name)[0];
	form.method = 'get';
	form.action = action;
	form.submit();
}

function _init_() {
	document.getElementById('solicitudes').style.display = "block";
	document.getElementById('button_solicitudes').setAttribute('class', 'tablinks active');
	const element = document.getElementById('radio_id');
	getInfo(element);
	element.setAttribute('checked', true);
}