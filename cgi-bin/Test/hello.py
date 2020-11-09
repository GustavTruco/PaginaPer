#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb; cgitb.enable()
import html

print("Content-type: text/html; charset=UTF-8\r\n\r\n")
print("""
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,900;1,300;1,400;1,500;1,600;1,700;1,900&family=Orbitron:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <title>Gustavo Varas</title>
</head>
<body>
    <header>
        <ul>
            <li>
                <a href="https://anakena.dcc.uchile.cl/~gvaras/">Inicio</a>
            </li>
            <li>
                <a href="https://anakena.dcc.uchile.cl/~gvaras/proyectos">Proyectos</a>
            </li>
        </ul>
    </header>

    <div class="title">
        <h2>
            Gustavo Varas
        </h2>

    </div>
</body>
</html>""")