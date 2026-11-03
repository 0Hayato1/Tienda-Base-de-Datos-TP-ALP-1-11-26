import sqlite3
conn = sqlite3.connect(r"C:\Users\Estudiante\Desktop\ \ESCUELA\Tienda.db")
cursor = conn.cursor()
print ("conexion establecida")


def mostrar_productos():
    cursor.execute("SELECT * FROM Tienda")
    productos = cursor.fetchall()

    if productos:
        for producto in productos:
            print(producto)
    else:
        print("No hay productos registrados.")


while True:
    print("\n===== MENU DE LA TIENDA =====")
    print("1. Mostrar todos los productos")
    print("2. Buscar por id")
    print("3. Agregar un producto")
    print("4. Modificar la cantidad de un producto")
    print("5. Eliminar un producto")
    print("6. Salir")

    opcion = input("Elegi una opcion: ")

    # 1. Mostrar todos los productos
    if opcion == "1":
        mostrar_productos()

    # 2. Buscar por id
    elif opcion == "2":
        id = input("Ingresa el id que queres buscar: ")

        cursor.execute(
            "SELECT * FROM Tienda WHERE ID = ?",
            (id,)
        )

        productos = cursor.fetchall()

        if productos:
            for producto in productos:
                print(producto)
        else:
            print("No se encontraron productos con ese id.")

    # 3. Agregar un producto
    elif opcion == "3":
        nombre = input("Ingresa el nombre del producto: ")
        cantidad = int(input("Ingresa la cantidad del producto: "))

        cursor.execute(
            "INSERT INTO Tienda (Producto, Cantidad) VALUES (?, ?)",
            (nombre, cantidad)
        )

        conn.commit()

        print("Producto agregado correctamente.")
        print("Tabla actualizada:")
        mostrar_productos()

    # 4. Modificar la cantidad de un producto
    elif opcion == "4":
        nombre = input("Ingresa el nombre del producto que queres modificar: ")
        cantidad = int(input("Ingresa la nueva cantidad: "))

        cursor.execute(
            "UPDATE Tienda SET Cantidad = ? WHERE Producto = ?",
            (cantidad, nombre)
        )

        conn.commit()

        print("Producto actualizado correctamente.")
        print("Tabla actualizada:")
        mostrar_productos()

    # 5. Eliminar un producto
    elif opcion == "5":
        nombre = input("Ingresa el nombre del producto que queres eliminar: ")

        cursor.execute(
            "DELETE FROM Tienda WHERE Producto = ?",
            (nombre,)
        )

        conn.commit()
        print("Producto eliminado correctamente.")

        print("Tabla actualizada:")
        mostrar_productos()

    # 6. Salir
    elif opcion == "6":
        print("Cerrando el programa...")
        break

    else:
        print("Opcion invalida. Elegi un numero del 1 al 6.")

conn.close()
print("Conexion cerrada.")