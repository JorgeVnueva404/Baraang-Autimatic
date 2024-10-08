import requests
from PIL import Image
from io import BytesIO
from Lib import shutil
import matplotlib.pyplot as plt


counter = 1
favourites = 'https://baraag.net/api/v1/favourites?limit=2'

auth = {
    'Authorization': 'Bearer ***'
}
respuesta = requests.get(favourites, headers=auth)

if respuesta.status_code == 200:
    compacto = respuesta.json() # Aquí estoy obteniendo la respuesta en formato JSON
    print(compacto)
    for lista in compacto:  # Aquí estoy leyendo cada elemento de la lista  
        linea = lista["media_attachments"]  # Acá busco la línea donde encuentro los media
        
        for diccionario in linea:
            print(counter)
            print(diccionario)
            img_response = requests.get(diccionario["url"])
            nombre_imagen = f"imagen {counter}.png"
            with open(nombre_imagen, 'wb') as handler:
                counter = 1 +counter
                handler.write(img_response.content)
    
        unfavourite=f'https://baraag.net/api/v1/statuses/{lista["id"]}/unfavourite'
        print(requests.post(unfavourite, headers=auth ))
        
else:
    print('Error:', respuesta.status_code, respuesta.text)