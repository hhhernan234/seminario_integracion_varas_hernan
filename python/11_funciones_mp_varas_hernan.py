print("Expediente policial - Funciones")
print("Autor: Hernán Varas")

def abrir_expediente():
    print("Se registra la denuncia")
    print("¡Expediente abierto!")

abrir_expediente()
abrir_expediente()
abrir_expediente()
abrir_expediente()

def interrogar(detective):
    print(detective, "realiza un interrogatorio")

interrogar("Pablo Díaz")
interrogar("Juan Torres")
interrogar("Comisario Soto")
interrogar("Hernán Varas")

def calcular_evidencias(pruebas, peso):
    total = pruebas * peso
    return total

resultado = calcular_evidencias(4, 26)
print("El puntaje de evidencia del caso de Hernán Varas es:", resultado)

resultado = calcular_evidencias(4, 5000)
print("El puntaje de evidencia del caso Rojas:", resultado)


def formalizar_sospechoso(nombre, puntaje):
    if puntaje >= 80:
        print(f"Formalización de {nombre} realizada con éxito")
    else:
        print(f"{nombre} necesita más pruebas")

formalizar_sospechoso("Hernán Varas", 50)
formalizar_sospechoso("Carlos Rojas", 150)

nombre_detective: str = "Hernán Varas"
anios_servicio: int = 10
estatura: float = 1.74
es_activo: bool = True

def multiplicador_pruebas(horas_investigacion: float, anios: int) -> float:
    return horas_investigacion * anios

puntaje: float = multiplicador_pruebas(15.5, 2)
print("Puntaje calculado", puntaje)
