from animal import Animal
from database import Database

class ZooDAO:
    def __init__(self):
        db = Database(database="zoo", collection="animais")
        self.collection = db.collection

    def createAnimal(self, animal: Animal) -> None:
        try:
            result = self.collection.insert_one({"_id": animal.id, "nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": animal.habitat})
            animal_id = str(result.inserted_id)
            print(f"Animal {animal.nome} created with id: {animal.id}")
        except Exception as error:
            print(f"An error occurred while creating this animal: {error}")

    def readAnimal(self, animal_id: str) -> Animal:
        try:
            animal = self.collection.find_one({"_id": animal_id})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while searching this animal: {error}")
            return None

    def updateAnimal(self, animal: Animal) -> None:
        try:
            result = self.collection.update_one({"_id": animal.id}, {"$set": {"nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": animal.habitat}})
            if result.modified_count:
                print(f"Animal {animal.id} updated")
            else:
                print(f"No animal found with id {animal.id}")
        except Exception as error:
            print(f"An error occurred while updating this animal: {error}")

    def deleteAnimal(self, animal_id: str) -> None:
        try:
            result = self.collection.delete_one({"_id": animal_id})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
        except Exception as error:
            print(f"An error occurred while deleting this animal: {error}")
