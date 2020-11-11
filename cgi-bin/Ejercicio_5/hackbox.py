#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import os
from http import cookies
import sys
import codecs
import string
import html
from typing import Tuple, Union

cgitb.enable()

# noinspection PyUnresolvedReferences
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# Obtener las cookies
c = ''
if 'HTTP_COOKIE' in os.environ:
    c = cookies.SimpleCookie(os.environ['HTTP_COOKIE'])


def SSID_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def evaluate_cookie(ck):
    """
    Recibe una cookie, y retorna el nombre de usuario y el estado del login. Si
    'login' no existe, o tiene formato distinto, retorna None.

    :param ck: Cookie
    :return: Datos
    """

    return None

# Pueden hacer esto desde el servidor, SQL
valid_users = {
    'pablo': 'a9sd-ds9f-34i0',
    'admin': 'sdf9-9sdf-3294',
    'Gasret': '12345678901234'
}

valid_SSID={}

# Variable que ira almacenando los errores
msgError = ''

# Leemos la informacion pasada desde el formulario
login_form = cgi.FieldStorage()  # POST
if 'username' in login_form and 'api' in login_form:
    name = html.escape(login_form.getvalue('username'))
    api = html.escape(login_form.getvalue('api'))
    if name in valid_users.keys() and api == valid_users[name]:
        c = cookies.SimpleCookie()
        c['username'] = '{0}'.format(name)
        c['username']['max-age'] = 10000  # segundos
        print(c)  # Esto no se debe imprimir despues del content-type
    else:
        msgError += 'API_KEY o Usuario incorrecto'

print('Content-type: text/html; charset=UTF-8')
print('')
print(msgError)  # Imprimirlo en el HTML

# Solo imprimimos si el usuario no tiene las cookies
if c == '' or evaluate_cookie(c) is None:  # Mas estricta
    bs = open('login.html', 'r', encoding='utf-8')
    for i in bs:
        print(i)
    bs.close()
    exit()

else:  # Imprime la aplicación
    #user, _ = evaluate_cookie(c)
    print(f"""
<!DOCTYPE html>
<!--suppress ALL -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hackbox</title>
    <link rel="stylesheet" type="text/css" href="estilo.css">
    <script src="validador.js"></script>
</head>


<body onload="">

<div class="menu entrada">

    <div class="entrada">
        <a href="https://google.cl">Home</a>
    </div>

    <div class="entrada">
        <a href="https://hackbox.html">Favoritos</a>
    </div>

    <div class="entrada" style="border-right: 0">
        <a href="">Configuraciones</a>
    </div>

</div>

<div class="titulo negrita">Hackbox</div>
<div class="saludo">Bienvenido </div>
<div class="main">

    <form id="miformulario" method="post" action="" onsubmit="return validacionFormulario()">

        <div class="entrada">

            <div class="leyenda">Nombre</div>

            <input type="text" id="nombre" minlength="10" maxlength="100" required="required"
                   placeholder="Escriba su nombre de archivo aqui"/>

        </div>

        <div class="entrada">

            <div class="leyenda">Archivo</div>

            <input type="file" id="archivo" required="required" accept="application/pdf">

        </div>

        <div class="entrada">

            <div class="leyenda">Privacidad</div>

            <select id="privacidad" required="required">
                <option value="" selected="selected">Seleccione una opción</option>
                <option value="1">Público</option>
                <option value="2">Privado</option>
            </select>

        </div>

        <div class="entrada">

            <div class="leyenda">Contraseña</div>

            <input type="password" id="password" size="10" maxlength="10">

        </div>

        <div class="entrada">

            <div class="leyenda">Autodestruir</div>

            <input type="number" id="autodestruir" min="1" max="3153600">

        </div>

        <div class="entrada">

            <div class="leyenda comentario">Comentario</div>

            <textarea id="comentario" maxlength="1000" rows="10" cols="40"
                      placeholder="Ingrese sus comentarios acá"></textarea>

        </div>

        <div class="entrada botones">

            <button id="enviar" type="submit">Submit</button>

            <button id="borrar" type="reset">Borrar</button>

        </div>

    </form>

</div>

<div id="error">Este es un mensaje de error</div>

</body>


</html>
""")
