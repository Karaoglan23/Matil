from matematik import Matematik
import itertools

class Kume(object):
    def __init__(self, parametre=None):
        self.pos = 0
        if parametre == None:
            self.elemanSayisi = 0
            self.elemanlari = []
        elif type(parametre) == type(3) or type(parametre) == type("test"):
            self.elemanlari = [parametre]
            self.eleman = parametre
            self.elemanSayisi = 1
        elif type(parametre) == type(lambda : None):
            self.test_func = parametre
            self.elemanlari = []
            self.elemanSayisi = 0
        elif type(parametre) == type(True):
            self.kosul = parametre
            self.elemanlari = []
            self.elemanSayisi = 0
        elif type(parametre) == type([]):
            self.elemanSayisi = len(parametre)
            self.elemanlari = parametre
        elif type(parametre) == type(tuple()):
            self.elemanSayisi = len(list(parametre))
            self.elemanlari = list(parametre)

    def fark(self, diger):
        fark = []
        for eleman in self.elemanlari:
            if not eleman in diger.elemanlari:
                fark.append(eleman)
        return self.__class__(fark)

    def kesisim(self, diger):
        kesisim = []
        for eleman in self.elemanlari:
            if eleman in diger.elemanlari:
                kesisim.append(eleman)
        return self.__class__(kesisim)

    def bilesim(self, diger):
        bilesim = diger.elemanlari
        for eleman in self.elemanlari:
            if not eleman in diger.elemanlari:
                bilesim.append(eleman)
        return self.__class__(bilesim)

    def test(self, kume):
        return self.test_func(kume)

    def ekle(self, eleman):
        if('test_func' in dir(self)):
            if(type(eleman) == type([])):
                for el in eleman:
                    if(self.test_func(el)):
                        self.elemanlari.append(el)
            elif(type(eleman) == type(self.__class__([]))):
                for el in eleman.elemanlari:
                    if(self.test_func(el)):
                        self.elemanlari.append(el)
            else:
                if(self.test_func(eleman)):
                    self.elemanlari.append(eleman)
        else:
            self.elemanlari.append(eleman)
            self.elemanSayisi = len(self.elemanlari)

    def tumAltKumeler(self):
        self.elemanlari
        self.altKumeListesi = []
        for sayi in range(0, len(self.elemanlari)+1):
            for alt_kume in itertools.combinations(self.elemanlari, sayi):
                self.altKumeListesi.append(self.__class__(alt_kume))
        return self.altKumeListesi

    def __iter__(self):
        return KumeIterator(self)

class KumeIterator:
    def __init__(self, kume):
        self._kume = kume
        self._konum = 0
        
    def __next__(self):
        if self._konum < (self._kume.elemanSayisi or self._konum > 0) :
            self._konum += 1
            return self._kume.elemanlari[self._konum - 1]
        raise StopIteration

if __name__ == "__main__":
    gizemli_kume = Kume(lambda kume : kume.elemanSayisi in kume)
    gizemli_alt_kume_listesi = Kume()
    A = Kume([1,2,3,4,5,6])
    for altKume in A.tumAltKumeler():
        if(gizemli_kume.test(altKume)):
            gizemli_alt_kume_listesi.ekle(altKume)
    print(gizemli_alt_kume_listesi.elemanSayisi)
