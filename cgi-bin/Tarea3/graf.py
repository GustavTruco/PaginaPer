#!/usr/bin/python
# -*- coding: utf-8 -*-


import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re
import sys
import codecs
import os
import json
from io import TextIOWrapper

database=mysql.connector.connect(
            host="localhost",
            user="cc500270_u",
            password="cuDuisphar",
            database="cc500270_db"
        )

c = database.cursor()


sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
cgitb.enable()

jsondata={}

print('Content-type: text/html; charset=UTF-8')
print('')


def checkMonth(id_tipo,month):
    query="select count(id), tipo_mascota from mascota_domicilio where domicilio_id in (select id from domicilio where extract(month from fecha_ingreso)=%s) and tipo_mascota_id=%s;"
    c.execute(query,(month,id_tipo))
    dato=c.fetchone
    return dato[0]

def getCantidadMascotas(id_tipo):
    query="select tipo_mascota_id, count(id) from mascota_domicilio where tipo_mascota_id=%s;"
    c.execute(query,(id_tipo,))
    dato=c.fetchone()
    return dato[1]

def getPieChartData():
    jsondata={}
    query="select * from tipo_mascota;"
    c.execute(query)
    datos=c.fetchall()
    for row in datos:
        jsondata[row[1]]=getCantidadMascotas(row[0])
    return jsondata

def getLineChartData():
    jsondata={}
    query="select cast(fecha_ingreso as Date), count(id) from domicilio group by cast(fecha_ingreso as Date);"
    c.execute(query)
    datos=c.fetchall()
    for row in datos:
        jsondata[row[0]]=row[1]
    return jsondata

def getBarChartData():
    jsondata={}
    perros=[]
    gatos=[]
    for i in range(12):
        perros.append(checkMonth(1,i+1))
        gatos.append(checkMonth(2,i+1))
    jsondata["perro"]=perros
    jsondata["gato"]=gatos
    return jsondata

jsondata={}
jsondata["PieChart"]=getPieChartData()
jsondata["LineChart"]=getLineChartData()
jsondata["BarChart"]=getBarChartData()

print(json.dumps(jsondata))
