from animal import AnimalClass
from database import DatabaseClass
from cuidador import CuidadorClass
from habitat import HabitatClass

# CRUD class
class ZooDAOClass:
    def __init__(self):
        db = DatabaseClass(database="zoo", collection="animais")
        self.collection = db.collection

    def createAnimal(self, animal: AnimalClass) -> None:
        try:
            print(type(animal.habitat))# list
            print(type(animal.habitat[0]))# HabitatClass

            #converting to dict for JSON encoding
            for i in range(len(animal.habitat)):
                animal.habitat[i] = animal.habitat[i].toDict()

            result = self.collection.insert_one({"id": animal.id, "nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": animal.habitat})
            print(f"Animal {animal.nome} created with id: {animal.id}")
        except Exception as error:
            print(f"An error occurred while creating this animal: {error}")

    def readAnimal(self, animal_id: str) -> AnimalClass:
        try:
            animal = self.collection.find_one({"id": animal_id})
            if animal:
                print(f"Animal found: {animal}")

                #parsing form Dict to AnimalClass object
                habitatList = []
                for i in range(len(animal["habitat"])):
                    caregiverDict = animal["habitat"][i]["cuidador"]
                    caregiverObj = CuidadorClass(caregiverDict["id"], caregiverDict["nome"], caregiverDict["documento"])
                    habitatDict = animal["habitat"][i]
                    habitatObj = HabitatClass(habitatDict["id"], habitatDict["nome"], habitatDict["tipoAmbiente"], caregiverObj)
                    habitatList.append(habitatObj)

                animalObj = AnimalClass(animal["id"], animal["nome"], animal["especie"], animal["idade"], habitatList)
                return animalObj
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while searching this animal: {error}")
            return None

    def updateAnimal(self, animal: AnimalClass) -> None:
        try:
            #converting to dict for JSON encoding
            for i in range(len(animal.habitat)):
                animal.habitat[i] = animal.habitat[i].toDict()

            result = self.collection.update_one({"id": animal.id}, {"$set": {"nome": animal.nome, "especie": animal.especie, "idade": animal.idade, "habitat": animal.habitat}})
            if result.modified_count:
                print(f"Animal {animal.id} updated")
            else:
                print(f"No animal found with id {animal.id}")
        except Exception as error:
            print(f"An error occurred while updating this animal: {error}")

    def deleteAnimal(self, animal_id: str) -> None:
        try:
            result = self.collection.delete_one({"id": animal_id})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
        except Exception as error:
            print(f"An error occurred while deleting this animal: {error}")
