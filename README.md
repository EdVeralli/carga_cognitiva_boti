# carga_cognitiva_boti
Del archivo TSV de Botmaker filtrar los rulenames activos y en la columna Bot Says hacer una limpieza de Links y signos de puntuación y contar la cantidad de palabras  por cada intención . Luego extraer medidas estadísticas de la cantidad de palabras y exportar las intenciones con mayor cantidad de palabras a un csv para su análisis .

Columnas a recuperar:	Id, name, bot says

Filtro por Filas:	no null, no spaces, active TRUE
 

## Proceso de Ejecucion:##

0	**00_check_emojis.py**
	Toma la lista de emojis usados en Boti y crea un archivo *emojis_unicode.csv* con los codigos unicodes asociados.
	
1	**01_proceso1.ps1**
	Script de PowerShell que transforma los unicodes graficos ( \u201c = Comilla doble que abre ) en caracteres ascii validos
	NOTA: Antes de ejecutar este script hay que habilitar el PowerShell en modo Administrador con el comando: `Set-ExecutionPolicy RemoteSigned`
	Luego se ejecuta:	.\proceso1.ps1 . Prestar atencion al Path que esta hardcodeado en el script.

2	**02_Crea_CSV_Emojis_encontrados.py**
	Crea un archivo *emojis_unicode_encontrados_TSV.csv* con los emojis de Paso 0 que fueron encontrados en el TSV . ( deberia dar vacios )

3	**03_Carga_cognitiva01.py**
	Analiza el TSV eliminando signos de pregunta , admiracion, tabulador, comas, puntos, asteriscos, retornos de carro.
	Tambien crea un *archivo barra_u_encontrados.csv* con los nuevos unicodes graficos aun no contemplados en el proceso 1
	Agrega una columna cant_palabras en el dataframe procesado y crea el archivo *TSV_procesado.csv*