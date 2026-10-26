print("Funciones")
print("Autor: Hernán Varas")

def kamehameha():
    print("Goku concentra su energía")
    print("!kamehameha")

kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegeta")
atacar("Piccolo")
atacar("Hernán Varas")

def calcular_poder(poder, ataques):
    danio = poder*ataques
    return danio

resultado = calcular_poder(4,26)
print("El poder de Hernán Varas es:", resultado)

resultado = calcular_poder(4,5000)
print("El poder de Goku:", resultado)


def transformar_saiyajin(nombre, poder):
    if poder >= 9000:
        print(f"Transformación de {nombre} a SuperSaiyajin exitosa")
    else:
        print(f"{nombre} Necesita aumentar tu poder")

transformar_saiyajin("Hernán Varas", 5000)
transformar_saiyajin("Gohan", 15000)

nombre_personaje: str = "Goku"
edad: int = 33
altura: float=1.74
es_activo= bool=True

def multiplicador_poder(entrenamiento:float, edad:int)->float:
    return entrenamiento*edad

poder:float= multiplicador_poder(15.5,2)
print("Poder calculado", poder)

