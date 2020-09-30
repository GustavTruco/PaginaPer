/**
 * Imprime error
 * @param {string|number} msg
 */
function mostrarError(msg) {

    let contenedor = document.getElementById('error');

    contenedor.innerHTML = msg;
    contenedor.style.display = 'block';
}

function eraseErrors(){
    let contenedor = document.getElementById('error');
    contenedor.style.display= 'None';
}

/**
 Validacion del formulario
 */


function validacionFormulario() {
    var mensaje = "";
    /** @type {string}*/ let nombre = document.getElementById('nombre').value;

    let regex = /^[a-zA-Z ]*$/;
    if (nombre.length < 10 || nombre.length > 100 || !regex.test(nombre)) {
        mensaje +="<br>";
        mensaje += "- Error en el nombre del archivo";
        
        
    }
    if (document.getElementById('archivo').files.length==0){
        mensaje +="<br>";
        mensaje += "- No has seleccionado un Archivo";
        
    }

    if (document.getElementById('privacidad').value==""){
        mensaje+="<br>"
        mensaje+="- No ha seleccionado la privacidad del archivo"
    }

    if (document.getElementById('privacidad').value=="2"){
        let pass=document.getElementById('password').value;
        var notpass = ["password", "1234", "pass", "user","hackbox"];
        if (pass==""){
            mensaje+="<br>";
            mensaje+="- Por favor ingrese contraseña";
        }
        if (notpass.includes(pass)){
            mensaje+="<br>";
            mensaje+="- Por favor ingrese una contraseña mas creativa";
        }
        if (pass.length>10){
            mensaje+="<br>";
            mensaje+="- Su contraseña excede el maximo de caracteres";
        }
    }

    let autodes=document.getElementById("autodestruir").value;
    if (autodes!="" && (autodes<1 || autodes>3153600 || isNaN(autodes))){
        mensaje+="<br>";
        mensaje+="- Ingrese un tiempo de autodestrucción válido";
    }

    if (document.getElementById("comentario").value.length>1000){
        mensaje+="<br>";
        mensaje+="- Su comentario es muy largo, sea mas breve";
    }

    if (mensaje.length < 1){
        return true;
    }

    mostrarError("Se han encontrado los siguientes errores:"+ mensaje)
    return false;

}

console.log('app v1.0'); // stack trace