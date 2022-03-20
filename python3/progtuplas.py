#TUPLAS.. SON ESTRUCTURAS INMUTABLES
#01.dECLARACION DE TUPLAS Los datos no se modifican nicambian

Mercosur = ("Argentina","Brasil","Chile","Paraguay", "Uruguay")
PactoAndino = ("Bolivia","Colombia","Ecuador","Peru")

print(type(Mercosur))
print(Mercosur)

for i in Mercosur:
    print(i)
    
#Recuperar un valor especifico

#Sustituir
Mercosur[0] = "Panama"#No se puede modificar la tuplas

x=(0.18, 0.25, 0.09)
