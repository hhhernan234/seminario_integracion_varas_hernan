print("Incluir datos con el input")
nombre = input("Ingrese su nombre: ")
print("Hola", nombre, "¡Bienvenido a Python!")
print("Hasta Luego"+nombre)

cantidad= int(input("¿Cuantas rosquillas hay"))
print(cantidad+2)

print("CONVERSIONES")
print("==== TIENDA DE APU=====")
nombre_cliente = input("Ingrese su nombre: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad_producto = int(input("Ingrese la cantidad del producto: "))
total = precio_producto * cantidad_producto
print("El total a pagar por", nombre_cliente, "es:",round(total,2))
print(f"El total a pagar por {nombre_cliente} es: {round(total,2)}")