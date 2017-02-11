Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var = 1
>>> # Não e ncessário ponto e virgula no final dos comandos
>>> var = 1, varr = 2
SyntaxError: can't assign to literal
>>> var1 = 1 ; var2 = 2
>>> #Mas para separar dus váriaveis diferentes e necessário ;
>>> #Outra coisa muito importante e ausência de chaves, não e preciso colcoar para indicar um bloco de comandos igual ao C/C++
>>> def funcao()
SyntaxError: invalid syntax
>>> def funcao():
KeyboardInterrupt
>>> def funcao():
	pass

>>> #Os dois pontos mostrar que apartir dele será inciado um bloco de códigos
>>> #Como mostrado na função def funcao():
>>> #O python usa a indentação para determinar os blocos de códigos, esse e o motivo da ausência de chaves.
>>> #No uso de condições if e elif e opcional o uso de parentes
>>> idade = 16
>>> if idade == 16:
	print("pode votar")

	
pode votar
>>> if (idade == 16):
	print("pode votar")

	
pode votar
>>> #No caso do print e necessário ter partens pois se trata de uma função.
>>> #No teste da condicional que o if está fazendo no exemplo anterior.
>>> 
