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
        <title>Listado Mascotas Censadas</title>
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
            <div class="listado">
                <h2>Listado Mascotas Censadas</h2>
                <div class="titulos">
                    <h4>Fecha Ingreso</h4>
                    <h4>Comuna</h4>
                    <h4>Nombre Calle</h4>
                    <h4>Nombre Contacto</h4>
                    <h4>Total Mascotas</h4>
                    <h4>Total Fotos</h4>
                </div>
                <div class="elemento palido">
                    <a href="info.py">
                        <p>23/01/2020</p>
                        <p>Ñuñoa</p>
                        <p>Irarrázabal</p>
                        <p>Gustavo Varas</p>
                        <p>3</p>
                        <p>1</p>
                    </a>
                </div>
                <div class="elemento">
                    <a href="info.py">
                        <p>04/03/2020</p>
                        <p>Macul</p>
                        <p>Macul</p>
                        <p>Antonia Díaz</p>
                        <p>1</p>
                        <p>1</p>
                    </a>
                </div>
                <div class="elemento palido">
                    <a href="info.py">
                        <p>28/04/2020</p>
                        <p>Ñuñoa</p>
                        <p>Duble Almeyda</p>
                        <p>Antonio Santander</p>
                        <p>1</p>
                        <p>1</p>
                    </a>
                </div>
                <div class="elemento">
                    <a href="info.py">
                        <p>12/09/2020</p>
                        <p>Peñañolen</p>
                        <p>Nueva Dos</p>
                        <p>Josefa Perez</p>
                        <p>2</p>
                        <p>1</p>
                    </a>
                </div>
                <div class="elemento palido">
                    <a href="info.py">
                        <p>26/09/2020</p>
                        <p>Las Condes</p>
                        <p>Las Lomas</p>
                        <p>Julián Donoso</p>
                        <p>1</p>
                        <p>2</p>
                    </a>
                </div>
            </div>
        </div>
    </body>
</html>
""")