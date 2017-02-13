Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #As tuplas no python e uma estrutura de dado imutavel
>>> #Ela recebe indexaçao por inteiro, mas não e possível mudar as posições dela
>>> #Ela suporta qualquer tipo de objeto, os objetos inseridos na tupla permanece com suas caracteristicas
>>> tupla = ("Python", "Java", "Android" 12, [1,2,3],(1,2) )
SyntaxError: invalid syntax
>>> tupla = ("Python", "Java", "Android", 12, [1,2,3],(1,2) )
>>> type(tupla)
<class 'tuple'>
>>> #fazendo indexação, vamos ver que quem está na primeira posição
>>> tupla[1]
'Java'
>>> # Correção: #fazendo indexação, vamos ver que quem está na pisição um
>>> tupla[0]
'Python'
>>> tupla[5]
(1, 2)
>>> tupla.apped(15)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tupla.apped(15)
AttributeError: 'tuple' object has no attribute 'apped'
>>> #Tupla não tem o metodo apped
>>> tupla.count("Python")
1
>>> #O metodo count serve para contar a quantidade de objetos dentro da tupla
>>> #A lista que está dentro da tupla continua sendo mutavel, vamos testar, ela esta na posição 4
>>> tupla[4].append(4)
>>> tupla
('Python', 'Java', 'Android', 12, [1, 2, 3, 4], (1, 2))
>>> #O quatro foi adicionado a nossa lista.
>>> 
