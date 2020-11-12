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

region= form['region'].value
comuna= form['comuna'].value
calle= form['calle'].value
numero= form['numero'].value
sector= form['sector'].value
nombre= form['nombre'].value
email= form['email'].value
celular= form['celular'].value


datos=(region,comuna,calle,numero,sector,nombre,email,celular)

mensaje=""

regex = r"/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/"

regex =r"/^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$/"

print("Content-type: text/html\r\n\r\n")
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

            <h3>Su información ha sido recibida muchas gracias por participar</h3>

            <p>Podra encontrar toda su informcaion en nuestro censo, viendo en portada los ultimos datos añadidos y en el listado podra encontrar la lista completa de todos los domicilios censados hasta la fecha</p>
            <div class="buttons">
""")
print(datos)
print("""


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

