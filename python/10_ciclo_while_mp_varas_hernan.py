print("Expediente policial - Ciclo while")
print("Autor: Hernán Varas")

evidencia = 20
while evidencia < 100:
    print("Hernán Varas está recopilando evidencia:", evidencia)
    evidencia += 20

print("¡Hernán Varas completó el expediente!")

horas = 24
while horas > 0:
    print("El sospechoso lleva detenido, quedan", horas, "horas de plazo")
    horas -= 6

print("Se terminó el plazo de detención")

print("Continue y break")

dia = 0
while dia < 10:
    dia += 1
    if dia == 4:
        print("Día 4: Hernán Varas declara en el tribunal")
        continue
    print("Día", dia, "de investigación")
    if dia == 8:
        print("Cierre del expediente")
        break

sectores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sector in sectores:
    if sector == 3:
        print("Zona acordonada por la policía")
        continue  # Salta al siguiente sector sin ejecutar lo de abajo
    print(f"Continúa con el siguiente sector (Sector actual: {sector})")
    if sector == 7:
        print("Se encontró la evidencia, detener la búsqueda")
        break
