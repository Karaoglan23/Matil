
from itertools import permutations, combinations
from denklem import Denklem, Degisken

class Matematik():
	@staticmethod
	def OBEB(sayi1, sayi2):
		obeb = 0
		kucuk_olan = 0

		if sayi1 < 0:
			sayi1 = sayi1 * -1
		
		if sayi2 < 0:
			sayi2 = sayi2 * -1

		if sayi1 > sayi2:
			kucuk_olan = sayi2
		else:
			kucuk_olan = sayi1 
		
		obeb = kucuk_olan

		while kucuk_olan > 0:
			if sayi1 % kucuk_olan == 0 and sayi2 % kucuk_olan == 0:
				obeb = kucuk_olan
				break
			kucuk_olan = kucuk_olan - 1
			
		return obeb

def hesapla(ifade):
	return eval(str(ifade))

def uslu_yaz(sayi, kac_ussu):
	x = Degisken('x')
	denklem = Denklem( str(sayi) + " ** (1/x) - " + str(kac_ussu), [x])
	us = int(denklem.coz()[0])
	print(str(kac_ussu) + "**" + str(us))

def uzunluk(x):
	return len(x)

def yaz(x):
	print(x)