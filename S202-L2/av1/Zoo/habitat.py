from cuidador import CuidadorClass

class HabitatClass():
    def __init__(self, id: str, nome: str, tipoAmbiente: str, cuidador: CuidadorClass) -> None:
        self.id = id
        self.nome = nome 
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador

    def toDict(self):
        return {"id": self.id, "nome": self.nome, "tipoAmbiente": self.tipoAmbiente, "cuidador": self.cuidador.toDict()}