Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # if e uma estrutura de controle
>>> # Ele serve para fazer uma verificação para sabe se sera necessario ou nao executar uma parte do programa.
>>> idade = 16
>>> if idade >= 16:
	print("pode votar")

	
pode votar
>>> #No caso acima e feito uma verificação se idade e maior ou igual 16 anos como deu valor verdadeiro pode votar.
>>> v = True
>>> if v:
	print("verdadeiro")

	
verdadeiro
>>> #Outra estrutura interessante que existe nas linguagens e o swith
>>> #No python não tem o swith
>>> #No python existe o elif nas outra linguagens e conhecida como if e else
>>> idade = 15
>>> if idade >= 16:
	print("Pode votar")

	
>>> if idade >= 16:
	print("Pode votar")
elif idade < 16:
	print("Ainda não pode votar")

	
Ainda não pode votar
>>> 
