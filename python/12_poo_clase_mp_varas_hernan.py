class Expediente:
    nombre: str
    delito: str

    def __init__(self, nombre: str, delito: str):
        self.nombre = nombre
        self.delito = delito

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Delito ", self.delito)

carlos = Expediente("Carlos Rojas", "Robo")
marta = Expediente("Marta Soto", "Fraude")
luis = Expediente("Luis Pérez", "Hurto")
hernan = Expediente("Hernán Varas", "Extravío de documentos")

carlos.mostrar_info()
hernan.mostrar_info()
