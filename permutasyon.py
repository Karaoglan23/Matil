from itertools import permutations

class Permutasyon():
    def __init__(self, secenek, secilecek):
        if type(secenek) == type(list()):
            self._permutasyonlar = list(permutations(secenek, secilecek))
            self._permutasyon_sayisi = len(list(self._permutasyonlar))
        elif type(secenek) == type(3):
            self._permutasyon_sayisi = len(list(permutations(range(secenek), secilecek)))
            self._permutasyonlar = list(permutations(range(secenek), secilecek))
        else:
            print("Permutasyon hesabı yapabilmeniz için secenek olarak bir dizi yada sayi girmelisiniz!")

    @property
    def permutasyon_sayisi(self):
        return self._permutasyon_sayisi

    @permutasyon_sayisi.setter
    def permutasyon_sayisi(self, sayi):
        self._permutasyon_sayisi = sayi

    @property
    def permutasyonlar(self):
        return self._permutasyonlar

    @permutasyonlar.setter
    def permutasyonlar(self, permutations):
        self._permutasyonlar = permutations

    def __mul__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi * other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi * other

    def __rmul__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi * other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi * other

    def __add__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi + other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi + other

    def __radd__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi + other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi + other

    def __sub__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi - other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi - other

    def __rsub__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi - other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi - other

    def __truediv__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi / other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi / other

    def __rtruediv__(self, other):
        if type(other) == type(self):
            return self._permutasyon_sayisi / other._permutasyon_sayisi
        elif '__mul__' in dir(other):
            return self._permutasyon_sayisi / other
    
    def __str__(self):
        return str(self._permutasyon_sayisi)

    def __iter__(self):
        return PermutasyonIterator(self)

class PermutasyonIterator:
    def __init__(self, obj):
        self._obj = obj
        self._konum = 0
        
    def __next__(self):
        if self._konum < (self._obj.permutasyon_sayisi or self._konum > 0) :
            self._konum += 1
            return self._obj.permutasyonlar[self._konum - 1]
        raise StopIteration