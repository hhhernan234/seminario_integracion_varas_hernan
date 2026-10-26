class Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre: str, poder: int):
        self.nombre = nombre
        self.__poder = poder

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Poder ", self.__poder)

Goku = Guerrero("Goku", 9000)
Vegeta = Guerrero("Vegeta", 6000)
Picolo = Guerrero("Picolo", 10000)
Victor = Guerrero("Victor", 5000)

Goku.mostrar_info()
Vegeta.mostrar_info()
Picolo.mostrar_info()
Victor.mostrar_info()
print(Goku.nombre)
print(Vegeta.nombre)
print(Vegeta.__poder)