import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from urllib.parse import urljoin, urlparse
import os


def download_favicon(site_url):
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    icon_link = None
    for link in soup.find_all('link'):
        if 'rel' in link.attrs:
            rel_value = link['rel'][0].lower() if isinstance(
                link['rel'], list) else link['rel'].lower()
            if rel_value in ['icon', 'shortcut icon', 'apple-touch-icon', 'apple-touch-icon-precomposed', 'mask-icon']:
                icon_link = link
                break
        if 'href' in link.attrs and 'manifest' in link['href']:
            manifest_response = requests.get(urljoin(site_url, link['href']))
            if manifest_response.status_code == 200:
                manifest_data = manifest_response.json()
                if 'icons' in manifest_data:
                    icon_link = manifest_data['icons'][0]['src']
                    break

    if icon_link is None or not isinstance(icon_link, Tag) or 'href' not in icon_link.attrs:
        og_image = soup.find('meta', property='og:image')
        if og_image is not None and isinstance(og_image, Tag) and 'content' in og_image.attrs:
            favicon_url = og_image['content']
        else:
            favicon_url = '/favicon.ico'
    else:
        favicon_url = icon_link['href']

    if isinstance(favicon_url, list):
        favicon_url = favicon_url[0]

    favicon_url = urljoin(site_url, favicon_url)

    # Obtener el nombre del icono
    parsed_url = urlparse(site_url)
    icon_name = os.path.basename(parsed_url.netloc)

    # Descargar el favicon con el formato específico
    response = requests.get(favicon_url)
    if response.status_code == 200:
        extension = favicon_url.split(".")[-1].lower()
        if extension in ["ico", "png", "jpg", "jpeg", "gif"]:
            icon_extension = extension
        else:
            icon_extension = "ico"

        # Crear la carpeta "icon" si no existe
        if not os.path.exists("icon"):
            os.makedirs("icon")

        # Guardar el icono en la carpeta "icon"
        with open(f"icon/{icon_name}.{icon_extension}", "wb") as file:
            file.write(response.content)
        print(f"Icono guardado: {icon_name}.{icon_extension}")
    else:
        print(f"No se pudo descargar el icono para: {site_url}")
        print(f"Ruta URL del favicon: {favicon_url}")


# Ingresar las URLs desde la consola, una por línea
print("Pega las URLs aquí (una por línea). Presiona Enter en una línea vacía para finalizar:")
urls = []
while True:
    url = input()
    if not url:
        break
    urls.append(url)

# Descargar los favicons de las URLs proporcionadas
for url in urls:
    download_favicon(url)
