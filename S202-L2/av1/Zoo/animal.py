from habitat import HabitatClass

class AnimalClass():
    def __init__(self, id: str, nome: str, especie: str, idade: int, habitat: HabitatClass) -> None:
        self.id = id
        self.nome = nome
        self.especie = especie 
        self.idade = idade 
        self.habitat = habitat