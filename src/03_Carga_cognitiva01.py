#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 09:20:39 2024

@author: eduardo
"""

import csv
import os
import sys
import pandas as pd
import time

os.chdir("C:/GCBA/carga_cognitiva_boti/data/")


"""
Genero otro archivo .tsv con reemplazos de los Barra u usando un script de powershell
Atencion.. para ejecutar script en powershell entrar en modo Administrador y ejecutar:

    Set-ExecutionPolicy RemoteSigned
    .\proceso1.ps1

Luego de ejecutar el script, volver a poner la seguridad

    Set-ExecutionPolicy Restricted

"""

# Cargo en un df los unicodes de los emojis analizados en check_emojis.py
df_emojis_unicode = pd.read_csv("emojis_unicode.csv", index_col=False)
# paso los datos del df a una lista
lista_emojis_unicode = df_emojis_unicode["Unicode"].tolist()

df_tsv = pd.read_csv("rules.tsv", sep='\t', on_bad_lines='warn', index_col=False)

# Elimino las filas donde la columna Bot Says contiene valores NULL
df_tsv_sin_null = df_tsv.dropna(subset=['Bot Says'])

# Elimino las filas donde la columna Bot Says contiene valores espacios vacios
df_tsv_sin_nul_sin_vacios = df_tsv_sin_null[df_tsv_sin_null['Bot Says'].apply(lambda x: not x.isspace())]

# Solo dejo las filas donde ACTIVE esta en True
df_tsv_sin_nul_sin_vacios_Active = df_tsv_sin_nul_sin_vacios[df_tsv_sin_nul_sin_vacios['Active'] == True]

# Lista de nombres de columnas relevantes para el analisis
columnas_deseadas = ['Active', 'ID', 'Name','Bot Says']

# Creo un nuevo DataFrame con las columnas deseadas
df_tsv_limpio = df_tsv_sin_nul_sin_vacios_Active[columnas_deseadas].copy()

# Creo una columna nueva destino de los reemplazos
df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot Says']

# limpio las variables de reemploazo que son de la forma ${ algo adentro }
df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot_Says2'].str.replace(r'\${.*?}', '', regex=True)


# Defino un diccionario de reemplazos
reemplazos = {'\\t': ' ','¿': ' ','?': ' ', '!': ' ', '¡': ' ','¡': ' ',',': ' ','.': ' ','null': ' ','*': ' ','\\r\\n': ' '}

# Realizo los reemplazos en una sola línea
for buscar, reemplazar in reemplazos.items():
    df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot_Says2'].str.replace(buscar, reemplazar)


# InicialiZO una lista para almacenar los resultados
barra_u = []

# Itero sobre cada fila del DataFrame
for indice, fila in df_tsv_limpio.iterrows():
    # Divido las palabras en la columna "Bot_Says2" por espacios en blanco
    palabras = fila["Bot_Says2"].split()
    # Verifico si alguna palabra comienza con "\u" y tiene 4 caracteres
    for palabra in palabras:
        if len(palabra) == 6 and palabra.startswith("\\u"):
            barra_u.append(palabra)

# Elimino elementos duplicados de la lista
barra_u_sin_duplicados = list(set(barra_u))

print("Elementos \\u reconocidos hasta el momento")
print(barra_u_sin_duplicados)
print("Genero un diccionario sobre los valores encontrados y creo un CSV para ver si hay nuevos a procesar en el PowerShell")


nombre_archivo = "barra_u_encontrados.csv"

# Escribir la lista en el archivo CSV
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Barra_U'])
    for elemento in barra_u_sin_duplicados:
        escritor_csv.writerow([elemento])

print(f"Se ha creado el archivo CSV '{nombre_archivo}' con la lista de los barra_u_encontrados.")

# diccionario_barra_u = {}
# # Asigno valores específicos a cada elemento de la lista
# for elemento in barra_u_sin_duplicados:
#     ultimos_4_caracteres = elemento[-4:]
#     valor = " "
#     if ultimos_4_caracteres == "201c" :
#         valor = '"'
#     if ultimos_4_caracteres == "200d":
#         valor = ' '
#     if ultimos_4_caracteres == "20e3":
#         valor = ' '
#     if ultimos_4_caracteres == "2013":
#         valor = '-'
#     if ultimos_4_caracteres == "0094":
#         valor = ' '
#     if ultimos_4_caracteres == "2026":
#         valor = '...'
#     if ultimos_4_caracteres == "2019":
#         valor = "'"
#     if ultimos_4_caracteres == "2018":
#         valor = "'"
#     if ultimos_4_caracteres == "201d":
#         valor = '"'
#     # Asigno el valor al diccionario con el elemento como clave
#     diccionario_barra_u[elemento] = valor



print("-Cuenta la cantidad de palabras -----------------------------------------------------")



# Agrego columna con la cantidad de palabras 
df_tsv_limpio['cant_palabras'] = df_tsv_limpio['Bot_Says2'].str.split().apply(len)

# # Escribo en un csv el dataframe final
archivo_csv = "TSV_procesado.csv"
df_tsv_limpio.to_csv(archivo_csv, index=False)
