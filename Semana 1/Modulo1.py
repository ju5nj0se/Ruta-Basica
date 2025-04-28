valido = False # variable de control del while
while valido == False:
    Producto = input("Ingrese el producto: ")#entrada de datos
    PrecioUnitario = float(input("Ingrese el precio unitario: "))
    CantidadProductos = float(input("Ingrese la cantidad de productos: "))
    Descuento = float(input("Ingrese porcentaje del descuento: "))
    if (PrecioUnitario > 0 and CantidadProductos > 0 and Descuento >= 0 and Descuento <= 100):
        valido = True # filtro que permite corregir si los input estan bien
    else:
        print("Compruebe que haya ingresado los datos correctamente :)\n ")
def ImprimirPrecio(PrecioUnitario, CantidadProductos, Descuento): #Funcion que evalua si es necesario imprimir descuento y lo imprime en caso de ser necesario
    if Descuento > 0 and valido == True:
        Total = float(PrecioUnitario*CantidadProductos)
        CompraDescuento = float(Total-((Descuento/100)*Total))
        print(f"¨\n- Producto: {Producto}\n- Precio Unitario: {PrecioUnitario}\n- Cantidad de productos: {CantidadProductos}\n- Total(Sin descuento):{Total}\n- Total(Con descuento): {CompraDescuento}\n- Descuento: {Descuento}%")
    elif Descuento == 0 and valido == True:
        Total = float(PrecioUnitario*CantidadProductos)
        print(f"¨\n- Producto: {Producto}\n- Precio Unitario: {PrecioUnitario}\n- Cantidad de productos: {CantidadProductos}\n- Total: {Total}\n- Descuento: {Descuento}%")

ImprimirPrecio(PrecioUnitario, CantidadProductos, Descuento)