import mmh3  # Importamos el módulo mmh3 para calcular el hash del icono de favoritos
import sys  # Importamos el módulo sys para obtener argumentos de línea de comandos
import codecs  # Importamos el módulo codecs para codificar el contenido de la respuesta en base64
import requests  # Importamos el módulo requests para hacer solicitudes HTTP

# Verificamos si se proporcionó un argumento de línea de comandos
if len(sys.argv) != 2:
  print(f"Usage: {sys.argv[0]} [Favicon URL]")  # Imprimimos un mensaje de uso
  sys.exit(0)  # Salimos del programa

try:
  # Hacemos una solicitud HTTP GET a la URL proporcionada como argumento de línea de comandos
  response = requests.get(sys.argv[1])
  # Codificamos el contenido de la respuesta en base64
  favicon = codecs.encode(response.content, 'base64')
  # Calculamos el hash del icono de favoritos utilizando la función hash del módulo mmh3
  hash = mmh3.hash(favicon)
  print(f"Favicon Hash: {hash}")  # Imprimimos el hash del icono de favoritos
except Exception as e:  # Capturamos cualquier excepción que se produzca
  print(f"Error occured as: {e}",
        file=sys.stderr)  # Imprimimos el error en la salida de error estándar
