#Ejemplo

edad = 13
if edad >=18: 
    print("podes pasar")
else: 
    print("no podes pasar")
    
#Podemos introducirla en una base de datos y compararlos  
 
Contraseña_almasenada= "123456"
Contraseña_introducida= "12344444"    
if Contraseña_almasenada == Contraseña_introducida:
    print("Ingrasando")
else: print("contraseña erronea, vuelva a introducirla")

#Elif si hay varias condiciones

Ingreso_mensul = 1005
tus_gastos = 505


if Ingreso_mensul >10000: #if anidados
    if tus_gastos <7000:
        print("Estas bien BB")
    else: 
        print("estas gastando mucho BB")
elif Ingreso_mensul > 1000: #se pueden poner varias condiciones, si no se cumple ni el if ni ninguno de los elif imprime else
    print("estas bien en latinoamerica")
    
  
else: print("sos pobre")

