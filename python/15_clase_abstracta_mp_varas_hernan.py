class Funcionario:
    nombre: str
    cargo: str

    def __init__(self, nombre: str, cargo: str):
        self.nombre = nombre
        self.cargo = cargo

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Cargo ", self.cargo)


class Inspector(Funcionario):
    def __init__(self, nombre: str, cargo: str):
        super().__init__(nombre, cargo)

    def muestra_info(self):
        print("El inspector a cargo del expediente: ", self.nombre, "Cargo: ", self.cargo)


varas = Inspector("Hernan Varas", "Inspector")
ramirez = Inspector("Ramirez", "Detective")
varas.mostrar_info()
ramirez.mostrar_info()
varas.muestra_info()
ramirez.muestra_info()
