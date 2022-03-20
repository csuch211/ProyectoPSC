archivo = open("copia_ejemplo.txt","r")

contenido = archivo.read()

print(contenido)

contenido = archivo.readline()

print(f"El contenido de la primera linea es {contenido}")

contenido = archivo.readline()

print(f"El contenido de la segunda linea es {contenido}")

contenido = archivo.readline()

print(f"El contenido de la tercera linea es {contenido}")

archivo.close()

with open("nuevo_archivo.txt","w") as archivo_nuevo:
    archivo_nuevo.write("Esta es mi tercera linea\n")
    archivo_nuevo.write("Esta es mi cuarta linea\n")

archivo_leer = input("Introduce el archivo a leer: ")

try:
    with open(archivo_leer) as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("No he encontrado el archivo, compruebe el nombre. ")
