import base64
#
## Decodificamos la imagen dada:
#

uanl_img = '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'

uanl_img_bytes = uanl_img.encode('utf8')
with open('decoded_uanl.png','wb') as file_to_save:
    decoded_image_data = base64.decodebytes(uanl_img_bytes)
    file_to_save.write(decoded_image_data)

#
##Datos: Pablo Emilio Guajardo De la Cruz
##Matrícula: 1727651
#
