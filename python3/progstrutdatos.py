#TEMA 03: ESTRUCTURAS DE DATOS 
#3.1. LISTAS..SON MUTABLES Se puede modificar los datos
#01. Declaracion de listas de
Paises = ["Argentina", "Brasil", "Chile", "Peru", "Uruguay"]

#02. Operaciones basicas
#2.1. Recorrer listas
#print(type(Paises))
#print(Paises)
Paises[1] = "Alemania"
for i in range(Paises):
    print(i)
    
print(Paises[1])

del Paises[2]
print(Paises)

print("Cantidad de elementos: ", Paises)


Paises.append("China")
print(Paises)

#El metodo insert no devuelve nada
Paises.insert(2,"USA")
print(Paises)


cantidad = Paises.count()
print("Veces que aparece China",cantidad)
 
#sort ordena alfabeticamente ascendente
Paises.sort()
print(Paises)

x = "ITEC"
for i in x:
    print(i)