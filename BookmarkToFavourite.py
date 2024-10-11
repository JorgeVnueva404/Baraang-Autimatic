import requests
from PIL import Image
from io import BytesIO
from Lib import shutil
import matplotlib.pyplot as plt
import FF

bookmarks = 'https://baraag.net/api/v1/bookmarks?limit=1'
ruta_archivo = 'JSON/archivo.json'
dato = FF.leer_json(ruta_archivo)
codigo = dato["palabra"]
counter = dato["numero"]


auth = {
    'Authorization': f"Bearer {codigo}"
}
respuesta = requests.get(bookmarks, headers=auth)

if respuesta.status_code == 200:
    compacto = respuesta.json() # Aquí estoy obteniendo la respuesta en formato JSON
    print(compacto)
    for lista in compacto:  # Aquí estoy leyendo cada elemento de la lista  
        linea = lista["media_attachments"]  # Acá busco la línea donde encuentro los media
        
        for diccionario in linea:
            print(counter)
            print(diccionario)
            img_response = requests.get(diccionario["url"])
            nombre_imagen = f"imagenes/Img{counter}.png"
            with open(nombre_imagen, 'wb') as handler:
                counter = 1 +counter
                handler.write(img_response.content)
            
        unbookmark=f'https://baraag.net/api/v1/statuses/{lista["id"]}/unbookmark'
        favourite=f'https://baraag.net/api/v1/statuses/{lista["id"]}/favourite'

        print(requests.post(favourite, headers=auth ))
        print(requests.post(unbookmark, headers=auth ))
        FF.modificar_json(ruta_archivo,counter)
        
else:
    print('Error:', respuesta.status_code, respuesta.text)