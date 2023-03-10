#Creando un conjunto con Set
conjunto=set(["dato1","dato2"])

print(conjunto)

#metiendo un conjunto dentro de otro conjunto

conjuntoA= frozenset(["dato1","dato2"])
conjuntoB= {conjuntoA,"dato3"}
print(conjuntoB)



#Teoria de conjuntos

Conjunto1 = {1,3,5,7}
Conjunto2 = {1,3,7}

#verificar si es un sub conjunto
resultadoA= Conjunto2.issubset(Conjunto1) #es conjunto2 un subconjunto de conjunto 1
resultadoB= Conjunto2 <= Conjunto1

print(resultadoA)

#verificando si es un super conjunto 
resultado1= Conjunto2.issuperset(Conjunto1) #es conjunto2 un subconjunto de conjunto 1
resultado2= Conjunto2 > Conjunto1

print(resultado2)

#verificar si hay algun elemento en comun
resultadoX= Conjunto1.isdisjoint(Conjunto2) #cuando solo hay un elemento que conincide deja de ser true "deja de ser completamente distinto"
print(resultadoX)



