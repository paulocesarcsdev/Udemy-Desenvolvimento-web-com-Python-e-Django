Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #No python existe algumas categorias de números, inteiro, flutuante, complexos, e mais comum lidar com inteiro e flout.
>>> num = 1
>>> #Através do comando type e possível verificar o tipo do mesmo.
>>> type(num)
<class 'int'>
>>> #E mostrado o tipo inteiro.
>>> num2 = 1.5
>>> type(num2)
<class 'float'>
>>> #Também e possível fazer operação de categorias diferentes o python resolve isso automaticamente.
>>> 1 + 1.5
2.5
>>> num + num2
2.5
>>> #No python tudo e um objeto
>>> dir(num)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> #dir mostra os metodos que podem ser usado na váriavel num
>>> 
