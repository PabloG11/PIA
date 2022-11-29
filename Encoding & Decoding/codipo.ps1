﻿Clear-Host
Write-Host "Bienvenido a un ejemplo de codificacion / decodificacion base64 usando PS" -ForegroundColor Green
Write-Host "Codificando un archivo de texto"
#
#Se va a leer el contenido de l archivo de texto
#
$inputfile = "C:\Users\elcha\Desktop\secret.txt"
$fc = Get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.GetBytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es: " $etext -ForegroundColor Green
#
#Decodificando contenido de un archivo
#
Write-Host "DECODIFICANDO el texto previo: "
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" c:\Users\elcha\Desktop\decode_secret.txt
$outfile12 = Get-Content c:\Users\elcha\Desktop\decode_secret.txt
Write-Host "El texto decodificado es el siguiente: " -ForegroundColor Green
Write-Host "DECODIFICADO: " $outfile12

#
##Datos: Pablo Emilio Guajardo De la Cruz
##Matrícula: 1727651
#
