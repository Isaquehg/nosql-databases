from animal import Animal

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho
    
    def trombar(self):
        print(self.som)
    
    def mudar_tamanho(self, novoTamanho):
        self.tamanho = novoTamanho
