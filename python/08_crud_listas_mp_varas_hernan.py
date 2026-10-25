print("\n==== CRUD de Expedientes Policiales en Python ====")
expedientes_policiales = [
    {"id": 1, "numero_caso": "EXP-2026-001", "ciudadano": "Carlos Mendoza", "delito": "Robo", "estado": "Abierto"},
    {"id": 2, "numero_caso": "EXP-2026-002", "ciudadano": "María Torres", "delito": "Estafa", "estado": "En investigación"},
    {"id": 3, "numero_caso": "EXP-2026-003", "ciudadano": "Jorge Ruiz", "delito": "Alteración del orden", "estado": "Cerrado"},
]

id_publico = 4

def create():
    global id_publico
    print("\n--- Registrar Nuevo Expediente ---")
    numero_caso = input("Ingrese el número de caso (ej. EXP-2026-004): ")
    ciudadano = input("Ingrese el nombre del ciudadano implicado: ")
    delito = input("Ingrese el tipo de delito o infracción: ")
    estado = input("Estado [Abierto, En investigación, Cerrado, Archivo]: ")
    
    nuevo_expediente = {
        "id": id_publico,
        "numero_caso": numero_caso,
        "ciudadano": ciudadano,
        "delito": delito,
        "estado": estado
    }
    expedientes_policiales.append(nuevo_expediente)
    print(f"Expediente {numero_caso} registrado con éxito con ID {id_publico}.")
    id_publico += 1

def read():
    print("\n--- Lista de Expedientes Policiales ---")
    for exp in expedientes_policiales:
        print(f"ID: {exp['id']} | Caso: {exp['numero_caso']} | Ciudadano: {exp['ciudadano']} | Delito: {exp['delito']} | Estado: {exp['estado']}")

def update():
    print("\n--- Actualizar Expediente ---")
    try:
        id_update = int(input("Ingrese el ID del expediente a modificar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
        
    for exp in expedientes_policiales:
        if exp["id"] == id_update:
            exp["numero_caso"] = input("Ingrese el nuevo número de caso: ")
            exp["ciudadano"] = input("Ingrese el nuevo nombre del ciudadano: ")
            exp["delito"] = input("Ingrese el nuevo delito: ")
            exp["estado"] = input("Ingrese el nuevo estado: ")
            print("Expediente policial actualizado correctamente.")
            return
    print("No se encontró un expediente con ese ID.")

def delete():
    print("\n--- Eliminar Expediente ---")
    try:
        id_delete = int(input("Ingrese el ID del expediente a eliminar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
        
    for exp in expedientes_policiales:
        if exp["id"] == id_delete:
            expedientes_policiales.remove(exp)
            print("Expediente policial eliminado correctamente.")
            return
    print("No se encontró un expediente con ese ID.")

def menu():
    while True:
        print("\n=== SISTEMA DE EXPEDIENTES POLICIALES ===")
        print("1. Registrar nuevo expediente")
        print("2. Listar expedientes")
        print("3. Actualizar expediente")
        print("4. Eliminar expediente")
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
            print("Saindo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()