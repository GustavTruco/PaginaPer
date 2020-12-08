import cgi
import cgitb
import mysql.connector
import re
import sys
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

print('Content-type: text/html; charset=UTF-8')
print('')

sql="select domicilio.comuna_id as id_comuna, count(domicilio.id) as suma From domicilio Inner join mascota_domicilio on domicilio.id=mascota_domicilio.domicilio_id group by domicilio.comuna_id;"

c.execute(sql)
record= c.fetchall()
jsdata={}
for row in records:
    id_com= row[0]
    suma=row[1]
    query=("SELECT * from comuna where id=%s;")
    c.execute(query,(id_com,))
    dato=c.fetchone()
    json[dato[1]]=suma

print(json.dumps(jsdata))
