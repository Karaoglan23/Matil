#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import sys
import re
from matematik import *
from kesir import Kesir
from kumeler import Kume
from permutasyon import Permutasyon
from kombinasyon import Kombinasyon
from denklem import Degisken, Denklem

A = Kume(lambda kume : kume.eleman[0] == "A")
N = Kume(lambda kume : kume.eleman[-1] == "N")
B = Kume(lambda kume : uzunluk(kume.eleman) == 5)
K = Kume(["AÇELYA","AHMET","AYSUN","BEREN","KENAN","NERMİN"])
A.ekle(K)
N.ekle(K)
B.ekle(K)
hedefKume = Kume(A.fark(N).bilesim(N.fark(A)).kesisim(B))
sonuc = 0
for eleman in K.elemanlari:
    if(eleman in hedefKume):
        sonuc += 1
yaz(sonuc)