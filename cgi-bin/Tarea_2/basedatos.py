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
obligatorios=["region","comuna","calle","numero","nombre",
        "email","tipo-mascota","edad-mascota","color-mascota",
        "raza-mascota","esterilizado-mascota","vacunas-mascota","foto-mascota"]
opcionales=["sector","celular"]

keys=form.keys()

mensaje=""
c=0
for string in obligatorios:
    if string not in keys:
        c+=1

if c>0:
    mensaje+="<br> -Faltan datos obligatorios en el formulario"
else:
    region= form['region'].value
    comuna= form['comuna'].value
    calle= html.escape(form['calle'].value)
    numero= html.escape(form['numero'].value)
    nombre= html.escape(form['nombre'].value)
    email= html.escape(form['email'].value)
    tipos=[html.escape(elem) for elem in form.getlist("tipo-mascota")]
    edades=[html.escape(elem) for elem in form.getlist("edad-mascota")]
    colores=[html.escape(elem) for elem in form.getlist("color-mascota")]
    razas=[html.escape(elem) for elem in form.getlist("raza-mascota")]
    esterilizados=form.getlist("esterilizado-mascota")
    vacunas=form.getlist("vacunas-mascota")

if "sector" in keys:
    sector= html.escape(form['sector'].value)
if "celular" in keys:
    celular=html.escape(form['celular'].value)


regex = r"/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/"

regex =r"/^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$/"

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
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

