#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import html
import mysql.connector
import re
import sys
from io import TextIOWrapper

database=mysql.connector.connect(
            host="localhost",
            user="cc500270_u",
            password="cuDuisphar",
            database="cc500270_db"
        )

cursor=database.cursor()

sys.stdout = TextIOWrapper(sys.stdout.buffer.detach(), encoding='utf8')

form = cgi.FieldStorage()

print("Content-type: text/html\r\n\r\n")
def validar():
    msensaje=""
    if form['region'].value=="":
        mensaje +="<br>"
        mensaje += "- Seleccione su Región"

    if form['comuna'].value=="" or form['comuna'].value=="Seleccione su Comuna":
        mensaje +="<br>"
        mensaje += "- Seleccione su Comuna"

    if form['calle'].value=="" or len(form['calle'].value)>250:
        mensaje +="<br>"
        mensaje += "- Ingrese un nombre de calle válido"

    if form['numero'].value=="" or len(form['numero'].value)>20:
        mensaje +="<br>"
        mensaje += "- Ingrese un número de vivienda válido"

    if form['sector'].value!="" and len(form['sector'].value)>100:
        mensaje +="<br>"
        mensaje += "- Ingrese un sector de vivienda válido"

    if form['nombre'].value=="" or len(form['nombre'].value)>250:
        mensaje +="<br>"
        mensaje += "- Ingrese un nombre de contacto válido"

    regex = r"/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/"

    if form['email'].value=="" or not bool(re.match(regex,form['email'].value)) or len(form['email'].value)>20:
        mensaje +="<br>"
        mensaje += "- Ingrese un correo de contacto válido"

    regex =r"/^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$/"

    if form['celular'].value=="" and not bool(re.match(regex,form['celular'].value)) or len(form['celular'].value)>20:
        mensaje +="<br>"
        mensaje += "- Ingrese un celular de contacto válido"

    for tipo in form['tipo-mascota']:
        pass

    return mensaje






print("""
<!DOCTYPE html>
<html lang=es>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <title>Display</title>
    </head>
    <body>
        <div class="content">
            <header>
                <ul>
                    <li><a href="index.py">Inicio</a></li>
                    <li><a href="informe.py">Informar Mascotas</a></li>
                    <li><a href="listado.py">Ver Listado de Mascotas</a></li>
                    <li><a href="estadisticas.html">Estadísticas</a></li>
                </ul>
            </header>
            <div class="estatistics">
""")

print(form['tipo-mascota'][1].value,form['tipo-mascota'][2].value)
msg=""
if msg=="":
    print("""
            <h3>Su información ha sido recibida muchas gracias por participar</h3>

            <p>Podra encontrar toda su informcaion en nuestro censo, viendo en portada los ultimos datos añadidos y en el listado podra encontrar la lista completa de todos los domicilios censados hasta la fecha</p>
            <div class="buttons">
                <a href="index.py"><button type="button">Cerrar y volver a la portada.</button></a>
            </div>
        </div>
        </div>
    </body>
</html>""")
else:
    print("""
            <h3>Su información Contiene los siguientes errores</h3>
            <p>""")
                    
    print(msg)
    print("""</p>
            <div class="buttons">
                <a href="informe.py"><button type="button">Cerrar y volver a la portada.</button></a>

            </div>
            </div>
        </div>
    </body>
</html>""")

