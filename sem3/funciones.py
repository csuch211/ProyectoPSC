#Funciones sin parametros que modifican o imprimen algo

def saludo():
    print("Hola a todos")

def incrementar_puntaje():
    global score
    score += 1
    

#Funciones sin parametros que regresan algo

def valor_cero():
    return 0

def forma_de_saludar():
    return "Saludo a todo el mundo"


saludo ()
incrementar_puntaje()
a = valor_cero()
print(a)

#Funciones con argumentos que no tienen return
def saludo_especial(nombre):
    print(f"Hola {nombre} mucho gusto.")

#Funciones con argumento que devuelven algo

def suma(a, b):
    return a + b

saludo_especial("Pepito")

suma_total = suma(10, 7)
print(suma_total)







