
function eliminar() {
	changeAction("form_usuarios", "/sistema_gestor_asociados/administracion/eliminar");
}

function crear() {
	changeAction("form_usuarios", "/sistema_gestor_asociados/registro/");
}

function getInfo(element) {
	var currentRow = element.closest('tr');
	document.getElementsByClassName('info_id')[0].innerHTML = currentRow.getElementsByClassName('id')[0].innerHTML;
	document.getElementsByClassName('info_username')[0].innerHTML = currentRow.getElementsByClassName('username')[0].innerHTML;
	document.getElementsByClassName('info_email')[0].innerHTML = currentRow.getElementsByClassName('email')[0].innerHTML;
}

function changeAction(form_class_name, action) {
	const form = document.getElementsByClassName(form_class_name)[0];
	form.method = 'post';
	form.action = action;
	form.submit();
}

function _init_() {
	document.getElementById('usuarios').style.display = "block";
	document.getElementById('button_usuarios').setAttribute('class', 'tablinks active');
	const element = document.getElementById('radio_id');
	getInfo(element);
	element.setAttribute('checked', true);
}