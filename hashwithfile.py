import mmh3, base64

filepath = input("Ingrese la ruta del archivo de imagen: ")

with open(filepath, "rb") as image_file:
    encoded_string = base64.encodebytes(image_file.read())
    favicon = encoded_string
    hash_del_archivo = mmh3.hash(favicon)

print("El hash del archivo es:", hash_del_archivo)
