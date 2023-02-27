# HASH WEB

Podemos extraer el hash desde la web, pero siempre tiene sus limites, aun asi funciona de la misma manera que desde codigo.

- [CyberWarZone Online Favicon Checksum Tool](https://cyberwarzone.com/online-favicon-checksum-tool/)
- [RealFaviconGenerator](https://realfavicongenerator.net)

Con estos sitios podemos hacerlo rapidamente, pero hay que revisar con cuidado ya que no todos los dominios que les pasemos funcionaran correctamente.

En las siguientes herramientas podran ver con detalle:

- [Shodan Favicon Map](https://faviconmap.shodan.io)
- [Nmap Favicon](https://nmap.org/favicon/)
- [IconMap.io](https://iconmap.io)

# HashEXT-FAVICO

Para este caso tenemos tres archivos: uno para la extracción automática de la URL de cada sitio, `exturlapi.py`; en caso de que funcione, podemos utilizar el siguiente archivo, `hashfav.py`, para codificar el .ico en hash (Favicon MM3H). Este último nos devuelve `http.favicon.hash:hash`, que es lo que debemos colocar en Shodan.io.

En caso de que no funcione, podemos utilizar el último archivo que nos permitirá convertir directamente el .ico descargado.

Podemos emplear las siguientes URL para ese proceso:

- [Favicon Grabber](https://favicongrabber.com)
- [Favicon Grabber/Narendrad Wivedi](https://favicongrabber.narendradwivedi.org)
- [Icon Horse](https://icon.horse/icon/domain.com)
- [Icons Duck](https://icons.duckduckgo.com/ip3/domain) (puede llegar a funcionar en algunos casos)
- [Google Icon](https://www.google.com/s2/favicons?domain=midomain.com&sz=128)
- [Google Icon 2](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE>,SIZE,URL&url=http://banco.bradesco&size=128)

Una vez cumplido esto, también nos devolverá "Favicon Hash: hash obtenido", que debemos adicionar como en el paso anterior.

Toda la documentación de la API se puede encontrar aquí:

- [Github API](https://github.com/antongunov/favicongrabber.com)
- [Github API 2](https://github.com/antongunov/favicongrabber.com/blob/master/docs/API.md)
