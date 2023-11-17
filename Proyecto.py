#Considerar en Productos, StockReal es la cantidad del producto actual
#Y StockCritico es cual es el minimo de stock que tiene que tener el producto

#PRODUCTOS Y TIPOPRODUCTOS SON ACCESO RELATIVO Y MARCAS ACCESO SECUENCIAL

import os

# Constantes según las especificaciones
tamaño_reg_productos = 73
tamaño_reg_tipo_productos = 29
posicion_overflow_productos = 101
posicion_overflow_tipos_productos = 21

def HashProductos(id_producto):
    return int(id_producto[-2:])


def HashTiposProductos(id_tipo):
    return int(id_tipo[-2:])


def agregar_datos_producto(id_producto, nombre_Archivo, PosicionHash, overflow=False):
    nombre = input("Ingrese el Nombre del producto: ")
    marca_id = input("Ingrese el Id de la Marca del producto: ")
    id_tipo = input("Ingrese el Id del Tipo de producto: ")
    stock_real = input("Ingrese el Stock Real: ")
    stock_critico = input("Ingrese el Stock Crítico: ")
    
    if not validar_existencia(marca_id, "MARCAS.TXT"):
        agregar_marca(marca_id)
    
    if not validar_existencia(id_tipo, "TIPOSPRODUCTOS.DAT"):
        agregar_tipo_producto(id_tipo)
    
    guardar_producto(nombre_Archivo, PosicionHash, id_producto, nombre, marca_id, id_tipo, stock_real, stock_critico, overflow)

def validar_existencia(id_entidad, nombre_Archivo):
    with open(nombre_Archivo, "r") as archivo:
        return any(id_entidad in line for line in archivo)

def agregar_marca(marca_id):
    with open("MARCAS.TXT", "a") as archivo:
        archivo.write(f"{marca_id}\n")

def agregar_tipo_producto(id_tipo):
    with open("TIPOSPRODUCTOS.DAT", "a") as archivo:
        archivo.write(f"{id_tipo}\n")

def encontrar_en_overflow(id_producto, nombre_Archivo, overflow_PosicionHash):
    with open(nombre_Archivo, "r") as archivo:
        for i, line in enumerate(archivo):
            fields = line.strip().split(" ")
            if fields[0] == id_producto and fields[-1] == "SI":
                return i
    return -1

def guardar_producto(nombre_Archivo, PosicionHash, id_producto, nombre, marca_id, id_tipo, stock_real, stock_critico, overflow=False):
    registro = f"{id_producto}{nombre}{marca_id}{id_tipo}{stock_real}{stock_critico}SI\n"
    
    if overflow:
        with open(nombre_Archivo, "a") as archivo:
            archivo.write(registro)
    else:
        with open(nombre_Archivo, "r+") as archivo:
            archivo.seek(PosicionHash * tamaño_reg_productos)
            archivo.write(registro)

def AgregarProducto():
    id_producto = input("Ingrese el Id del producto: ")
    PosicionHash = HashProductos(id_producto)
    nombre_Archivo = "PRODUCTOS.DAT"
    
    with open(nombre_Archivo, "r") as archivo:
        archivo.seek(PosicionHash * tamaño_reg_productos)
        record = archivo.read(tamaño_reg_productos)
        
        if not record.strip():
            agregar_datos_producto(id_producto, nombre_Archivo, PosicionHash)
        else:
            overflow_PosicionHash = encontrar_en_overflow(id_producto, nombre_Archivo, posicion_overflow_productos)
            if overflow_PosicionHash != -1:
                print(f"Error: El Id del producto {id_producto} ya existe.")
            else:
                agregar_datos_producto(id_producto, nombre_Archivo, overflow_PosicionHash, overflow=True)


def ModificarMarca():
    marca_id = input("Ingrese el Id de la marca: ")
    nombre_Archivo = "MARCAS.TXT"

    if not validar_existencia(marca_id, nombre_Archivo):
        print(f"Error: La marca con Id {marca_id} no existe.")
        return

    nuevo_nombre = input("Ingrese el nuevo Nombre de la marca: ")

    modificar_marca(nombre_Archivo, marca_id, nuevo_nombre)

def modificar_marca(nombre_Archivo, marca_id, nuevo_nombre):
    nuevas_lineas = []

    with open(nombre_Archivo, "r") as archivo:
        for line in archivo:
            fields = line.strip().split(";")
            if fields[0] == marca_id and fields[-1] == "SI":
                nueva_linea = f"{marca_id};{nuevo_nombre};SI\n"
                nuevas_lineas.append(nueva_linea)
            else:
                nuevas_lineas.append(line)


    with open(nombre_Archivo, "w") as archivo:
        archivo.writelines(nuevas_lineas)


def EliminarTipoProducto():
    return







while True:
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        AgregarProducto()
        print("Se Completo la operacion. ")
    elif opcion == 2:
        ModificarMarca()
    elif opcion == 3:
        EliminarTipoProducto()
    else:
        break