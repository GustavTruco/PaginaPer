#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import html

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang=es>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <script src="funciones.js"></script>
        <title>Información Censo</title>
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
            <div class="censo">
                <div class="seccion palido">
                        <h3>Domicilio:</h3> 
                        <h4>Región: </h4> <p>Metropolitana</p>
                        <h4>Comuna: </h4> <p>Ñuñoa</p>
                        <h4>Nombre Calle: </h4> <p>Irarrazabal</p>
                        <h4>Número: </h4> <p>2000</p>
                        <h4>Sector: </h4> <p>Villa Seca</p>
                </div>
                <div class="seccion">
                        <h3>Datos de Contacto:</h3>
                        <h4>Nombre: </h4> <p>Gustavo Varas</p>
                        <h4>Email: </h4> <p>g.varas@gmail.com</p>
                        <br>
                        <h4>Número de Celular: </h4> <p>+56 9 4444 0440</p>
                </div>
                <div class="seccion palido">
                        <h3>Información de Mascota:</h3>
                        <h4>Tipo:</h4> <p>Hamster</p>
                        <h4>Edad en Años:</h4> <p>2</p>
                        <h4>Color: </h4> <p>Blanco, negro y cafe</p>
                        <h4>Raza: </h4> <p>Roborowski</p>
                        <h4>Esterilizado: </h4> <p>N/A</p>
                        <h4>Vacunas al Día: </h4> <p>N/A</p>
                </div>
                <div class="fotos">
                    <h3>Fotos</h3>
                    <img src="img/hamster3.png" alt="Hmasters" id="foto" onclick="agrandar(this)">
                </div>

                <div class="enlaces palido">
                    <div><a href="listado.html">Volver al listado</a></div>
                    <div><a href="index.html">Ir a Portada</a></div>
                </div>
            </div>
            
        </div>

        <div id="myModal" class="modal" >
            <img  class="close" src="img/close.svg" alt="" onclick="achicar()">
            <img class="modal-content" id="img01" src="img/close.svg" alt="Imagen agrandada">
        </div>
    </body>
</html>
""")