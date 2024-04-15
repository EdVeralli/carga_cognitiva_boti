$archivo_original = "C:\GCBA\carga_cognitiva_boti\data\rules-2024.04.04-12.19.tsv"
$archivo_modificado = "C:\GCBA\carga_cognitiva_boti\data\rules.tsv"

$contenido = Get-Content $archivo_original -Raw
$diccionarioReemplazo = @{
    '\u201c' = '"'
    '\u200d' = ' '
    '\u20e3' = ' '
    '\u2013' = '-'
    '\u0094' = ' '
    '\u2026' = '...'
    '\u2019' = "'"
    '\u2018' = "'"
    '\u201d' = '"'
	
}

foreach ($cadenaOrig in $diccionarioReemplazo.Keys) {
    $contenido = $contenido -replace [regex]::Escape($cadenaOrig), $diccionarioReemplazo[$cadenaOrig]
}

$contenido | Set-Content $archivo_modificado -Encoding UTF8
