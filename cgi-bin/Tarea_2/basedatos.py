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


    return mensaje






print("""
<!DOCTYPE html>
<html lang=es>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <title>Estadisticas del Censo</title>
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
            <form method="post" id="formulario" onsubmit="return validar()">
                <div class="error oculto" id="error">
                    <p>error</p>
                </div>
                <div class="informe palido" id="domicilio">
                    <h3>Datos del Domicilio</h3>
                    <div class="entrada">
                        <h4>Región:</h4>
                        <select name="region" id="region" required onchange="comunasgenerate()">
                        <option value="">Seleccione su Region</option>
                        <option value="Región Metropolitana de Santiago">Región Metropolitana de Santiago</option>
                        <option value="Región de Arica y Parinacota">Región de Arica y Parinacota</option>
                        <option value="Región de Tarapacá">Región de Tarapacá</option>
                        <option value="Región de Antofagasta">Región de Antofagasta</option>
                        <option value="Región de Atacama">Región de Atacama</option>
                        <option value="Región de Coquimbo">Región de Coquimbo</option>
                        <option value="Región de Valparaíso">Región de Valparaíso</option>
                        <option value="Región del Libertador Gral. Bernardo O Higgins">Región del Libertador Gral. Bernardo O Higgins</option>
                        <option value="Región del Maule">Región del Maule</option>
                        <option value="Región de Ñuble">Región de Ñuble</option>
                        <option value="Región del Biobío">Región del Biobío</option>
                        <option value="Región de la Araucanía">Región de la Araucanía</option>
                        <option value="Región de Los Ríos">Región de Los Ríos</option>
                        <option value="Región de Los Lagos">Región de Los Lagos</option>
                        <option value="Región Aisén del Gral. Carlos Ibáñez del Campo">Región Aisén del Gral. Carlos Ibáñez del Campo</option>
                        <option value="Región de Magallanes y de la Antártica Chilena">Región de Magallanes y de la Antártica Chilena</option>
                        </select>
                    
                        <h4>Comuna:</h4>
                        <select name="comuna" id="comuna" required>
                            <option value="">Seleccione su Comuna</option>
                        </select>
                    </div>
    
                    <div class="entrada">
                        <h4>Nombre Calle:</h4>
                        <input type="text" name="calle" id="calle" required size=100 maxlength=250>
                        <h4>Número:</h4>
                        <input type="text" name="numero" id="numero" required size=10 maxlength=10>
                        <h4>Sector:</h4>
                        <input type="text" name="sector" id="sector" size=100 maxlength=100>
                    </div>
                </div>
                <div class="informe" id="contacto">
                    <h3>Datos de contacto</h3>
                    <div class="entrada">
                        <h4>Nombre:</h4>
                        <input type="text" name="nombre" id="nombre" size=100 required maxlength=200>
                        <h4>Email:</h4>
                        <input type="text" name="email" id="email" required size=100>
                        <h4>Número de Celular:</h4>
                        <input type="text" name="celular" id="celular">
                    </div>
                </div>
                <div class="informe palido">
                    <div class= "oculto" id="infomascota">
                        <h3>Informacion Mascota</h3>
                       <div class="entrada">
                           <h4>Tipo:</h4>
                            <select name="tipo-mascota" onchange="addOtro(this)">
                                <option value="">Seleccione el tipo</option>
                                <option value="perro">perro</option>
                                <option value="gato">gato</option>
                                <option value="pez">pez</option>
                                <option value="tortuga">tortuga</option>
                                <option value="hámster">hámster</option>
                                <option value="loro">loro</option>
                                <option value="iguana">iguana</option>
                                <option value="araña">araña</option>
                                <option value="otro">otro</option>
                            </select>
                            <input class="oculto" type="text" name="tipo-mascota-otro" size=40 maxlength=40>
                            <h4>Edad en años:</h4>
                            <input type="text" name="edad-mascota" size=5>
                       </div>
                       <div class="entrada">
                            <h4>Color:</h4>
                            <input type="text" name="color-mascota" size=30 maxlength=30>
        
                            <h4>Raza:</h4>
                            <input type="text" name="raza-mascota" maxlength=30 size=30>
                       </div>
                       <div class="entrada">
                            <h4>Esterilizado:</h4>
                            <select name="esterilizado-mascota">
                                <option value="">¿Esta esterilizado?</option>
                                <option value="sí">si</option>
                                <option value="no">no</option>
                                <option value="no aplica">no aplica</option>
                            </select>

                            <h4>Vacunas:</h4>
                            <select name="vacunas-mascota">
                                <option value="">¿Tiene las vacunas al día?</option>
                                <option value="si">sí</option>
                                <option value="no">no</option>
                                <option value="no aplica">no aplica</option>
                            </select>
                       </div>
                       <div>
                            <h4>Fotos:</h4>
                            <input class="especial" type="file" name="foto-mascota" id="foto-mascota">
                            <button type="button" onclick="duplicar('foto-mascota',this)">agregar otra foto</button>
                       </div>
                    </div>
                    <div class="palido">
                        <h3>Informacion Mascota</h3>
                       <div class="entrada">
                           <h4>Tipo:</h4>
                            <select name="tipo-mascota" required onchange="addOtro(this)">
                                <option value="">Seleccione el tipo</option>
                                <option value="perro">perro</option>
                                <option value="gato">gato</option>
                                <option value="pez">pez</option>
                                <option value="tortuga">tortuga</option>
                                <option value="hámster">hámster</option>
                                <option value="loro">loro</option>
                                <option value="iguana">iguana</option>
                                <option value="araña">araña</option>
                                <option value="otro">otro</option>
                            </select>
                            <input class="oculto" type="text" name="tipo-mascota-otro" size=40 maxlength=40>

                            <h4>Edad en años:</h4>
                            <input type="text" name="edad-mascota" required size=5>
                       </div>
                       <div class="entrada">
                            <h4>Color:</h4>
                            <input type="text" name="color-mascota" size=30 required maxlength=30>
                    
                            <h4>Raza:</h4>
                            <input type="text" name="raza-mascota" required maxlength=30 size=30>
                       </div>
                       <div class="entrada">
                            <h4>Esterilizado:</h4>
                            <select name="esterilizado-mascota" required>
                                <option value="">¿Esta esterilizado?</option>
                                <option value="sí">si</option>
                                <option value="no">no</option>
                                <option value="no aplica">no aplica</option>
                            </select>

                            <h4>Vacunas:</h4>
                            <select name="vacunas-mascota" required>
                                <option value="">¿Tiene las vacunas al día?</option>
                                <option value="si">sí</option>
                                <option value="no">no</option>
                                <option value="no aplica">no aplica</option>
                            </select>
                       </div>
                       <div>
                            <h4>Fotos:</h4>
                            <input class="especial" type="file" name="foto-mascota">
                            <button type="button" onclick="duplicar('foto-mascota',this)">agregar otra foto</button>
                       </div>
                    </div>
                </div>
                <div class="buttons">
                    <button type="button" onclick="duplicar('infomascota',this)">agregar otra mascota</button>
                    <button type="button" onclick="abrir()">Enviar informacion de este domicilio</button>
                </div>
            <div id="myModal" class="modal" style="display: block;">
                <div class="modal-content2">
""")

msg=validar()
if msg=="":
    print("""
                    <h4>Su información ha sido recibida muchas gracias por participar</h4>
                    <div class="buttons">
                        <a href="index.py"><button type="button">Cerrar y volver a la portada.</button></a>
        """)
else:
    print("""
                    <h4>Su información Contiene los siguientes errores</h4>
                    <p>{}</p>
                    <div class="buttons">
                        <a href="informe.py"><button type="button">Cerrar y volver a la portada.</button></a>
        """.format(msg))

print("""
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
""")