import glob
import importlib

# adapting imports dinamically
modules = glob.glob("Zoo/*.py")
for module in modules:
    module_name = module.split("/")[-1].split(".")[0]
    importlib.import_module(f"Zoo.{module_name}")

class CuidadorClass():
    def __init__(self, id: str, nome: str, documento: str) -> None:
        self.id = id
        self.nome = nome
        self.documento = documento