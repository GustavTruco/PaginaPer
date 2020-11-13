#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import html
import mysql.connector
import re
import sys
from io import TextIOWrapper
from datetime

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

if "sector" in keys:
    sector= html.escape(form['sector'].value)
    if len(sector)>100:
        mensaje+="<br> -Ingrese un sector de vivienda válido"
else: 
    sector=""
if "celular" in keys:
    celular=html.escape(form['celular'].value)
else:
    celular=""

if "tipo-mascota-otro" in keys:
    otros=[html.escape(elem) for elem in form.getlist("tipo-mascota-otro")]
    for otro in otros:
        if len(otro)>40:
            mensaje+="<br> -Ingrese un tipo de mascota válido"
        else:
            query=("INSERT INTO tipo_mascota (nombre) VALUES ({});".format(otro))
            cursor.execute(query)

if c>0:
    mensaje+="<br> -Faltan datos obligatorios en el formulario"
else:
    region= form['region'].value
    comuna= form['comuna'].value
    calle= html.escape(form['calle'].value)
    if len(calle)>250:
        mensaje+="<br> -Ingrese un nombre de calle válido"
    numero= html.escape(form['numero'].value)
    if len(numero)>20:
        mensaje+="<br> -Ingrese un número de casa válido"
    nombre= html.escape(form['nombre'].value)
    if len(nombre)>200:
        mensaje+="<br> -Ingrese un nombre válido"
    email= html.escape(form['email'].value)

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex,email):
        mensaje+="<br> -Ingrese un correo electrónico válido"
    
    tipos=[html.escape(elem) for elem in form.getlist("tipo-mascota")]
    edades=[html.escape(elem) for elem in form.getlist("edad-mascota")]
    for edad in edades:
        if not edad.isdigit() or edad<0:
            mensaje+="<br> -Ingrese una edad para su mascota válida"

    colores=[html.escape(elem) for elem in form.getlist("color-mascota")]
    for color in colores:
        if len(color)>30:
            mensaje+="<br> -Ingrese un color de mascota válido"
    razas=[html.escape(elem) for elem in form.getlist("raza-mascota")]
    for raza in razas:
        if len(raza)>30:
            mensaje+="<br> -Ingrese una raza de mascota válida"
    esterilizados=form.getlist("esterilizado-mascota")
    vacunas=form.getlist("vacunas-mascota")



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

    fecha = datetime.datetime.now()
    query=("SELECT * from comuna where nombre='{}';".format(comuna))
    print(comuna)
    print("<br>")
    #cursor.execute(query)
    #for id_com,_,_ in cursor:
    #    id_comuna=id_com

    query=("""INSERT INTO domicilio (fecha_ingreso,comuna_id,
            nombre_calle,numero,sector,nombre_contacto,email,celular)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""")
    data=(fecha,id_comuna,calle,numero,sector,nombre,email,celular)
    print (data)
    #cursor.execute(query,data)


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

