from cuidador import Cuidador

class Habitat():
    def __init__(self, id: str, nome: str, tipoAmbiente: str, cuidador: Cuidador) -> None:
        self.id = id
        self.nome = nome 
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador