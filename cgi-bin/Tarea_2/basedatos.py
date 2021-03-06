#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re
import sys
import os
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

permited_ext=["jpeg","jpg","gif","png"]

keys=form.keys()

mensaje=""
c=0

for string in obligatorios:
    if string not in form:
        mensaje+=string
        c+=1

if c>0:
    mensaje+="<br> -Faltan datos obligatorios en el formulario"
    region=""
    comuna=""
    calle=""
    numero=""
    nombre=""
    email=""
    tipos=[]
    edades=[]
    colores=[]
    razas=[]
    esterilizados=[]
    vacunas=[]

else:
    region= form['region'].value
    comuna= form['comuna'].value
    calle=form['calle'].value
    if len(calle)>250:
        mensaje+="<br> -Ingrese un nombre de calle válido"
    numero=form['numero'].value
    if len(numero)>20:
        mensaje+="<br> -Ingrese un número de casa válido"
    nombre= form['nombre'].value
    if len(nombre)>200:
        mensaje+="<br> -Ingrese un nombre válido"
    email= form['email'].value
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(regex,email):
        mensaje+="<br> -Ingrese un correo electrónico válido"

    tipos=form.getlist("tipo-mascota")
    tipos.pop(0)
    for tipo in tipos:
        if tipo =="":
            mensaje+="<br> -Ingrese un tipo de mascota válido"

    edades=form.getlist("edad-mascota")
    edades.pop(0)
    for edad in edades:
        if not edad.isdigit() or int(edad)<0:
            mensaje+="<br> -Ingrese una edad para su mascota válida"

    colores=form.getlist("color-mascota")
    colores.pop(0)
    for color in colores:
        if len(color)>30:
            mensaje+="<br> -Ingrese un color válido"
    razas=form.getlist("raza-mascota")
    razas.pop(0)
    for raza in razas:
        if len(raza)>30:
            mensaje+="<br> -Ingresea raza válido"

    esterilizados=form.getlist("esterilizado-mascota")
    esterilizados.pop(0)
    for esterilizado in esterilizados:
        if esterilizado=="":
            mensaje+="<br> -Ingrese estado de esterilización"

    vacunas=form.getlist("vacunas-mascota")
    vacunas.pop(0)
    for vacuna in vacunas:
        if vacuna=="":
            mensaje+="<br> -Ingrese estado de vacunas"

if "sector" in keys:
    sector=form['sector'].value
    if len(sector)>100:
        mensaje+="<br> -Ingrese un sector de vivienda válido"
else: 
    sector=""

if "celular" in keys:
    celular=form['celular'].value
else:
    celular=""

if "tipo-mascota-otro" in keys:
    otros=form.getlist("tipo-mascota-otro")
    otros.pop(0)
    for otro in otros:
        if len(otro)>40:
            mensaje+="<br> -Ingrese un tipo de mascota válido"
otro=[]

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
num_mascotas=len(tipos)
i=1
allnombres_archivos=[]
allarchivos=[]
while i<=num_mascotas:
    name='foto-mascota'+str(i)
    fotos=form[name]
    nombres_archivos=[]
    allarchivos.append(fotos)
    if type(fotos)==list:
        for foto in fotos:
            fn=foto.filename
            nombres_archivos.append(fn)
    else:
        fn=fotos.filename
        nombres_archivos.append(fn)
    allnombres_archivos.append(nombres_archivos)
    i+=1

for nombres in allnombres_archivos:
    for nom in nombres:
        ext=str(nom).split('.')[1]
        if ext not in permited_ext:
            mensaje+="<br> -Ingrese una imagen con formato válido"
            
if mensaje=="":
    print(tipos)
    print(edades)
    #--------------------------------------#
    #Ingresar datos a la base de datos:
    query1=("INSERT INTO domicilio (fecha_ingreso,comuna_id,nombre_calle,numero,sector,nombre_contacto,email,celular)"
            "VALUES (NOW(),%s,%s,%s,%s,%s,%s,%s);")
    query2=("Select * from comuna where nombre=%s;")
    cursor.execute(query2,(comuna,))
    records=cursor.fetchone()
    id_com=records[0]

    data=(id_com,calle,numero,sector,nombre,email,celular,)
    cursor.execute(query1,data)
    database.commit()

    query3=("Select * from domicilio where nombre_calle=%s and numero=%s and nombre_contacto=%s and email=%s;")
    cursor.execute(query3,(calle,numero,nombre,email,))
    records=cursor.fetchone()
    id_dom=records[0]

    i=0
    print("STAR PET QUERY")
    while i<num_mascotas:
        print(i)
        tipo=tipos[i]
        if tipo=="otro":
            query6=("INSERT INTO tipo_mascota (nombre) VALUES (%s);")
            cursor.execute(query6,(otros[i],))
            database.commit()
            query5=("Select * from tipo_mascota where nombre=%s;")
            cursor.execute(query5,(otros[i],))
            records=cursor.fetchone()
            tipo=records[0]
      
        print(tipo,id_dom)

        print(edades)
        edad=edades[i]
        print(edad)

        color=colores[i]
        print(color)

        raza=razas[i]
        print(raza)

        esterilizado=esterilizados[i]
        print(esterilizado)

        vacuna=vacunas[i]
        print(vacuna)

        query4=("INSERT INTO mascota_domicilio (tipo_mascota_id,edad,color,raza,esterilizado,vacunas_al_dia,domicilio_id)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s);")
        data=(int(tipo),int(edades[i]),colores[i],razas[i],int(esterilizados[i]),int(vacunas[i]),id_dom,)
        cursor.execute(query4,data)
        database.commit()
        print("END QUERY")
        
        #-----------#
        #fotos
        c=0
          
        dir_path=os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        if (len(allnombres_archivos[i])>1):
            print("2 archivo")
            for archivo in allarchivos[i]:
                new_n=str(id_com)+str(id_dom)+str(i)+str(c)+".png"
                f=open("./DBIGM/"+new_n,"wb+")
                f.write(archivo.value)
                f.close
                print("FILE SAVED")
                c+=1
        else:
            new_n=str(id_com)+str(id_dom)+str(i)+str(c)+".png"
            archivo=allarchivos[i]
            print("1 archivo")
            f=open("./DBIGM/"+new_n,"wb+")
            f.write(archivo.value)
            f.close
            print("FILE SAVED")
            c+=1
    
        #-----------#
        i+=1


    #----------------------------------------#
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