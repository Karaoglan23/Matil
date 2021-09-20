from sympy.solvers import solve
from sympy import Symbol
import re

class Degisken():
	def __init__(self, degisken):
		self.degisken = degisken
		self.sembol = Symbol(degisken)

	def __repr__(self):
		return self.degisken

def hepsini_bul(kelime, aranan):
	konumlar = []
	basla = 0
	while(-1 != kelime.find(aranan, basla)):
		konumlar.append(kelime.find(aranan, basla))
		basla = kelime.find(aranan, basla) + 1
		print(basla)
	return konumlar

def str_degis(kelime, konum, degistirilecek):
	return kelime[:konum] + degistirilecek + kelime[konum+1:]

def konumlari_degistir(kelime, konum_listesi, degistirilecek):
	for konum in konum_listesi:
		kelime = str_degis(kelime, konum, degistirilecek)
	return kelime

class Denklem():
	def __init__(self, denklem, tum_degiskenler, denklik = 0):
		self.denklem = denklem
		self.denklik = denklik
		self.tum_degiskenler = tum_degiskenler

	def yaz(self):
		print(self.denklem)

	def sonuc_yaz(self):
		print(self.sonuc)

	def tek_tarafa_topla(self):
		self.esitlik = self.denklem[self.denklem.find('=') + 1:]
		self.denklem = self.denklem.replace(self.esitlik, "")
		self.denklem = self.denklem[:-1]
		artilar = hepsini_bul(self.esitlik, '+')
		eksiler = hepsini_bul(self.esitlik, '-')
		no_double_yildiz = re.sub(r"\*\*", "__1337__", self.esitlik)
		yildizlar = hepsini_bul(no_double_yildiz, '*')
		bolumler = hepsini_bul(self.esitlik, '/')
		self.esitlik = "-1*(" + self.esitlik.strip() + ")"
		# self.esitlik = konumlari_degistir(self.esitlik, artilar, '-')
		# self.esitlik = konumlari_degistir(self.esitlik, eksiler, '+')
		self.esitlik = konumlari_degistir(self.esitlik, yildizlar, '/')
		self.esitlik = konumlari_degistir(self.esitlik, bolumler, '*')

		self.denklem += self.esitlik
		return self.denklem

	def coz(self):
		for degisken in self.tum_degiskenler:
			self.denklem = self.denklem.replace(degisken.degisken, degisken.degisken + ".sembol")
			exec(degisken.degisken + " = Degisken('" + degisken.degisken + "')")
		if(self.denklem.find('=') != -1):
			self.denklem = self.tek_tarafa_topla()
		# print("solve("+self.denklem+")")
		self.sonuc = eval("solve("+self.denklem+")")
		return self.sonuc

if __name__ == "__main__":
	x = Degisken('x')
	y = Degisken('y')
	z = Degisken('z')
	denklem = Denklem("z**2*x**2 - z**2*y**2",[x,y,z])
	denklem.yaz()
	denklem.coz()
	denklem.sonuc_yaz()
