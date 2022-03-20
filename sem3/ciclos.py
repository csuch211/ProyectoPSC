frutas=["Banana","Manzana","Peras"]
usuarios = ["Maria","Juan","Pablo"]

for i in frutas:
    print(f"Tengo una {i} en mi lista de frutas.")


usuario = ""
while usuario not in usuarios:
    usuario = input("Ingrese su nombre:  ")

print("Has ingresado al sistema")

i = 0
while 5 > i:
    print("No estas en un ciclo infinito")
    i = i + 1 # i += 1