print("Expediente policial - Ciclo for")
print("Autor: Hernán Varas")

for revision in range(1, 6):
    print("El detective Hernán Varas revisa la hoja del expediente", revision)

for numero in range(1, 11):
    print("Evidencias", 5, "*", numero, "=", 5 * numero)

expedientes = [
    {"id": 1, "sospechoso": "Carlos Rojas", "delito": "Robo", "abierto": True},
    {"id": 2, "sospechoso": "Marta Soto", "delito": "Fraude", "abierto": True},
    {"id": 3, "sospechoso": "Luis Pérez", "delito": "Hurto", "abierto": False},
]

print("Lista de expedientes")
for expediente in expedientes:
    print(f"{expediente['id']} - sospechoso : {expediente['sospechoso']}")

detectives = ["Hernán Varas", "Pablo Díaz", "Juan Torres"]
for detective in detectives:
    print("Detective asignado: ", detective)

sospechosos = {
    "Carlos Rojas": 95,
    "Marta Soto": 60,
    "Luis Pérez": 85,
    "Hernán Varas (testigo)": 10
}

for nombre, puntaje in sospechosos.items():
    if puntaje >= 80:
        print(nombre, "puede ser formalizado")
    else:
        print(nombre, "necesita más pruebas")

print("Ciclo for anidados")

for detective in detectives:
    print("Turno de:", detective)

    for ronda in range(1, 4):
        print("Ronda de interrogatorio:", ronda)

print("Break y Continue")

for detective in detectives:
    if detective == "Juan Torres":
        break

    if detective == "Pablo Díaz":
        continue

    print("Detective", detective, "firma el expediente")
