# HashEXT-FAVICO

Para este caso tenemos tres archivos: uno para la extracción automática de la URL de cada sitio, "exturlapi.py"; en caso de que funcione, podemos utilizar el siguiente archivo, "hashfav.py", para codificar el .ico en hash (Favicon MM3H). Este último nos devuelve "http.favicon.hash:hash", que es lo que debemos colocar en Shodan.io.

En caso de que no funcione, podemos utilizar el último archivo que nos permitirá convertir directamente el .ico descargado.

Podemos emplear las siguientes URL para ese proceso:

- <https://favicongrabber.com>
- <https://favicongrabber.narendradwivedi.org>
- <https://icon.horse/icon/domain.com>
- <https://icons.duckduckgo.com/ip3/domain> (puede llegar a funcionar en algunos casos)
- <https://www.google.com/s2/favicons?domain=midomain.com&sz=128>
- <https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE>,SIZE,URL&url=<http://banco.bradesco&size=128>

Una vez cumplido esto, también nos devolverá "Favicon Hash: hash obtenido", que debemos adicionar como en el paso anterior.

Toda la documentación de la API se puede encontrar aquí:

- <https://github.com/antongunov/favicongrabber.com>
- <https://github.com/antongunov/favicongrabber.com/blob/master/docs/API.md>
