from abc import ABC, abstractmethod


class Funcionario(ABC):
    @abstractmethod
    def investigar(self):
        pass


class Inspector(Funcionario):
    def investigar(self):
        return "Hernan Varas interroga al sospechoso"


class Detective(Funcionario):
    def investigar(self):
        return "El detective revisa las cámaras de seguridad"


varas = Inspector()
ramirez = Detective()
print(varas.investigar())
print(ramirez.investigar())

# Una clase abstracta no se puede instanciar
try:
    funcionario = Funcionario()
except TypeError as error:
    print("Error:", error)
