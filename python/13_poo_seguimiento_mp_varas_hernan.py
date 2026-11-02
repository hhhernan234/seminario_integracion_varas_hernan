class Expediente:
    nombre: str
    delito: str

    def __init__(self, nombre: str, nivel_riesgo: int):
        self.nombre = nombre
        self.__nivel_riesgo = nivel_riesgo  # atributo privado

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Nivel de riesgo ", self.__nivel_riesgo)

carlos = Expediente("Carlos Rojas", 90)
marta = Expediente("Marta Soto", 60)
luis = Expediente("Luis Pérez", 100)
hernan = Expediente("Hernán Varas", 50)

carlos.mostrar_info()
marta.mostrar_info()
luis.mostrar_info()
hernan.mostrar_info()
print(carlos.nombre)
print(marta.nombre)
# print(marta.__nivel_riesgo)  # Error: el atributo es privado (encapsulado)
