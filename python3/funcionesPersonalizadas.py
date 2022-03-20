''' Identificadores:
    variables: declarar
    constantes: declarar
    
01. Definir funciones sin parametro
    '''
from re import S


def MostrarSaludo(): #Firma
    print('Buenas noches')   #cuerpo
    
# 002. Invocar la funcion sin parametros

MostrarSaludo()

#03. Defenir funciones con parametros

def Sumar(num1, num2):
    #entrada
    resultado = 0
    
    #Proceso 
    resultado = num1 +  num2
    #Salida
    return resultado
# Invocar la  funcion
n1 = 23
n2 = 34 
Sumar(n1, n2)
Sumar(5+10,len("Henry"))
#Argumento: Valores  expresiones 
#Expresiones: Formulas  funciones
#Formula -> 5+10
#Funcion -> len(Paises)

    
    
    

    
    