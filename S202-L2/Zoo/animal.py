from habitat import HabitatClass
from typing import List

class AnimalClass():
    def __init__(self, id: str, nome: str, especie: str, idade: int, habitat: List[HabitatClass]) -> None:
        self.id = id
        self.nome = nome
        self.especie = especie 
        self.idade = idade 
        self.habitat = habitat