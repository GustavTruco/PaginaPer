#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
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

obligatorios=["region","comuna","calle","numero","nombre",
        "email","tipo-mascota","edad-mascota","color-mascota",
        "raza-mascota","esterilizado-mascota","vacunas-mascota","foto-mascota"]

opcionales=["sector","celular","tipo-mascota-otro"]

keys=form.keys()

mensaje=""
c=0

for string in obligatorios:
    if string not in form:
        mensaje+=string
        c+=1

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print("")
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
if mensaje=="":
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

if mensaje!="":
    print("""
            <h3>Su información contiene los siguientes errores</h3>
            <p>""")
                    
    print(mensaje)
    print("""</p>
            <div class="buttons">
                <a href="informe.py"><button type="button">Cerrar y volver a la portada.</button></a>
            </div>
            </div>
        </div>
    </body>
</html>""")
