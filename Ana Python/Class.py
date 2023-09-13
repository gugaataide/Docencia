'''Classes sao fundamentais na Programação Orientada a Objetos.
    Servem para "Modelar" um objeto na vida real com atributos e comportamentos
    
    Atributos: Idade, Nome, Raça
    Comportamentos: Latir, Deitar, Rolar

'''

#Implementação
class cachorro ():
    nome: str
    idade: int
    raca:str
    
    #toda classe precisa de um construtor
    def __init__(self, nome_input, idade_input, raca_input):
        self.nome = nome_input
        self.idade = idade_input
        self.raca = raca_input
    
    def latir (self):
        print(f"{self.nome} latiu")
        
    def se_apresentar (self):
        print(f"Olá! Me chamo {self.nome}, sou um cachorro da raça {self.raca} e tenho {self.idade} meses")
        

#Exemplo
Kata = cachorro("Kattaryna", 12, "Salsicha")
Kata.se_apresentar()
Kata.latir()
Kata.latir()
Kata.latir()

Karol = cachorro("Karol", 4, "Arlequim")
Karol.se_apresentar()
Karol.latir()



''' PRÁTICA
   1. Crie uma classe que modele algo do seu dia a dia, com atributos e métodos
'''