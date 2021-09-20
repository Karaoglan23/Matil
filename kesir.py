from matematik import Matematik

class Kesir():
	def __init__(self, pay, payda=1):
		self.pay = pay
		self.payda = payda

	def yaz(self):
		print(str(self.pay) + "/" + str(self.payda))

	def carp(self, kesir):
		return self.__class__(self.pay * kesir.pay, self.payda * kesir.payda).sadelestir()

	def bol(self, kesir):
		return self.__class__(self.pay * kesir.payda, self.payda * kesir.pay).sadelestir()

	def topla(self, kesir):
		self.payda_esitle(kesir)
		return self.__class__(self.pay + kesir.pay, self.payda).sadelestir()

	def cikar(self, kesir):
		self.payda_esitle(kesir)
		return self.__class__(self.pay - kesir.pay, self.payda).sadelestir()

	def payda_esitle(self, kesir):
		if(self.payda != kesir.payda):
			payda_temp = kesir.payda
			kesir.pay  = kesir.pay * self.payda 
			kesir.payda  = kesir.payda * self.payda
			self.pay  = self.pay * payda_temp 
			self.payda  = self.payda * payda_temp
		return [self, kesir]

	def sadelestir(self):
		bolen = Matematik.OBEB(self.pay, self.payda)
		if(bolen != 0):
			self.pay = int(self.pay / bolen)
			self.payda = int(self.payda / bolen)
		return self

	def __repr__(self):
		return str(self.pay) + "/" + str(self.payda)

	def __mul__(self, other):
		if type(other) == type(self):
			return self.carp(other)
		elif '__mul__' in dir(other):
			return self.carp(Kesir(other, 1))

	def __rmul__(self, other):
		if type(other) == type(self):
			return self.carp(other)
		elif '__mul__' in dir(other):
			return self.carp(Kesir(other, 1))

	def __add__(self, other):
		if type(other) == type(self):
			return self.topla(other)
		elif '__mul__' in dir(other):
			return self.topla(Kesir(other, 1))

	def __radd__(self, other):
		if type(other) == type(self):
			return self.topla(other)
		elif '__mul__' in dir(other):
			return self.topla(Kesir(other, 1))

	def __sub__(self, other):
		if type(other) == type(self):
			return self.cikar(other)
		elif '__mul__' in dir(other):
			return self.cikar(Kesir(other, 1))

	def __rsub__(self, other):
		if type(other) == type(self):
			return self.cikar(other)
		elif '__mul__' in dir(other):
			return self.cikar(Kesir(other, 1))

	def __truediv__(self, other):
		if type(other) == type(self):
			return self.bol(other)
		elif '__mul__' in dir(other):
			return self.bol(Kesir(other, 1))

	def __rtruediv__(self, other):
		if type(other) == type(self):
			return self.bol(other)
		elif '__mul__' in dir(other):
			return self.bol(Kesir(other, 1))

if __name__ == "__main__":
	kesir = Kesir(5, 8)
	kesir2 = Kesir(10, 3)
	kesir3, kesir4 = kesir.payda_esitle(kesir2)
	kesir3.yaz()
	kesir4.yaz()
	(kesir3 + kesir4).yaz()
	kesir3.topla(kesir4).sadelestir().yaz()