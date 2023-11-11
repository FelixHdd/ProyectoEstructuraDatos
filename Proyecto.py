#Considerar en Productos, StockReal es la cantidad del producto actual
#Y StockCritico es cual es el minimo de stock que tiene que tener el producto

#PRODUCTOS Y TIPOPRODUCTOS SON ACCESO RELATIVO Y MARCAS ACCESO SECUENCIAL






largoproductos = 73
largotproductos = 29



def AgregarProducto():
    id = input("Ingrese ID del producto para agregar: ")
    #validar con el hashing si el ID ya existe en el PRODUCTOS.DAT 
    return

def ModificarMarca():
    return

def EliminarTipoProducto():
    return







while True:
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        AgregarProducto()
    elif opcion == 2:
        ModificarMarca()
    elif opcion == 3:
        EliminarTipoProducto()
    else:
        break