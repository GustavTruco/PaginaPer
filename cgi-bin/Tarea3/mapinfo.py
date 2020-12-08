#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import cgitb
import html
import codecs
import sys
import mysql.connector
import json

# noinspection PyUnresolvedReferences
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

def getTipo(id_tipo):
    query="Select * from tipo_mascota where id=%s"
    c.execute(query,(id_tipo,))
    dato=c.fetchone()
    return dato[1]


# Obtiene los datos por post
datos = cgi.FieldStorage()  # get, post
jsondata={}
lista_dom=[]

print('comuna' in datos)
if 'comuna' in datos:
    comuna=html.escape(datos.getvalue('comuna'))
    comuna=sql.escape(comuna)
else:
    comuna="Gorbea"
database=mysql.connector.connect(
            host="localhost",
            user="cc500270_u",
            password="cuDuisphar",
            database="cc500270_db"
        )
c = database.cursor()
query="Select * from comuna where nombre=%s;"
c.execute(query,(comuna,))
dato=c.fetchone()
id_com=dato[0]
print(id_com)
query2= "Select * from mascota_domicilio where domicilio_id in (select id from domicilio where comuna_id=%d);"
c.execute(query,(id_com,))
datos=c.fetchall()
print(datos)
for row in datos:
    tipo=getTipo(row[1])
    edad=row[2]
    color=row[3]
    raza=row[4]
    esterilizado=[5]
    vacunas=[6]
    print(tipo,edad,color,raza,esterilizado,vacunas)
    lista_dom.append({"tipo":tipo,"edad":edad,"color":color,"raza":raza,"esterilizado":esterilizado,"vacunas":vacunas})

jsondata["results"]=lista_dom
print(json.dumps(jsondata))
    




