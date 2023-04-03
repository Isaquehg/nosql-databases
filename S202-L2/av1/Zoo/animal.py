import glob
import importlib

# adapting imports dinamically
modules = glob.glob("Zoo/*.py")
for module in modules:
    module_name = module.split("/")[-1].split(".")[0]
    importlib.import_module(f"Zoo.{module_name}")

from habitat import Habitat

class Animal():
    def __init__(self, id: str, nome: str, especie: str, idade: int, habitat: Habitat) -> None:
        self.id = id
        self.nome = nome
        self.especie = especie 
        self.idade = idade 
        self.habitat = habitat