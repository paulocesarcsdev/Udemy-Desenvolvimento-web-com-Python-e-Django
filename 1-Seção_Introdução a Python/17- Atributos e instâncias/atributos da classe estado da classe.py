Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Pessoa:
	nome = ""
	idade = 0
	mae = ""

	
>>> #Instancia
>>> p = Pessoa()
>>> 
>>> #17. Atributos e instâncias - Como fazer uso dos atributos do objeto pessoa.
>>> # para acessar o atributo da classe nome usamos p.nome para ter acesso a váriavel do atributo
>>> p.nome = "Paulo César"
>>> p.idade = 20
>>> p.mae = "Maria"
>>> p
<__main__.Pessoa object at 0x036ABAF0>
>>> p.nome
'Paulo César'
>>> p.idade 24
SyntaxError: invalid syntax
>>> p.idade = 25
>>> #Muitas vezes será ouvido que as caracteristicas do objeto serem chamados de estado
>>> #Porque vc pode criar vários objetos da classe pessoa, cada objeto desse vai guardar uma informação individual e diferente.
>>> p2 = Pessoa()
>>> type(p2)
<class '__main__.Pessoa'>
>>> p2.nome
''
>>> #vou dar um estado difentre a instancia da classe pessoa.
>>> p2.nome = "Paulo2"
>>> p.indade = 10
>>> p.mae = "Lais"
>>> p2.nome
'Paulo2'
>>> #Os atributos define o estado do objeto
>>> 
