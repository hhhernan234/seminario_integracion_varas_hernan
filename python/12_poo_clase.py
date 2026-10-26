class Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

goku = Guerrero("Goku", "Saiyaijin")
vegeta = Guerrero("Vegeta", "Saiyaijin")
piccolo = Guerrero("Piccolo", "Namkiano")
hernan = Guerrero("Hernán", "Humano")