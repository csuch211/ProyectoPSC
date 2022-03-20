def saludo(nombre):
    print(f"Hola {nombre}!")
    print("Que gusto de conocerte!!")

saludo("Dali")


def saludo(nombre, edad):
    print(f"Hola {nombre}!")
    print(f"Tienes {edad} años. ")
    print("Que gusto de conocerte!!")

saludo("Maria",45)


def quitar_vida():
    #vida = 10
    global vida
    vida -=1
    print(vida)

def sumar_dos_numeros(a, b):
    return a + b


vida = 3

print(vida)
saludo("Maria",22)
quitar_vida()
print(vida)

frutas = ["Manzana","Chirimoya","Papaya","Chirimoya","Uvas","Chirimoya"]
texto = "Hola a todos"
texto = "Adios a todos"

print(frutas)
frutas[0] = "Naranjas"
print(frutas)

print(texto[8:])
print(texto[8:12])
print(texto)

otra_lista = frutas[:3]
mismas_frutas = []
print(otra_lista)
print(frutas)

frutas.append("Melon")

print(frutas)
print(mismas_frutas)
print()

print(frutas[::-1])
print(frutas)

frutas.pop()
print(frutas)

#a="Hola"
a = 10
b = 5
c= 12
resultado = sumar_dos_numeros(a, b)
print(resultado + c)