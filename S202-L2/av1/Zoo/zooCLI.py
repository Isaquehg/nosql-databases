from zooDAO import ZooDAOClass
from animal import AnimalClass
from habitat import HabitatClass
from cuidador import CuidadorClass

# UI
class ZooCLIClass():
    def __init__(self) -> None:
        self.zooDAO = ZooDAOClass()

    # Main UI
    def menu(self) -> None:
        menuOn = True

        print("-------------------------------------------------")
        print("Welcome to the Zoo!!")
        while (menuOn):
            print("Please, choose one option above: ")
            print("1 - Create a animal")
            print("2 - Read a animal")
            print("3 - Update a animal")
            print("4 - Delete a animal")
            option = int(input("Number: "))

            # CRUD UI
            if(option == 1):
                self.createAnimal()
            
            elif(option == 2):
                self.readAnimal()

            elif(option == 3):
                self.updateAnimal()

            elif(option == 4):
                self.deleteAnimal()

            else:
                print("Please, select a valid option!")
            
            yes = input("Do u wanna do another operation? (YES to continue)")
            if(yes != ("YES" or "yes")):
                menuOn = False

        print("Bye!")

    def createAnimal(self) -> None:
        print("Great! Let's create a caregiver!")
        caregiverID = input("Caregiver ID: ")
        caregiverName = input("Caregiver name: ")
        caregiverDoc = input("Caregiver document: ")
        caregiver = CuidadorClass(caregiverID, caregiverName, caregiverDoc)

        print("Now, let's create the habitat!")
        nHabitats = int(input("How many habitats do u wanna create?"))

        habitatList = []
        for i in range(0, nHabitats):
            habitatID = input("Habitat ID: ")
            habitatname = input("Habitat name: ")
            habitatType = input("Habitat ambient type: ")
            habitat = HabitatClass(habitatID, habitatname, habitatType, caregiver)
            habitatList.append(habitat)

        print("Good job! Now we'gonna create the animal!")
        animalID = input("Animal ID: ")
        animalName = input("Animal name: ")
        animalSpecies = input("Animal species: ")
        animalAge = int(input("Animal age: "))

        animal = AnimalClass(animalID, animalName, animalSpecies, animalAge, habitatList)
        self.zooDAO.createAnimal(animal)
        
    def readAnimal(self) -> None:
        print("Let's find your animal!")
        animalID = input("What's the animal ID? ")
        animal = self.zooDAO.readAnimal(animalID)

        if(animal != None):
            print(f"Name: {animal.nome}")
            print(f"Species: {animal.especie}")
            print(f"Age: {animal.idade}")
            for i in range(animal.habitat):
                print(f"Habitat {i}:")
                print(f"Name: {animal.habitat[i].nome}")
                print(f"Type: {animal.habitat[i].tipoAmbiente}")
                print(f"Caregiver Name: {animal.habitat[i].cuidador.nome}")
                print(f"Caregiver Doc: {animal.habitat[i].cuidador.documento}")
        
    def updateAnimal(self) -> None:
        print("Let's make some changes!")
        animalID = input("What's the animal ID? ")
        animalName = input("New animal's name: ")
        animalSpecies = input("New animal's species: ")
        animalAge = input("New animal's age: ")
        nHabitats = input("How many habitats do you wanna modify? ")

        print("First, let's change the caregiver!")
        caregiverID = input("Caregiver ID: ")
        caregiverName = input("New Caregiver Name: ")
        caregiverDoc = input("New Caregiver Document: ")
        caregiver = CuidadorClass(caregiverID, caregiverName, caregiverDoc)

        habitatList = []
        for i in range(0, nHabitats):
            habitatID = input("Habitat ID: ")
            habitatname = input("New Habitat Name: ")
            habitatType = input("New Habitat Ambient Type: ")
            habitat = HabitatClass(habitatID, habitatname, habitatType, caregiver)
            habitatList.append(habitat)

        
        newAnimal = AnimalClass(animalID, animalName, animalSpecies, animalAge, animalAge, habitatList)
        self.zooDAO.updateAnimal(newAnimal)

    def deleteAnimal(self) -> None:
        print("Are you sure about that? :(")
        animalID = input("What's the animal ID? ")
        self.zooDAO.deleteAnimal(animalID)

UI = ZooCLIClass()
UI.menu()
    