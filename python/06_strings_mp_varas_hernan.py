"""
Manejo de cadena de caracteres - Expedientes Policiales
"""

nombre1 = "Inspector Carlos Pérez"
print(f"Oficial 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")
nombre2 = "Comisionado Ana Gómez"
print(f"Oficial 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

## Funciones comunes de las variables String 
print("\n--- Funciones comunes de texto ---")
patrulla_1 = "PAT-01"
patrulla_2 = "PAT-02"
longitud_patrulla_1 = len(patrulla_1)
longitud_patrulla_2 = len(patrulla_2)
print("Nombre patrulla 1:", patrulla_1)
print("Longitud patrulla 1:", longitud_patrulla_1)
print("Nombre patrulla 2:", patrulla_2)
print("Longitud patrulla 2:", longitud_patrulla_2)
   
print("\n--- Convertir Mayúsculas y Minúsculas ---")
mensaje = "La unidad móvil patrulla el Distrito Metropolitano"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje Original:", mensaje)
print("Mensaje en Mayúscula:", mensaje_mayuscula)
print("Mensaje en Minúscula:", mensaje_minuscula)

print("\n--- Reemplazo de Substring ---")
mensaje = "El operativo se realizará en el sector Norte"
nuevo_mensaje = mensaje.replace("Norte", "Sur")
print("Mensaje Original:", mensaje)
print("Mensaje Reemplazado:", nuevo_mensaje)

print("\n--- Separación de cadenas en un arreglo ---")
distritos = "Norte, Sur, Centro, Eloy Alfaro"
print("Distritos:", distritos)
lista_distritos = distritos.split(",")
print(lista_distritos)
print("Primer distrito:", lista_distritos[0].strip())

print("\n--- Extraer subcadenas ---")
mensaje = "Atención código rojo en la central"
adjetivo = mensaje[9:14]
verbo = mensaje[19:23]
print("Palabra extraída 1:", adjetivo)
print("Palabra extraída 2:", verbo)

print("\n--- Comprobaciones útiles ---")
codigo = "EXP2026"
numero = "911"
nombre = "PoliciaNacional"
identificador = "CASO01"
print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())