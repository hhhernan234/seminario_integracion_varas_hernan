poder = 2000
while poder < 10000:
    print("Vegeta esta entrenado")
    poder += 2000

print("!Vegeta alcanzo su objetivo")

while poder >0:
    print("Majin Buu tiene", poder, "de poder")
    poder -= 500

print("Majin buu quedo sin energia")

print("Continue y break")

dia = 0
while dia < 0:
    dia+=1
    if dia== 4:
        print("Dia 4: gohan estudia")
        continue
    print("Dia", dia, "Gohan entrena")
    if dia == 8:
        print("Fin del sistema")
        break


sectores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sector in sectores:
    # Si quieres evaluar el número de sector actual:
    if sector == 3:
        print("Zona destruida")
        continue  # Salta al siguiente sector sin ejecutar lo de abajo   
    print(f"Continua con el siguiente sector (Sector actual: {sector})")
    if sector == 7:
        print("Detener la busqueda")
        break