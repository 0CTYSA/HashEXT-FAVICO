import requests

# Solicitar el dominio al usuario
dominio = input("Ingrese el dominio (ejemplo: google.com): ")

# Construir la URL de la API con el dominio ingresado
url = f"https://favicongrabber.com/api/grab/{dominio}?pretty=true"

# Realizar la solicitud a la API
response = requests.get(url)

# Imprimir la respuesta de la API
print(response.json())
