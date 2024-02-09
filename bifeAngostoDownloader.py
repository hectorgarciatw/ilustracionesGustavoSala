# Lic. García Héctor
#! python3
# bifeAngostoDownloader.py - Descarga las últimas ilustraciones del ilustrador Gustavo Sala  

import os,requests,sys,bs4,webbrowser,re

url = 'https://www.pagina12.com.ar/autores/844-gustavo-sala'

os.makedirs('images', exist_ok=True)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
images= soup.find_all('img')
urls=[]
# Expresión regular para verificar el patrón que contiene el id de la imagen
patron = r"/\d{6}-"

#Reemplazamos la resolución
for image in images:
    src = image.get('src')
    if re.search(patron,src):
        urls.append(src.replace('300x200','960x640'))

for url in urls:
    #Guardamos la imagen
    imageFile = os.path.basename(url)
    dir = os.getcwd() + '/images'
    print('Descargando imagen ' + imageFile)
    imageFile = open(os.path.join(dir,imageFile),'wb')
    res = requests.get(url)
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

print('Imagenes descargadas correctamente')