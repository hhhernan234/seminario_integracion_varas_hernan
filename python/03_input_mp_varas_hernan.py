print("Incluir datos con el input")
nombre = input("Ingrese el nombre del denunciante: ")
print("Hola", nombre, "¡Bienvenido a la Comisaría!")
print("Hasta luego, " + nombre)

cantidad = int(input("¿Cuántas evidencias hay? "))
print(cantidad + 2)

print("CONVERSIONES")
print("==== COMISARÍA: REGISTRO DE MULTAS (Inspector Hernan Varas) =====")
nombre_infractor = input("Ingrese el nombre del infractor: ")
monto_multa = float(input("Ingrese el monto de la multa: "))
cantidad_infracciones = int(input("Ingrese la cantidad de infracciones: "))
total = monto_multa * cantidad_infracciones
print("El total a pagar por", nombre_infractor, "es:", round(total, 2))
print(f"El total a pagar por {nombre_infractor} es: {round(total, 2)}")