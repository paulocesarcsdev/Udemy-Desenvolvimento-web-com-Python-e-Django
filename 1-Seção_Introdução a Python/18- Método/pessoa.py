class Pessoa:
    #atributos
    nome = ""
    idade = 0

    #metodo
    def caminhar(self):
        print("Pessoa está caminhando...")
#chamado classe
p = Pessoa()
#chamada de atributo
p.nome = "Paulo"
p.idade = 25
print("Nome da pessoa:", p.nome)
print("Idade da pessoa:", p.idade)
p.caminhar()
