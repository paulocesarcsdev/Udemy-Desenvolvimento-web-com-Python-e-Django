Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Assim como nas outras linguagens o python também existe os tipos de dados
>>> #No qual será trabalhado.
>>> #Os mais conhecidos no python são strings, tuplas, listas e dicionários.
>>> #Vamos ver cada um, começando de string
>>> #O que e uma string? Se trata de um texto.
>>> #Um conjuto de caracteres, e toda string deve vir sobre aspas
>>> texto = "Python"
>>> #Para verificar o tipo de dado dessa váriavei pode usar a função type
>>> type(texto)
<class 'str'>
>>> #No python seu tipo e definido dinamicament, o python e uma linguagem dinamicamente tipada.
>>> #Fortimente tipada
>>> #OBS: As string são imutável, não pode ser modificada após sua criação.
>>> texto[0]
'P'
>>> texto[1]
'y'
>>> texto[10]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    texto[10]
IndexError: string index out of range
>>> texto = "sss"
>>> texto = "Python"
>>> texto[0] = "pp"
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    texto[0] = "pp"
TypeError: 'str' object does not support item assignment
>>> texto[0:3]
'Pyt'
>>> 
