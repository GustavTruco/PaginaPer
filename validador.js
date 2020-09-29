/**
 * Imprime error
 * @param {string|number} msg
 */
function mostrarError(msg) {

    let contenedor = document.getElementById('error');

    contenedor.innerHTML = msg;
    contenedor.style.display = 'block';
    contenedor.style.fontWeight = '800';

}

/**
 Validacion del formulario
 */


function validacionFormulario() {
    var mensaje = "";
    /** @type {string}*/ let nombre = document.getElementById('nombre').value;

    let regex = /^[a-zA-Z ]*$/;
    if (nombre.length < 10 || nombre.length > 100 || !regex.test(nombre)) {
        mensaje += "Error en el nombre del archivo";
        
    }
    if (document.getElementById('archivo').files.length==0){
        mensaje += "No has seleccionado un Archivo";
    }
    /*
    La idea sería ir añadiendo más validaciones aquí, e ir concatenando el mensaje
    de error si es que existe, para al final realizar "mostrarError(mensaje_error_concatenado)".
     */
    if (mensaje.length < 1){
        return true;
    }

    mostrarError("Se han encontrado los siguientes errores:"+ mensaje)
    return false;

}

console.log('app v1.0'); // stack trace