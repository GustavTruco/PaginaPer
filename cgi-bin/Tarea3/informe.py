#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import html
import mysql.connector

database=mysql.connector.connect(
            host="localhost",
            user="cc500270_u",
            password="cuDuisphar",
            database="cc500270_db"
        )

cursor=database.cursor()


print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang=es>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <script src="funciones.js"></script>
        <title>Censo Mascotas</title>
        
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

            <form method="post" action="basedatos.py" id="formulario" onsubmit="return validar()" enctype="multipart/form-data">
                <div class="error oculto" id="error">
                    <p>error</p>
                </div>
                <div class="informe palido" id="domicilio">
                    <h3>Datos del Domicilio</h3>
                    <div class="entrada">
                        <h4>Región:</h4>
                        <select name="region" id="region" required onchange="comunasgenerate()">
                        <option value="">Seleccione su Region</option>
""")

query=("SELECT * FROM region;")
cursor.execute(query)

for id_num,nombre in cursor:
    print("<option value='{}'>{}</option>".format(id_num,nombre))

print("""
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
                        <input type="text" name="nombre" id="nombre" required size=100 maxlength=200>
                        <h4>Email:</h4>
                        <input type="text" name="email" id="email" required size=100>
                        <h4>Número de Celular:</h4>
                        <input type="text" name="celular" id="celular">
                    </div>
                </div>
                <div class="informe palido">
                    <div class= "oculto" id="infomascota" title="0">
                        <h3>Informacion Mascota</h3>
                       <div class="entrada">
                           <h4>Tipo:</h4>
                            <select name="tipo-mascota" onchange="addOtro(this)">
                            <option value="">Seleccione el tipo</option>
""")

query=("SELECT * FROM tipo_mascota;")
cursor.execute(query)

for id_num,nombre in cursor:
    print("<option value='{}'>{}</option>".format(id_num,nombre))

print("""
                            <option value="otro">otro</option>
                            </select>
                            <input class="oculto" type="text" name="tipo-mascota-otro" placeholder="Ingrese el tipo" size=40 maxlength=40>
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
                                <option value="0">si</option>
                                <option value="1">no</option>
                                <option value="2">no aplica</option>
                            </select>

                            <h4>Vacunas:</h4>
                            <select name="vacunas-mascota">
                                <option value="">¿Tiene las vacunas al día?</option>
                                <option value="0">sí</option>
                                <option value="1">no</option>
                                <option value="2">no aplica</option>
                            </select>
                       </div>
                       <div class="buscado">
                            <h4>Fotos:</h4>
                            <input class="especial" type="file" name="foto-mascota" id="foto-mascota" accept="image/*">
                            <button type="button" onclick="duplicar('foto-mascota',this)">agregar otra foto</button>
                       </div>
                    </div>
                    <div class="palido" title="1">
                        <h3>Informacion Mascota</h3>
                       <div class="entrada">
                           <h4>Tipo:</h4>
                            <select name="tipo-mascota" required onchange="addOtro(this)">
                            <option value="">Seleccione el tipo</option>
""")

query=("SELECT * FROM tipo_mascota;")
cursor.execute(query)

for id_num,nombre in cursor:
    print("<option value='{}'>{}</option>".format(id_num,nombre))

print("""
                            <option value="otro">otro</option>
                            </select>
                            <input class="oculto" type="text" name="tipo-mascota-otro" placeholder="Ingrese el tipo" size=40 maxlength=40>

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
                                <option value="0">si</option>
                                <option value="1">no</option>
                                <option value="2">no aplica</option>
                            </select>

                            <h4>Vacunas:</h4>
                            <select name="vacunas-mascota" required>
                                <option value="">¿Tiene las vacunas al día?</option>
                                <option value="0">sí</option>
                                <option value="1">no</option>
                                <option value="2">no aplica</option>
                            </select>
                       </div>
                       <div class="buscado">
                            <h4>Fotos:</h4>
                            <input class="especial" type="file" name="foto-mascota1" id="1" accept="image/*">
                            <button type="button" onclick="duplicar('foto-mascota',this)">agregar otra foto</button>
                       </div>
                    </div>
                </div>
                <div class="buttons">
                    <button type="button" onclick="duplicar('infomascota',this)">agregar otra mascota</button>
                    <button type="button" onclick="abrir()">Enviar informacion de este domicilio</button>
                </div>
                <div id="myModal" class="modal">
                    <div class="modal-content2">
                        <h4>¿Esta seguro que desea enviar esta información?</h4>
                        <div class="buttons">
                            <button type="button" onclick="achicar()">No estoy seguro</button>
                            <button type="submit" onclick="achicar()">Si, estoy total y absolutamente seguro</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    
    </body>
</html>

""")
