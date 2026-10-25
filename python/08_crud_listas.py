print("==== Crud de listas en Python ====")
avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": True},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitán América", "estado": True},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": True},
]

id_publico = 4
def create():
    global id_publico
    print("Reclutar avenger")
    nombre = input("Ingrese el nombre del avenger: ")
    heroe = input("Ingrese el nombre del héroe: ")
    estado = input("Estado [Activo, Retirado, Desaparecido]")
    nuevo_avenger = {
        "id": id,
        "nombre": nombre,
        "estado": estado
    }
    avengers.append(nuevo_avenger)


def read():
    print("Lista de avengers")
    for avenger in avengers:
        print(f"{avenger['id']} - nombre: {avenger['nombre']}")

def update():
    id_update = int(input("id a modificar: "))
    for avenger in avengers:
        if avenger["id"] == id_update:
            avenger["nombre"] = input("Ingrese el nuevo nombre: ")
            avenger["heroe"] = input("Ingrese el nuevo nombre del héroe: ")
            avenger["estado"] = input("Ingrese el estado: ")
            print("Avenger actualizado")
            return
    print("No se encontró un avenger con ese id")

def delete():
    id_delete = int(input("id a eliminar: "))
    for avenger in avengers:
        if avenger["id"] == id_delete:
            avengers.remove(avenger)
            print("Avenger eliminado")
            return
    print("No se encontró un avenger con ese id")

def menu():
    while True:
        print("Avengers")
        print("1. Reclutar avenger")
        print("2. Listar avengers")
        print("3. Actualizar avenger")
        print("4. Eliminar avenger")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")

if _name_ == "_main_":
    menu()









