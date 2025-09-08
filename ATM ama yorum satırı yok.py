from datetime import datetime

# Global Değişkenler
bakiye = 1000
kredi_borcu_miktari = 0
gunluk_para_cekme_limiti = 100000
gunluk_para_yatirma_limiti = 100000
havale_limiti = 150000
kredi_cekme_limiti = 300000
fatura = 1500

def zaman():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def sifre_giris():
    hak = 4
    while hak > 0:
        try:
            sifre = int(input("\n4 haneli şifrenizi giriniz: "))
            if 1000 <= sifre <= 9999:
                return sifre
            else:
                hak -= 1
                print(f"Şifre 4 haneli olmalı. Kalan deneme hakkı: {hak}")
        except ValueError:
            hak -= 1
            print(f"Geçersiz giriş. Rakamlarla deneyin. Kalan deneme hakkı: {hak}")
    print("\nGiriş hakkınız doldu. Sistem kapanıyor...")
    exit()

def bakiye_goruntule():
    print(f"\nGüncel bakiyeniz: {bakiye:.2f} TL - {zaman()}")

def para_cekme():
    global bakiye, gunluk_para_cekme_limiti
    try:
        miktar = int(input("\nÇekmek istediğiniz miktar: "))
        if miktar > gunluk_para_cekme_limiti:
            print("Günlük limit aşıldı.")
        elif miktar <= bakiye:
            bakiye -= miktar
            gunluk_para_cekme_limiti -= miktar
            print(f"{miktar:.2f} TL çekildi. Yeni bakiye: {bakiye:.2f} TL")
        else:
            print("Yetersiz bakiye.")
    except ValueError:
        print("Geçersiz miktar girişi.")

def para_yatirma():
    global bakiye, gunluk_para_yatirma_limiti
    try:
        miktar = int(input("\nYatırmak istediğiniz miktar: "))
        if miktar > gunluk_para_yatirma_limiti:
            print("Günlük limit aşıldı.")
        else:
            bakiye += miktar
            gunluk_para_yatirma_limiti -= miktar
            print(f"{miktar:.2f} TL yatırıldı. Yeni bakiye: {bakiye:.2f} TL")
    except ValueError:
        print("Geçersiz miktar girişi.")

def havale():
    global bakiye, havale_limiti
    try:
        iban = input("\nIBAN giriniz (TR ile başlayıp 26 hane): ").strip().upper()
        if not (iban.startswith("TR") and len(iban) == 26):
            print("Geçersiz IBAN formatı.")
            return
        miktar = int(input("Göndermek istediğiniz miktar: "))
        if miktar > havale_limiti:
            print("Günlük havale limiti aşıldı.")
        elif miktar <= bakiye:
            bakiye -= miktar
            havale_limiti -= miktar
            print(f"{iban} hesabına {miktar:.2f} TL gönderildi.")
        else:
            print("Yetersiz bakiye.")
    except ValueError:
        print("Geçersiz miktar girişi.")

def kredi_cekme():
    global bakiye, kredi_borcu_miktari, kredi_cekme_limiti
    try:
        miktar = int(input("\nÇekmek istediğiniz kredi miktarı: "))
        if miktar > kredi_cekme_limiti:
            print("Kredi limiti yetersiz.")
        else:
            bakiye += miktar
            kredi_borcu_miktari += miktar * 1.1  # %10 faiz
            kredi_cekme_limiti -= miktar
            print(f"{miktar:.2f} TL kredi çekildi. Yeni bakiye: {bakiye:.2f} TL")
    except ValueError:
        print("Geçersiz miktar girişi.")

def kredi_borc_sorgula():
    print(f"\nKredi borcunuz: {kredi_borcu_miktari:.2f} TL")

def kredi_karti_borcu_odeme():
    global kredi_borcu_miktari,bakiye
    print(f"\nKredi kartı borcunuz: {kredi_borcu_miktari:.2f} TL")
    try:
        odeme = int(input("Ödeme miktarı: "))
        if odeme > kredi_borcu_miktari:
            print("Borçtan fazla ödeme yapılamaz.")
        else:
            kredi_borcu_miktari -= odeme
            bakiye -= odeme
            print(f"{odeme:.2f} TL ödendi. Kalan borç: {kredi_borcu_miktari:.2f} TL")
    except ValueError:
        print("Geçersiz giriş.")

def faturalar():
    global fatura, bakiye
    print(f"\nFatura tutarınız: {fatura:.2f} TL")
    try:
        odeme = float(input("Ödeme tutarı: "))
        if odeme > fatura or odeme > bakiye:
            print("Fatura veya bakiyeyi aşan tutar girdiniz.")
        else:
            fatura -= odeme
            bakiye -= odeme
            print(f"{odeme:.2f} TL ödendi. Kalan fatura: {fatura:.2f} TL")
    except ValueError:
        print("Geçersiz giriş.")

def doviz_piyasasi():
    print(f"\nDolar: {bakiye / 38:.2f} USD | Euro: {bakiye / 45:.2f} EUR | Altın: {bakiye / 3850:.2f} gr")

def sifre_degistir(sifre):
    hak = 4
    while hak > 0:
        try:
            eski = int(input("\nEski şifrenizi giriniz: "))
            if eski == sifre:
                yeni = int(input("Yeni 4 haneli şifre: "))
                if 1000 <= yeni <= 9999:
                    print("Şifre değiştirildi.")
                    return yeni
                else:
                    print("Şifre 4 haneli olmalıdır.")
            else:
                hak -= 1
                print(f"Yanlış şifre. Kalan hak: {hak}")
        except ValueError:
            print("Geçersiz giriş.")
    print("Şifre değiştirme başarısız.")
    return sifre

def ana_menu(sifre):
    print(f"""
    -- ATM'ye Hoşgeldiniz --
       {zaman()}
          
    1 - Bakiye Görüntüle
    2 - Para Çekme
    3 - Para Yatırma
    4 - Havale
    5 - Kredi Çekme
    6 - Kredi Borcu Sorgulama
    7 - Kredi Kartı Borcu Ödeme
    8 - Faturalar
    9 - Döviz Piyasası
   10 - Şifre Değiştir
    Q - Kart İade / Çıkış
    """)
    while True:
        secim = input("\nİşlem seçiniz: ").strip()
        if secim == "1": bakiye_goruntule()
        elif secim == "2": para_cekme()
        elif secim == "3": para_yatirma()
        elif secim == "4": havale()
        elif secim == "5": kredi_cekme()
        elif secim == "6": kredi_borc_sorgula()
        elif secim == "7": kredi_karti_borcu_odeme()
        elif secim == "8": faturalar()
        elif secim == "9": doviz_piyasasi()
        elif secim == "10": sifre = sifre_degistir(sifre)
        elif secim.upper() == "Q":
            print("\nKart iade ediliyor. Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim.")

# Program Başlat
sifre = sifre_giris()
ana_menu(sifre)
