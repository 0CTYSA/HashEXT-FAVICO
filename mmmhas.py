import os
import hashlib
import mmh3

# Función para buscar activos relacionados con un ícono en base al iconhash md5


def search_assets_by_md5_icon(iconhash, file_name):
    md5_value = hashlib.md5(iconhash.encode()).hexdigest()

    print(f"- Archivo: {file_name}")
    print(f"Activos relacionados con el icono (MD5: {md5_value}):")

# Función para buscar activos relacionados con un ícono en base al iconhash mmh3


def search_assets_by_mmh3_icon(iconhash, file_name):
    mmh3_value = mmh3.hash(iconhash)

    print(f"- Archivo: {file_name}")
    print(f"Activos relacionados con el icono (MMH3: {mmh3_value}):")


# Leer contenido de los archivos en la carpeta "icon/"
for file in os.listdir("icon/"):
    with open(os.path.join("icon", file), 'rb') as f:
        file_content = f.read()
        file_name = file

        # Calcular los valores de MD5 y MMH3
        iconhash_md5 = hashlib.md5(file_content).hexdigest()
        iconhash_mmh3 = str(mmh3.hash(file_content))

        # Buscar activos relacionados con los valores de MD5 y MMH3
        search_assets_by_md5_icon(iconhash_md5, file_name)
        search_assets_by_mmh3_icon(iconhash_mmh3, file_name)
        print()  # Imprimir una línea en blanco para separar los resultados
