#1. ENTRADA DE DATOS
Entrada = float(input())

if Entrada > 0 and type(Entrada) == float:
    print("Valido")


#2. ingresar una lista de calificaciones  y un valor especifico para comparar
Cadena = input("Ingrese las calificaciones separadas por comas: ")
Calificaciones = list(map(float, Cadena.split(",")))
print(Calificaciones)
Comparador = input("Ingrese el valor a comparar a las calificaciones para ver si fueron aprobadas o no aprobadas")

#3. utilizar condicionales para determinar el estado de aprobacion
# #4. utilizar un ciclo para contar cuantas calificaciones son mayores que el valor especificado 
Aprobados = 0
Desaprobados = 0
for i in Calificaciones:
    if i > Comparador:
        Aprobados = Aprobados + 1
        print("Aprobado")
    elif i < Comparador:
        Desaprobados = Desaprobados + 1
        print("Desaprobados")



#5. emplear un ciclo for para verificar la presencia de una calificacion especifica y contar cuantas veces aparece (utilizar break y continue)
    


