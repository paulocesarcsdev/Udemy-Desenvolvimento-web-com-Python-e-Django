Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #While Tem quase a mesma finalidade que o for
>>> controle = 10
>>> while controle >= 0:
	print("Contage regressiva:", controle)
	controle = controle - 1
	if controle < 0:
		print("BOmmmmmmm")

		
Contage regressiva: 10
Contage regressiva: 9
Contage regressiva: 8
Contage regressiva: 7
Contage regressiva: 6
Contage regressiva: 5
Contage regressiva: 4
Contage regressiva: 3
Contage regressiva: 2
Contage regressiva: 1
Contage regressiva: 0
BOmmmmmmm
>>> #Quando usar for e quando usar while? For quando sabemos quantas interações serão feitas nos objtos.
>>> #Quanto usar while? Ele não sabe o momento de parar, e necessario informar qquando ele pare.
>>> 
