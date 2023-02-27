import requests
import json

# Solicitar el dominio al usuario
dominio = input("Ingrese el dominio (ejemplo: google.com): ")

# Construir la URL de la API con el dominio ingresado
url = f"https://favicongrabber.com/api/grab/{dominio}?pretty=true"

# Realizar la solicitud a la API
response = requests.get(url)

# Verificar si la respuesta es válida y convertirla a un diccionario de Python
try:
    data = json.loads(response.text)
except json.decoder.JSONDecodeError:
    print("La respuesta de la API no es un JSON válido.")
    data = None

# Imprimir la respuesta de la API
if data:
    print(data)
else:
    print("No se pudo obtener la respuesta de la API.")
