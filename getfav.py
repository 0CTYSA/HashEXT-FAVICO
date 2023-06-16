import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from urllib.parse import urljoin


def get_favicon_url(site_url):
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

    return favicon_url


print(get_favicon_url('https://secure.ficohsa.com/'))
