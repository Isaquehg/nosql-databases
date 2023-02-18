from elefante import Elefante

nome = input("Nome do elefante: ")
idade = int(input("Idade do elefante: "))
especie = input("Especie do elefante: ")
cor = input("Cor do elefante: ")
tamanho = input("Tamanho do elefante: ")

e1 = Elefante(nome, idade, especie, cor, "PpPaAaHhHh", tamanho)
e1.emitir_som()

if((especie == "Africano") & (idade < 10)):
    e1.som = "Paaah"
    e1.tamanho = "Pequeno"
    e1.cor = "Beje"
elif((especie == "Africano") & (idade >= 10)):
    e1.som = "PAHHHHHH"
    e1.tamanho = "Grande"
    e1.cor = "Cinza"

print("Novo Som: ")
e1.emitir_som()
print(f"Novo Tamanho: {e1.tamanho}")
print(f"Nova Cor: {e1.cor}")