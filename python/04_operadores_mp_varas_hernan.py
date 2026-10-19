print("Operadores Aritméticos")
print("=====")
a = 10  # evidencias recolectadas
b = 5   # evidencias analizadas
print("a =", a)
print("b =", b)
print(" SUMA a + b =", a + b)
print(" RESTA a - b =", a - b)
print(" MULTIPLICACIÓN a * b =", a * b)
print(" DIVISIÓN a / b =", a / b)
print(" DIVISIÓN ENTERA a // b =", a // b)
print(" MÓDULO a % b =", a % b)
print(" POTENCIA a ** b =", a ** b)

print("Tabla de evidencias: 5 cajas del inspector Hernan Varas")
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

# Operadores de Comparación
print("Operadores de Comparación")
print("== Igual a: ", 5, "==", 5, "==", 5 == 5)
print("!= Distinto a: ", 5, "!=", 5, "==", 5 != 5)
print("< Menor que: ", 5, "<", 5, "==", 5 < 5)
print("> Mayor que: ", 5, ">", 5, "==", 5 > 5)
print("<= Menor o igual que: ", 5, "<=", 5, "==", 5 <= 5)
print(">= Mayor o igual que: ", 5, ">=", 5, "==", 5 >= 5)

# Operadores Lógicos
print("Operadores Lógicos")
print("Operador AND : (5==5) and (10>5) =", (5 == 5) and (10 > 5))
print("Operador OR : (5==5) or (10<5) =", (5 == 5) or (10 < 5))
print("Operador NOT : not(5==5) =", not (5 == 5))

tiene_orden_judicial = True
testigo_disponible = True
puede_allanar = tiene_orden_judicial and testigo_disponible
print("Puede allanar:", puede_allanar)

es_fiscal = False
tiene_orden_judicial = True
acceso_expediente = es_fiscal or tiene_orden_judicial
print("Acceso al expediente:", acceso_expediente)