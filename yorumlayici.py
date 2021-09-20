#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, os, sys, codecs, traceback
from matematik import *
from kesir import Kesir
from kumeler import Kume
from permutasyon import Permutasyon
from kombinasyon import Kombinasyon
from denklem import Degisken, Denklem

def yil_sec():
    ekran_temizle()
    print("Matil Yorumlayıcı version 1.1")
    print("")
    yillar = ["2017", "2018", "2019", "2020", "2021"]
    print("[1] 2017")
    print("[2] 2018")
    print("[3] 2019")
    print("[4] 2020")
    print("[5] 2021")
    print("[0] Çıkış")
    print("")
    yil = int(input("Yıl Seçiniz: "))
    if yil == 0:
        ekran_temizle()
        exit()
    elif(yil < 0 or yil > 5):
        input("Lütfen geçerli seçeneklerden birini seçin! (Devam etmek için bir tuşa basın)")
        return yil_sec()
    else:
        return yillar[yil-1]

def ekran_temizle():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def konu_sor(liste, yil):
    ekran_temizle()
    print("Matil Yorumlayıcı version 1.1")
    print("")
    print(yil + " TYT Konuları")
    print("")
    for i, konu in enumerate(liste):
        print("["+str(i+1)+"] " + konu)
    print("[0] Geri Dön")
    print("")
    konu = int(input("Konu Seçiniz: "))
    if(konu == 0):
        yil_menu()
    elif(konu < 0 or konu > len(liste) + 1):
        input("Lütfen geçerli seçeneklerden birini seçin! (Devam etmek için bir tuşa basın)")
        return konu_sor(liste, yil)
    return liste[konu-1]

def soru_sec(liste, yil, konu):
    ekran_temizle()
    print("Matil Yorumlayıcı version 1.1")
    print("")
    print(yil + " > " + konu + " Soruları")
    print("")
    for i, soru in enumerate(liste):
        print("["+str(i+1)+"] " + soru)
    print("[0] Geri Dön")
    print("")
    soru = int(input("Soru Seçiniz: "))
    print(soru)
    if(soru == 0):
        konu_menu()
    elif(soru < 0 or soru > len(liste) + 1):
        input("Lütfen geçerli seçeneklerden birini seçin! (Devam etmek için bir tuşa basın)")
        return soru_sec(liste, yil, konu)
    else:
        return liste[soru-1]

def duzenle_calistir_sor(kod, dosya_konumu):
    print("")
    print("[1] Kodu Düzenle")
    print("[2] Soruyu Görüntüle")
    print("[3] Çalıştır")
    print("[0] Geri Dön")
    print("")
    islem = int(input("İşlem Seç: "))
    if islem == 0:
        soru_menu()
    elif islem == 1:
        os.system("start notepad '" + dosya_konumu + "'")
    elif islem == 2:
        os.system(dosya_konumu.replace("ornekler", "resimler").replace(".matil", ".PNG"))
    elif islem == 3:
        ekran_temizle()
        try:
            exec(kod)
        except Exception as e:
            e = sys.exc_info()
            print('Hata Mesajı: ', e[1])
        input("Geri dönmek için bir tuşa basın")
    else:
        input("Lütfen geçerli seçeneklerden birini seçin! (Devam etmek için bir tuşa basın)")
        duzenle_calistir_sor(kod, dosya_konumu)
    print("")
    kod_menu(dosya_konumu)

def Kodu_goster(kod, dosya_konumu):
    ekran_temizle()
    print("-"*80)
    print(">>> " + dosya_konumu)
    print("-"*80)
    print("")
    print(kod)
    print("")
    print("-"*80)
    duzenle_calistir_sor(kod, dosya_konumu)

def kod_menu(dosya_konumu):
    dosya = codecs.open(dosya_konumu, "r", encoding="utf-8")
    kod = dosya.read()
    kod = re.sub(r"içinde", "in", kod)
    kod = re.sub(r"Her", "for", kod)
    kod = re.sub(r"Eğer", "if", kod)
    kod = re.sub(r".ilkHarf", "[0]", kod)
    kod = re.sub(r".sonHarf", "[-1]", kod)
    kod = re.sub(r"iken", "while", kod)
    Kodu_goster(kod, dosya_konumu)
    #exec(kod)
    dosya.close()

def konu_menu():
    global konu_listesi, sorular, yil, konu
    konu = konu_sor(konu_listesi, yil)
    sorular = os.listdir(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu)
    soru = soru_sec(sorular, yil, konu)
    kod_menu(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu + "\\" + soru)

def soru_menu():
    global sorular, yil, konu
    sorular = os.listdir(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu)
    soru = soru_sec(sorular, yil, konu)
    kod_menu(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu + "\\" + soru)

def yil_menu():
    ekran_temizle()
    yil = yil_sec()
    konu_listesi = os.listdir(os.getcwd() + "\\ornekler\\" +yil)
    konu = konu_sor(konu_listesi, yil)
    sorular = os.listdir(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu)
    soru = soru_sec(sorular, yil, konu)
    kod_menu(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu + "\\" + soru)

if __name__ == "__main__":
    ekran_temizle()
    if len(sys.argv) > 1:
        kod_menu(sys.argv[1])
    else:
        yil = yil_sec()
        konu_listesi = os.listdir(os.getcwd() + "\\ornekler\\" +yil)
        konu = konu_sor(konu_listesi, yil)
        sorular = os.listdir(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu)
        soru = soru_sec(sorular, yil, konu)
        kod_menu(os.getcwd() + "\\ornekler\\" +yil + "\\" + konu + "\\" + soru)
