class Pessoa:
    #atributos
    nome = ""
    idade = 0

    #Construtor
    #Passagem de parametro
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #metodo
    def caminhar(self):
        print("Pessoa está caminhando...")

    def dormir(self):
        print("Está na hora de dormir!...")
#Instanciando a classe
p = Pessoa("Paulo", 25)
#chamada de atributo
print("Nome da pessoa:", p.nome)
print("Idade da pessoa:", p.idade)
p.caminhar()
p.dormir()
#Você pode definr quantos metodos forem necessarios na sua classe
#Construtores: O metodo construtor ele eo responsavel por incializar um objeto,
#Na criação do objeto já ser difinido valores ao mesmo
#Exemplo: Quando uma pessoa nasce ela já tem um nome
