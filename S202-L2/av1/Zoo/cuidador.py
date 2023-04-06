class CuidadorClass():
    def __init__(self, id: str, nome: str, documento: str) -> None:
        self.id = id
        self.nome = nome
        self.documento = documento

    def toDict(self):
        return {"id": self.id, "nome": self.nome, "documento": self.documento}