from itertools import combinations

class Kombinasyon():
    def __init__(self, secenek, secilecek):
        if type(secenek) == type(list()):
            self._kombinasyonlar = list(combinations(secenek, secilecek))
            self._kombinasyon_sayisi = len(list(self.kombinasyonlar))
        elif type(secenek) == type(3):
            self._kombinasyon_sayisi = len(list(combinations(range(secenek), secilecek)))
            self._kombinasyonlar = list(combinations(range(secenek), secilecek))
        else:
            print("Kombinasyon hesabı yapabilmeniz için secenek olarak bir dizi yada sayi girmelisiniz!")

    @property
    def kombinasyon_sayisi(self):
        return self._kombinasyon_sayisi

    @kombinasyon_sayisi.setter
    def kombinasyon_sayisi(self, sayi):
        self._kombinasyon_sayisi = sayi

    @property
    def kombinasyonlar(self):
        return self._kombinasyonlar

    @kombinasyonlar.setter
    def kombinasyonlar(self, dizi):
        self._kombinasyonlar = dizi

    def __mul__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi * other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi * other

    def __rmul__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi * other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi * other

    def __add__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi + other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi + other

    def __radd__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi + other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi + other

    def __sub__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi - other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi - other

    def __rsub__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi - other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi - other

    def __truediv__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi / other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi / other

    def __rtruediv__(self, other):
        if type(other) == type(self):
            return self._kombinasyon_sayisi / other._kombinasyon_sayisi
        elif '__mul__' in dir(other):
            return self._kombinasyon_sayisi / other

    def __str__(self):
        return str(self._kombinasyon_sayisi)

    def __iter__(self):
        return KombinasyonIterator(self)

class KombinasyonIterator:
    def __init__(self, obj):
        self._obj = obj
        self._konum = 0
        
    def __next__(self):
        if self._konum < (self._obj.kombinasyon_sayisi or self._konum > 0) :
            self._konum += 1
            return self._obj.kombinasyonlar[self._konum - 1]
        raise StopIteration

if __name__ == "__main__":
    print(Kombinasyon(4, 1) * Kombinasyon(4, 3) * Kombinasyon(2, 1) * Kombinasyon(4, 2))