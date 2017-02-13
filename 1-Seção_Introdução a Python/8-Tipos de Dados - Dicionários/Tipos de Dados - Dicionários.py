Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Diferente da lista e da tupla o dicionario nao recebe indexação por inteiro e o desenvolvedor que e resposavel por criar essa chave valor. Você pode ter qualquer tipo de dado. Com exceção da lista, porque a lista e um tipo mutavel nao pode ter ela como uma chave.
>>> dic = ["chave1": "valor1", 2: "valor2", (1,2): "valor3"]
SyntaxError: invalid syntax
>>> dic = {"chave1": "valor1", 2: "valor2", (1,2): "valor3"}
>>> dic
{(1, 2): 'valor3', 'chave1': 'valor1', 2: 'valor2'}
>>> type(dic)
<class 'dict'>
>>> #Metodos que podem ser trabalhados com dicionarios
>>> dir(dic)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> dic.items()
dict_items([((1, 2), 'valor3'), ('chave1', 'valor1'), (2, 'valor2')])
>>> #items() e usado para lista todos os itens com chave de valor contidos no dicionario, OBS: o dicionario nao garante a ordem.
>>> #Outro metodo e o keys
>>> dic.keys
<built-in method keys of dict object at 0x03F48C88>
>>> 
>>> dic.keys()
dict_keys([(1, 2), 'chave1', 2])
>>> #Reotrnar as chaves definidas
>>> #Metodos pop
>>> dic.pop("chave1")
'valor1'
>>> #O pop e necessario passar o argumento, o item qual deseja remover.
>>> dic
{(1, 2): 'valor3', 2: 'valor2'}
>>> #POP item funciona igual na lsita basta que vc chame ele que fara a remoção do elemento
>>> dic.popitem()
((1, 2), 'valor3')
>>> #O metodo clear()
>>> dic.clear()
>>> dic
{}
>>> 
