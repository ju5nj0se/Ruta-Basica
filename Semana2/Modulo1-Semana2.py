
# Ingresar datos y validar datos
while True:
    try:
       Entrada = int(input("\nIngresa un calificacion(0-100)\n--> "))
    
    except ValueError:
        print("ERROR: INGRESO UN CARACTER")
   
    else:
        if Entrada >= 0 and Entrada <= 60:
            print("Reprobo")
            break
        elif Entrada > 60 and Entrada <= 100:
            print("Aprobo")
            break
        else:
            print("ERROR: INGRESE UN NUMERO DE 0 A 100")
    
    

#Ingresar lista de calificaciones y verificar con un numero para comparar
Calificaciones = int()
while True:
    CadCarac = input("Ingrese la lista de calificaciones, cada una separadas por comas: ")
    try:
        Calificaciones = list(map(float, CadCarac.split(",")))
    except ValueError:
        print("ERROR: Asegurese de haber ingresado las calificaciones bien")
    else:
        print("Los caracteres que ingreso son:", *Calificaciones)
        break

print("El promedio de las calificaciones es: ", sum(Calificaciones)/len(Calificaciones))

#Contar cuantos calificaciones son mayores al valor ingresado por el usuario
Comparador = int()
Mayores = int()
while True:
    try:
        Comparador = int(input("Ingrese un numero para contar cuantos numeros son mayores a ese numero en la lista de calificaciones\n--> "))
        
    except ValueError:    
        Comparador = int(input("ERROR"))

    else:
        for i in Calificaciones:
                if Comparador < i:
                    Mayores = Mayores + 1
        print(f"El numero de calificaciones mayores son: {Mayores}")
        break

#Contar cuantas calificaciones son mayores a la calificacion ingresada por el usuario
NumEspecifico = int()
Cont = int()
while True:
    try:
        NumEspecifico = int(input("Ingrese una calificacion a para ver cuantas veces esta esa calificacion en la lista de calificaciones\n--> "))
    except ValueError:
        print("ERROR: Asegurese de haber ingresado un numero")
        continue

    else:
        for i in range(len(Calificaciones)):
            if Calificaciones[i] > NumEspecifico:
                Cont = Cont +1
    break

print(f"La calificacion {NumEspecifico} esta {Cont} en la lista")

