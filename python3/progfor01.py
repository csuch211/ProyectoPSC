#ESTRUCTURAS DE CONTROL
# 1.- FOR

for i in range(5): # 5 cantidad de numeros que i toma 0,1,2,3,4
    print(i)

#2
for i in range(1,5):
    print(i)
    
#3
for i in range(1,6,2):
    print(i)
    
#4 --
for i in range(1,6):
    if i % 2 != 0:
        print(i)
        print("Iteración completa: ", i)
    else:
        continue
        print()
    
    
#5 -- Clausula break
# Imprimir hasta encontrar un multiplo de 3.
for i in range(1,6):
    if i % 3 != 0:
        print(i)
        print("Valor de i: ", i)
    else:
        break
        print("Iteracion completada: ", i)
        
print("Continua con las instrucciones.")
print("Continua con las instrucciones.")


#Utilizar variables acumulativas
# hallar las sumatoria de los cinco primeros numeros

S = 0

for i in range(1, 6):
    print(i, end="")
    S = S + i
print("Sumatoria", S)

#7 Matrices
#Imprimir de una matriz de 3 x 3:
#de los primeros numeros naturales 

N = 1
for i in range(3):
    for j in range(3):
        print(N, end="")
        N = N + 1
    print()    
    
r = int(input("Numero de iteraciones: "))
for i in range(1, r) :
    print(i) 
    
    
    