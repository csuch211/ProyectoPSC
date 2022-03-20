def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        

print(dividir(10, 0))
