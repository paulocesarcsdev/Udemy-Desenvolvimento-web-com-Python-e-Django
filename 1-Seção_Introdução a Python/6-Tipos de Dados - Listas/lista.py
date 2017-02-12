Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Lista são mutáveis e recebem também um índice com indexação inteira para que posse ser manipulada, também e um objeto que possui métodos
>>> #E uma estrutura muito importante muito utilizada no django.
>>> lista = []
>>> type(lista)
<class 'list'>
>>> #O método append pode ser usado para fazer inserção de elementos na lista.
>>> lista.append("Python")
>>> list
<class 'list'>
>>> lista
['Python']
>>> lista.append("Java")
>>> lista
['Python', 'Java']
>>> #A lista garante a ordem de inserção dos objetos.
>>> lista.append("JavaScript")
>>> lista.append("PHP")
>>> lista
['Python', 'Java', 'JavaScript', 'PHP']
>>> #Listar os métodos disponíveis
>>> dir(lista)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> lista.reverse()
>>> lista
['PHP', 'JavaScript', 'Java', 'Python']
>>> lista.reverse()
>>> lista.insert(0,"Android")
>>> #Método reverse() altera a ordem da lista
>>> #Método insert insere um elemento na lista o primeiro parâmetro indica a posição o segundo o elemento que será inserido.
>>> lista.pop()
'PHP'
>>> 
>>> #O método pop remove o ultimo elemento da lista e lista o mesmo.
>>> lista.count("Python")
1
>>> #O método count serve para contar a quantidade de ocorrência na lista.
>>> lista.remove("Java")
>>> #O método remove serve para remover um determinado elemento na lista
>>> lista
['Android', 'Python', 'JavaScript']
>>> #A lista suporta qualquer tipo de objeto
>>> #No exemplo temos uma lista de string, a seguir vou adicionar um número.
>>> lista.append(10)
>>> lista
['Android', 'Python', 'JavaScript', 10]
>>> lista2 = [1,2,3]
>>> lista.append(lista2)
>>> lista
['Android', 'Python', 'JavaScript', 10, [1, 2, 3]]
>>> 
