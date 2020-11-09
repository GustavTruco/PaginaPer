#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import html

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print("""<!DOCTYPE html>
<html lang=es>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <title>Censo Mascotas</title>
    </head>
    <body>
        <div class="content">
            <header>
                <ul>
                    <li><a href="index.py">Inicio</a></li>
                    <li><a href="informe.html">Informar Mascotas</a></li>
                    <li><a href="listado.html">Ver Listado de Mascotas</a></li>
                    <li><a href="estadisticas.html">Estadísticas</a></li>
                </ul>
            </header>
            <div class="banner">
                <h1>Censo Online de Mascotas</h1>
                <p>Bienvenido a la plataforma de censo virtual de mascotas, donde puede encontrar el 
                    listado de las mascotas censadas, las estadisticas de los datos recolectados e informar
                    de sus propias mascotas para contribuir en este censo. Por favor para navegar utilice el menú superior. 
                </p>
            </div>
            <div class="listado">
                <h3>Últimas Viviendas Censadas</h3>
                <div class="titulos">
                    <h4>Comuna</h4>
                    <h4>Calle</h4>
                    <h4>Tipo-Cantidad</h4>
                    <h4>Fotos</h4>
                </div>
                <div class="elemento palido">
                    <p>Las Condes</p>
                    <p>Las Lomas</p>
                    <p>Perro: 1</p>
                    <img src="img/perro1.jpeg" alt="Perro">
                </div>
                <div class="elemento">
                    <p>Peñañolen</p>
                    <p>Nueva Dos</p>
                    <p>Perro: 2</p>
                    <img src="img/perros2.jpeg" alt="Perros">
                </div>
                <div class="elemento palido">
                    <p>Ñuñoa</p>
                    <p>Duble Almeyda</p>
                    <p>Gato: 1</p>
                    <img src="img/gato1.jpeg" alt="Gato">
                </div>
                <div class="elemento">
                    <p>Macul</p>
                    <p>Macul</p>
                    <p>Otro: 1</p>
                    <img src="img/Huron1.jpeg" alt="Huron">
                </div>
                <div class="elemento palido">
                    <p>Ñuñoa</p>
                    <p>Irarrázabal</p>
                    <p>Hamster: 3</p>
                    <img src="img/hamster3.png" alt="Hamsters">
                </div>
            </div>
        </div>
    </body>
</html>

""")