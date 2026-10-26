for flexion in renge(1,6):
    print("Goku hace la flexion", flexion)

for tabla in renge(1,11):
    print("Multiplicacion", 5, "*", numero, "=", 5 * numero)

avengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": True},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitán América", "estado": True},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": True},
]

print("Lista de avengers")
for avenger in avengers:
    print(f"{avenger["id"]} - nombre : {avenger["nombre"]}")

nombres= ["Pedro", "Pablo", "Juan"]
for nombre in nombres:
    print("Nombre actual: ", nombre) 

guerreros = {
    "Goku": 9500,
    "Vegeta": 6000,
    "Gohan": 6000,
    "Piccolo": 4500
}

for nombre, poder in guerreros.items():
    if poder >= 9000:
        print(nombre, "puede enfrentar a Freezer")
    else:
        print(nombre, "necesita entrenar más")

print("Ciclo for anidados")

guerreros = ["Goku", "Vegeta", "Gohan", "Piccolo"]

for guerrero in guerreros:
    print("Turno de:", guerrero)

    for ronda in range(1, 4):
        print("Ronda:", ronda)

print("Break y Continue")

for guerrero in guerreros:
    if (guerrero == "Piccolo"):
        break

    if (guerrero == "Vegeta"):
        continue

    print("Guerrero", guerrero)        