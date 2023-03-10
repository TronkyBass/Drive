#Crear una lista (se pueden re definir) se definen entre []
lista = ["nahuel troncoso" , "tronkybass", True,1.70]

#imprimir una lista o un elemento de la misma
print (lista[0]) #imprimir un elemento de la lista por indice (El indice se genera por defecto, el primer elemento es 0)
print (lista) #imprimir lista

#Crear una tupla, se definen entre ()
tupla=("nahuel", "tronkybass",True,1.7) #conjunto de elementos que no se pueden modificar

#Modificar elemento de la lista o redefinir (por indice)
lista [2]= False
print (lista)

#Creando un set se define entre {}
conjunto = {"nahuel troncoso" , "tronkybass", True,1.70} #No se pude re definir ni acceder por indice. print (conjunto[2])-> No se puede

conjunto = {"nahuel troncoso" , "tronkybass", True,1.70, "nahuel troncoso", 1.70} #No puede tener elementos repetidos (los borra, permite eliminar datos duplicados)
print (conjunto)

#creando un diccionario estructura -> (se define entre {}, fomar 'key' : value y separamos con comas cada elemento)
diccionario = {
    'nombre' : "nahuel troncoso",
    'canal' : "tronkybass",
    'altura' : 1.70
    }
print (diccionario['canal']) #diccionario muestra por nombre asciado (no por indice)

#Funcion Tipo de dato
tipo_de_dato = type (diccionario["altura"])
print(tipo_de_dato)






