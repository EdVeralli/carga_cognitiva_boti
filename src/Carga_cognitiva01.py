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

# Cargo en un df los unicodes de los emojis analizados en check_emojis.py
df_emojis_unicode = pd.read_csv("emojis_unicode.csv", index_col=False)
# paso los datos del df a una lista
lista_emojis_unicode = df_emojis_unicode["Unicode"].tolist()

df_tsv = pd.read_csv("rules-2024.04.04-12.19.tsv", sep='\t', encoding='latin1', on_bad_lines='warn', index_col=False)

"""
nombres_columnas = df_tsv.columns.tolist()
# Imprimir los nombres de las columnas
print(nombres_columnas)

tipos_variables = df_tsv.dtypes
# Imprimir los tipos de variables
print(tipos_variables)
"""

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


"""
Analizo los codigos de esta forma: \u2019
"""
import pandas as pd

# Inicializar una lista para almacenar los resultados
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
print("------------------------------------------------------")

# Itero sobre cada fila del DataFrame 
# reemplazo los elementos de la columna Bot_Says2
# que correspondan a alguno de los elementos de la lista
# barra_u_sin_duplicados
for indice, fila in df_tsv_limpio.iterrows():
    botisays2 = fila["Bot_Says2"]
    for elemento in barra_u_sin_duplicados:
        botisays2 = botisays2.replace(elemento, ' ')
    df_tsv_limpio.at[indice, "Bot_Says2"] = botisays2


# Agrego columna con la cantidad de palabras 
df_tsv_limpio['cant_palabras'] = df_tsv_limpio['Bot_Says2'].str.split().apply(len)


"""
Analizo cuantas fila del tsv contienen alguno de los emojis en formato Unicode
Recordar que solo se pueden procesar los emojis de 1 byte, los de 2 bytes fueron descartados
en el proceso check_emojis.py
"""

# Inicializo una lista para almacenar los resultados
emojis_en_df = []

# Itero sobre cada fila del DataFrame
for indice, fila in df_tsv_limpio.iterrows():
    # Divido las palabras en la columna "Bot_Says2"
    palabras = fila["Bot_Says2"].split()
    # Verifico si algún elemento buscado está presente en las palabras
    if any(elemento in palabras for elemento in lista_emojis_unicode):
        # Si sí, agrego la fila al DataFrame de resultados
        emojis_en_df.append(fila)
        botisays2 = fila["Bot_Says2"]
        print("--////----------------------------------------------------")
        print("mensaje con emoji de 1byte",botisays2)
        print("fila",indice)
        print("--/////----------------------------------------------------")
        for elemento2 in lista_emojis_unicode:
            botisays2 = botisays2.replace(elemento2, ' ')
        df_tsv_limpio.at[indice, "Bot_Says2"] = botisays2
        


# Creo un DataFrame con las filas donde hay algun emoji de la lista
df_tsv_limpio_Solo_filas_con_Emojis = pd.DataFrame(emojis_en_df)

