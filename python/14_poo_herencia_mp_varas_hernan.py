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

    def muestra_nombre(self):
        print("Nombre: ", self.nombre)


varas = Inspector("Hernan Varas", "Inspector")
ramirez = Funcionario("Ramirez", "Detective")
torres = Funcionario("Torres", "Perito")
fiscal = Funcionario("Mendoza", "Fiscal")

varas.mostrar_info()
ramirez.mostrar_info()
torres.mostrar_info()
fiscal.mostrar_info()
varas.muestra_nombre()
