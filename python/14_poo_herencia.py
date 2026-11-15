class Personaje:
    nombre: str
    raza: str
    def __init__(self, nombre:str, raza:str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

class Saiyajin(Personaje):
    def __init__(self, nombre: str, raza: str):
        super().__init__(nombre, raza)

        def muestra_nombre(self):
            print("Nombre: ", self.nombre)

    
goku = Personaje("Goku", "Saiyajin")
vegeta = Personaje("Vegeta", "Saiyajin")
piccolo = Personaje("Piccolo", "Namkiano")
roberto = Personaje("Roberto", "Humnao")

goku.mostrar_info()
vegeta.mostrar_info()
piccolo.mostrar_info()
roberto.mostrar_info()