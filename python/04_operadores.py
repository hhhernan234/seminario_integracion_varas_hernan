print("Operadores Aritméticos")
print("=====")
a = 10
b = 5
print("a =", a)
print("b =", b)
print(" SUMA a + b =", a + b)
print(" RESTA a - b =", a - b)
print(" MULTIPLICACIÓN a * b =", a * b)
print(" DIVISIÓN a / b =", a / b)
print(" DIVISIÓN ENTERA a // b =", a // b)
print(" MÓDULO a % b =", a % b)
print(" POTENCIA a ** b =", a ** b)

print("Tabla de multiplicar del 5")
print(5, "x", 1, "=", 5 * 1)
print(5, "x", 2, "=", 5 * 2)
print(5, "x", 3, "=", 5 * 3)    
print(5, "x", 4, "=", 5 * 4)
print(5, "x", 5, "=", 5 * 5)
print(5, "x", 6, "=", 5 * 6)
print(5, "x", 7, "=", 5 * 7)
print(5, "x", 8, "=", 5 * 8)
print(5, "x", 9, "=", 5 * 9)
print(5, "x", 10, "=", 5 * 10)

#Operadores de Comparación
print("Operadores de Comparación")
print("== Igual a: ", 5, "==", 5, "==", 5 == 5)
print("!= Distinto a: ", 5, "!=", 5, "==", 5 != 5)
print("< Menor que: ", 5, "<", 5, "==", 5 < 5)
print("> Mayor que: ", 5, ">", 5, "==", 5 > 5)
print("<= Menor o igual que: ", 5, "<=", 5, "==", 5 <= 5)
print(">= Mayor o igual que: ", 5, ">=", 5, "==", 5 >= 5)

#Operadores Lógicos
print("Operadores Lógicos")
print("Operador AND : (5==5) and (10>5) =", (5==5) and (10>5))
print("Operador OR : (5==5) or (10<5) =", (5==5) or (10<5))
print("Operador NOT : not(5==5) =", not(5==5))

tiene_dinero = True
tienda_abierta = True
puede_comprar = tiene_dinero and tienda_abierta
print("Puede comprar:", puede_comprar)

es_cliente_vip = False
tiene_dinero = True
acceso_credito= es_cliente_vip or tiene_dinero
print("Acceso a crédito:", acceso_credito)

