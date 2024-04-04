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

          
# df= pd.read_csv("Sesiones 1ra Instancia ne 05-01-24.csv", encoding='utf-8',index_col=False)
# #df= pd.read_csv("responses_master.csv", encoding='utf-8',index_col=False)

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

# Agrego columna con la cantidad de palabras 
df_tsv_limpio['cantidad_palabras'] = df_tsv_limpio['Bot Says'].str.split().apply(len)






# segunda_instancia = pd.read_csv("Sesiones 2da Instancia ne 05-01-24.csv")
# mensajes_totales = pd.read_csv("mensajes_01_01_2024.csv")

# ids_primera_instancia = primera_instancia["session_id"].tolist()
# ids_segunda_instancia = segunda_instancia["session_id"].tolist()
# print("Cantidad de mensajes de segunda instancia", len(ids_segunda_instancia))
# print("Cantidad de mensajes totales", mensajes_totales.shape[0])

# segunda_instancia_lim = segunda_instancia[segunda_instancia["session_id"].isin(ids_primera_instancia)]
# mensajes_totales_prim_inst = mensajes_totales[mensajes_totales["session_id"].isin(ids_primera_instancia)]
# mensajes_totales_prim_inst = mensajes_totales_prim_inst[~mensajes_totales_prim_inst["session_id"].isin(ids_segunda_instancia)]
# print("Cantidad de mensajes de segunda instancia", segunda_instancia_lim.shape) 
# print("Cantidad de mensajes totales del 01/01/2024 que tuvieron un NE en la conversación pero no hay NE de segumda instancia", mensajes_totales_prim_inst.shape)

# mensajes_totales_prim_inst = mensajes_totales_prim_inst.sort_values(by=['creation_time', 'session_id'])


# mensajes_totales_prim_inst_2 = mensajes_totales_prim_inst.loc[~((mensajes_totales_prim_inst['rule_name'].isna()) & (mensajes_totales_prim_inst['original_user_message'].isna()))]


# mensajes_totales_prim_inst_2['rule_name'] = mensajes_totales_prim_inst_2['rule_name'].apply(str)


# Mensajes_1era_Instancia_Sin_Nan_Sin_Insultos = mensajes_totales_prim_inst_2[~(mensajes_totales_prim_inst_2['rule_name'].str.contains('Insultos'))]   ## BOT01CUX01 Insultos

# #Mensajes_1era_Instancia_Sin_Nan_Sin_Insultos.to_csv("mensajes.csv", index=False)

# sys.exit()

# lista_exitos_1era_instancia = []
# lista_fracasos_1era_instancia = []


# ant = "XXX"
# for indice, fila in Mensajes_1era_Instancia_Sin_Nan_Sin_Insultos.iterrows():
#     #print(f'Índice: {indice}, Fila:\n{fila}\n')
#     #print(f'Fila:\n{fila}\n')
    
#     lista_resultante = fila.tolist()
#     el_session_id            = str(lista_resultante[0])
#     el_msg_from              = str(lista_resultante[1])
#     la_rule_name             = str(lista_resultante[6])
#     el_original_user_message = str(lista_resultante[7])
#     el_message               = str(lista_resultante[8])
    
    
    
#     # if el_original_user_message.find(" No, nada de eso") > 1:
#     #     sys.exit()
    
    

#     if ant !=  el_session_id:
#         ant = el_session_id
#         df_una_sesionId = Mensajes_1era_Instancia_Sin_Nan_Sin_Insultos[Mensajes_1era_Instancia_Sin_Nan_Sin_Insultos['session_id'] == el_session_id]

#         # Localizar la fila con el valor específico en la columna 
#         indice_fila = df_una_sesionId[df_una_sesionId['rule_name'] == 'Instancia 1 | No entendidos'].index[0]
        
#         # Eliminar las filas anteriores utilizando loc
#         df_una_sesionId_cortado = df_una_sesionId.loc[indice_fila:]

#         if el_session_id.find("2024-01-02") > 1:
#             nom_arch = el_session_id+".csv"
#             if len(df_una_sesionId_cortado) > 12 :
#                 #df_una_sesionId_cortado.to_csv(nom_arch, index=False)
#                 """
#                 Estamos en el caso de un SessionId que fue entendida por el Bot 
#                 """
#                 lista_exitos_1era_instancia.append(el_session_id)
#                 print("Largo:",len(df_una_sesionId_cortado))
#                 print("grabo session ID ",nom_arch)
#             """
#             Analizo el caso de que en las 3 ultimas interacciones el Bot le dijo  ' No, nada de eso"'
#             """
#             ultimas_tres_filas = df_una_sesionId_cortado.tail(3)
#             df_filtrado3 = ultimas_tres_filas[ultimas_tres_filas['original_user_message'].str.contains(" No, nada de eso")]
#             if len(df_filtrado3) > 0:
#                 ## Termina la charla con No, nada de eso.   --> Abandono del user
#                 lista_fracasos_1era_instancia.append(el_session_id)
                


                
                
# """
# Charla 11-01-2024
# si luego de 1era instancia hay mas de 10 mensajes asumimos que siguio navengando asumiimos que el bot entendio ( bien o mal )
# si luego de la X no hay mas interaccion , asumimo que el user abandono
# si la ultima interaccion fue presentar la botonera de la X se toma como abandono

# campo message de message metrics  buscar: Creo que no te entendí bien , esto debe ser ultimo o anteultimo

# si el 30% de la charla son insultos se considera la sessionId ANULADA

# """
               
                
                
                
#         # if el_session_id.find("2024-01-02") > 1 and el_msg_from.find("user") > 1:
#         #     nom_arch = "User_"+el_session_id+".csv"
#         #     if len(df_una_sesionId_cortado) > 10 :
#         #         df_una_sesionId_cortado.to_csv(nom_arch, index=False)
#         #         print("Largo:",len(df_una_sesionId_cortado))
#         #         print("grabo session ID ",nom_arch)

    
#     #print("---->"+el_session_id+" //// "+la_rule_name+" \\\\\\\\ "+el_message+" *****************")
    
    