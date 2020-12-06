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
print("""<!DOCTYPE html>
<html lang=es>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <title>Censo Mascotas</title>  
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        <script src="map.js"></script>
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
            <div class="banner">
                <h1>Censo Online de Mascotas</h1>
                <p>Bienvenido a la plataforma de censo virtual de mascotas, donde puede encontrar el 
                    listado de las mascotas censadas, las estadisticas de los datos recolectados e informar
                    de sus propias mascotas para contribuir en este censo. Por favor para navegar utilice el menú superior. 
                </p>
            </div>
            <div id="mapcontainer">
                <div id="mapid">
                </div>
            </div>
            <div class="listado">
                <h3>Últimas Viviendas Censadas</h3>
                <div class="titulos">
                    <h4>Comuna</h4>
                    <h4>Calle</h4>
                    <h4>Tipo-Cantidad</h4>
                    <h4>Fotos</h4>
                </div>
""")
query=("select * from domicilio order by fecha_ingreso desc limit 5;")
cursor.execute(query)
rows=cursor.fetchall()

for row in rows:
    k=0
    if k%2==0:
        print(f"""<div class="elemento palido">""")
        k=k+1
    else:
        print("""<div class="elemento">""")
        k=k+1
    dom_id=row[0]
    comuna_id=row[2] 
    calle=row[3]
    query=("SELECT * from comuna where id=%s;")
    cursor.execute(query,(comuna_id,))
    dato=cursor.fetchone()
    print(f"""
                        <p>{dato[1]}</p>
                        <p>{calle}</p>
                        """)      
    print("""<p>Perro: 2</p> <img src="img/perros2.jpeg" alt="Perros">
            </div>""")   
                
print("""
            
            </div>
        </div>
    </body>
</html>

""")