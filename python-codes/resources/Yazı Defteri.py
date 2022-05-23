baslik_1, baslik_2, baslik_3, baslik_4, baslik_5 = "-", "-", "-", "-", "-"
baslik_6, baslik_7, baslik_8, baslik_9, baslik_10 = "-", "-", "-", "-", "-"
yazi_1, yazi_2, yazi_3, yazi_4, yazi_5 = "", "", "", "", ""
yazi_6, yazi_7, yazi_8, yazi_9, yazi_10 = "", "", "", "", ""
komutlar = "Tüm komutlar: Yardım, Yaz, Çıkış, Göster, (Düzenle), (Geri)."
print ("============================================================")
print (" ")
print ("                        Yazı Defteri                        ")
print (" ")
print (komutlar)
anahtar = "Açık"
while anahtar == "Açık":
    print (" ")
    print ("------------------------------------------------------------")
    print (" ")
    print ("=== Anasayfa ===")
    print (" ")
    durum = input ("")
    while durum == "Yardım":
        print (" ")
        print ("=== Yardım ===")
        print (" ")
        print (komutlar)
        print (" ")
        print ("Programın açıkları olabilir, bildirmek isterseniz;")
        print ("Ekin Aslan - 05537316580 - vnymea@gmail.com")
        durum = 0
    while durum == "Yaz":
        print (" ")
        print ("------------------------------------------------------------")
        print (" ")
        print ("=== Yaz ===")
        print (" ")
        numara = int (input ("Yazı numarası (1-10): "))
        print (" ")
        baslik = input ("Yazı başlığı: ")
        print (" ")
        print (">>>>-", baslik, "-<<<<")
        print (" ")
        yazi = input ("")
        if numara == 1:
            baslik_1 = baslik
            yazi_1 = yazi
        elif numara == 2:
            baslik_2 = baslik
            yazi_2 = yazi
        elif numara == 3:
            baslik_3 = baslik
            yazi_3 = yazi
        elif numara == 4:
            baslik_4 = baslik
            yazi_4 = yazi
        elif numara == 5:
            baslik_5 = baslik
            yazi_5 = yazi
        elif numara == 6:
            baslik_6 = baslik
            yazi_6 = yazi
        elif numara == 7:
            baslik_7 = baslik
            yazi_7 = yazi
        elif numara == 8:
            baslik_8 = baslik
            yazi_8 = yazi
        elif numara == 9:
            baslik_9 = baslik
            yazi_9 = yazi
        elif numara == 10:
            baslik_10 = baslik
            yazi_10 = yazi
        print (" ")
        print ("--- Kaydedildi ---")
        durum = 0
    while durum == "Göster":
        print (" ")
        print ("------------------------------------------------------------")
        print (" ")
        print ("=== Göster ===")
        print (" ")
        print ("1)", baslik_1)
        print ("2)", baslik_2)
        print ("3)", baslik_3)
        print ("4)", baslik_4)
        print ("5)", baslik_5)
        print ("6)", baslik_6)
        print ("7)", baslik_7)
        print ("8)", baslik_8)
        print ("9)", baslik_9)
        print ("10)", baslik_10)
        print (" ")
        print ("Gösterilecek başlığın numarasını yazınız, çıkmak için 'Geri'.")
        print (" ")
        goster = input ("")
        if goster == "Geri":
            durum = 0
        else:
            if goster == "1":
                yazi = yazi_1
                baslik = baslik_1
            elif goster == "2":
                yazi = yazi_2
                baslik = baslik_2
            elif goster == "3":
                yazi = yazi_3
                baslik = baslik_3
            elif goster == "4":
                yazi = yazi_4
                baslik = baslik_4
            elif goster == "5":
                yazi = yazi_5
                baslik = baslik_5
            elif goster == "6":
                yazi = yazi_6
                baslik = baslik_6
            elif goster == "7":
                yazi = yazi_7
                baslik = baslik_7
            elif goster == "8":
                yazi = yazi_8
                baslik = baslik_8
            elif goster == "9":
                yazi = yazi_9
                baslik = baslik_9
            elif goster == "10":
                yazi = yazi_10
                baslik = baslik_10
            print(" ")
            print(">>>>-", baslik, "-<<<<")
            print(" ")
            print(yazi)
            print(" ")
            print("------------------------------------------------------------")
            print(" ")
            print("Düzenlemek için 'Düzenle', çıkmak için 'Geri'.")
            print(" ")
            karar = input("")
            if karar == "Düzenle":
                print(" ")
                yeni_baslik = input("Yeni başlık: ")
                print(" ")
                print(">>>>-", yeni_baslik, "-<<<<")
                print(" ")
                yeni_yazi = input("")
                if goster == "1":
                    baslik_1 = yeni_baslik
                    yazi_1 = yeni_yazi
                elif goster == "2":
                    baslik_2 = yeni_baslik
                    yazi_2 = yeni_yazi
                elif goster == "3":
                    baslik_3 = yeni_baslik
                    yazi_3 = yeni_yazi
                elif goster == "4":
                    baslik_4 = yeni_baslik
                    yazi_4 = yeni_yazi
                elif goster == "5":
                    baslik_5 = yeni_baslik
                    yazi_5 = yeni_yazi
                elif goster == "6":
                    baslik_6 = yeni_baslik
                    yazi_6 = yeni_yazi
                elif goster == "7":
                    baslik_7 = yeni_baslik
                    yazi_7 = yeni_yazi
                elif goster == "8":
                    baslik_8 = yeni_baslik
                    yazi_8 = yeni_yazi
                elif goster == "9":
                    baslik_9 = yeni_baslik
                    yazi_9 = yeni_yazi
                elif goster == "10":
                    baslik_10 = yeni_baslik
                    yazi_10 = yeni_yazi
    if durum == "Çıkış":
        anahtar = "Kapalı"
print (" ")
print ("============================================================")
print (" ")
print (">>>>>>>>-- Ekin --<<<<<<<<                                  ")
print (" ")
print ("Ekin Aslan - 05537316580 - vnymea@gmail.com")
print (" ")
print ("Hakları bana ait değildir çalabilirsiniz.")
print (" ")
print ("============================================================")
