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

# Crear un nuevo DataFrame con las columnas deseadas
df_tsv_limpio = df_tsv_sin_nul_sin_vacios_Active[columnas_deseadas].copy()

# Creo una columna nueva destino de los reemplazos
df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot Says']

# limpio las variables de reemploazo que son de la forma ${ algo adentro }
df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot_Says2'].str.replace(r'\${.*?}', '', regex=True)


# Defino un diccionario de reemplazos
reemplazos = {'¿': ' ','?': ' ', '!': ' ', '¡': ' ','¡': ' ',',': ' ','.': ' ','null': ' ','*': ' ','\\r\\n': ' '}

# Realizo los reemplazos en una sola línea
for buscar, reemplazar in reemplazos.items():
    df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot_Says2'].str.replace(buscar, reemplazar)

"""
Analizar como hago con los codigos de esta forma: \u2019
"""


# Agrego columna con la cantidad de palabras 
df_tsv_limpio['cant_palabras'] = df_tsv_limpio['Bot_Says2'].str.split().apply(len)




# La Linea a continuacion NO funciona... tengo que usar un iterador
#df_tsv_limpio['Bot_Says2'] = df_tsv_limpio['Bot Says'].replace('\\r\\n', '')

# for index, row in df_tsv_limpio.iterrows():
#     linea = row['Bot Says'] 
#     #print("\n",linea)
#     linea2 = linea.replace('\\r\\n', ' ')
#     #print("\n",linea2)  
#     # Asign0 el nuevo valor a la columna 'Bot_Says2'
#     df_tsv_limpio.at[index, 'Bot_Says2'] = linea2
# 
