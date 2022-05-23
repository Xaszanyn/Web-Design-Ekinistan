print ("====================================================================================================")
print (" ")
print ("                                         Depresiflik Testi                                          ")
print (" ")
print ("= Aşağıdaki soruları cevaplayınız. (Evet/Hayır veya E/H veya e/h) =")
print (" ")
soru_1 = input ("Bazen hayatımda ufak tefek şeylere acayip gülerim. (Evet/Hayır): ")
print (" ")
soru_2 = input ("Geceleri canım tatlı istiyor. (Evet/Hayır): ")
print (" ")
soru_3 = input ("Kendi kendime çok konuşuyorum. (Evet/Hayır): ")
print (" ")
soru_4 = input ("Kendimi ifade etmek istememe rağmen ifade edemiyorum. (Evet/Hayır): ")
print (" ")
print ("= Size en yakın olan şıkkı yazınız. (Özel Türkçe harf önemli değildir.) =")
print (" ")
soru_5 = input ("En sevdiğim hava durumu (Yağmurlu/Güneşli/Sağanak Yağmurlu/Kapalı): ")
print (" ")
soru_6 = input ("En sevdiğim renk (Kırmızı/Mavi/Yeşil/Sarı/Mor/Turkuaz/Beyaz/Siyah/Hepsi): ")
print (" ")
print ("(Takım elbiseli adam/Sarışın bir kız/Küçük bir kız çocuğu/Siyah bir kedi)")
soru_7 = input ("Hayalinizde sokakta yürürken aniden karşınıza biri çıktı. Kim? (1/2/3/4): ")
print (" ")
print ("(Rusya/ABD/İsveç/İspanya/Küba)")
soru_8 = input ("En çok hoşlandığınız ülkeyi seçiniz: ")
print (" ")

sonuc = 100

if soru_1 == "Evet" or soru_1 == "E" or soru_1 == "e":
    sonuc = sonuc - 10
elif soru_1 == "Hayır" or soru_1 == "H" or soru_1 == "h":
    sonuc = sonuc - 0

if soru_2 == "Evet" or soru_2 == "E" or soru_2 == "e":
    sonuc = sonuc - 5
elif soru_2 == "Hayır" or soru_2 == "H" or soru_2 == "h":
    sonuc = sonuc - 0

if soru_3 == "Evet" or soru_3 == "E" or soru_3 == "e":
    sonuc = sonuc - 15
elif soru_3 == "Hayır" or soru_3 == "H" or soru_3 == "h":
    sonuc = sonuc -0

if soru_4 == "Evet" or soru_4 == "E" or soru_4 == "e":
    sonuc = sonuc - 20
elif soru_4 == "Hayır" or soru_4 == "H" or soru_4 == "h":
    sonuc = sonuc - 0

if soru_5 == "Yağmurlu" or soru_5 == "Yagmurlu":
    sonuc = sonuc - 6.6
elif soru_5 == "Güneşli" or soru_5 == "Gunesli":
    sonuc = sonuc - 0
elif soru_5 == "Sağanak Yağmurlu" or soru_5 == "Sağanak" or soru_5 == "Saganak Yagmurlu" or soru_5 == "Saganak":
    sonuc = sonuc - 10
elif soru_5 == "Kapalı" or soru_5 == "Kapali":
    sonuc = sonuc - 3.3

if soru_6 == "Siyah":
    sonuc = sonuc - 15
elif soru_6 == "Mavi":
    sonuc = sonuc - 13
elif soru_6 == "Kırmızı" or soru_6 == "Kirmizi":
    sonuc = sonuc - 11
elif soru_6 == "Mor":
    sonuc = sonuc - 9
elif soru_6 == "Turkuaz":
    sonuc = sonuc - 7
elif soru_6 == "Yeşil" or soru_6 == "Yesil":
    sonuc = sonuc - 5
elif soru_6 == "Sarı" or soru_6 == "Sari":
    sonuc = sonuc - 3
elif soru_6 == "Beyaz":
    sonuc = sonuc - 1
elif soru_6 == "Hepsi":
    sonuc = sonuc - 0

if soru_7 == "1":
    sonuc = sonuc - 15
elif soru_7 == "2":
    sonuc = sonuc - 0
elif soru_7 == "3":
    sonuc = sonuc - 10
elif soru_7 == "4":
    sonuc = sonuc - 5

if soru_8 == "Rusya":
    sonuc = sonuc - 10
elif soru_8 == "ABD":
    sonuc = sonuc - 0
elif soru_8 == "İsveç":
    sonuc = sonuc - 7.5
elif soru_8 == "İspanya":
    sonuc = sonuc - 2.5
elif soru_8 == "Küba":
    sonuc = sonuc - 5

print ("----------------------------------------------------------------------------------------------------")
print (" ")

if sonuc >= 91:
    print ("Neden bu testi çözdün ki? Senin hayatında depresyona yer yok. Hayal dışı!")
elif sonuc >= 81:
    print ("Ufak sorunlar çıksa da siz mutlusunuz ve hayata dair olumlu bakıyorsunuz.")
    print ("Sonuç = Olağanüstü!")
elif sonuc >= 71:
    print ("Sorunlar hayatımızda hep var ve siz bunları görmezden gelebiliyorsunuz.")
    print ("Sonuç = Tebrikler!")
elif sonuc >= 61:
    print ("Depresyonda olduğunuzu hissediyorsanız iyi dinleyin. Kurtulmanız an meselesi.")
    print ("Sonuç = Güzel!")
elif sonuc >= 51:
    print ("Sonuç çok kötü değil. İyi şeylere odaklanın, mutsuzsanız neden mutsuz olduğunuzu")
    print ("sorgulayın. Yalnız değilsiniz.")
    print ("Sonuç = Fena Değil.")
elif sonuc >= 41:
    print ("Hayatınızda bazı şeyler kötü gidiyor olabilir. Onları değiştirmenin sizin elinizde")
    print ("olduğunu unutmayın. Yarın filan değil, bugünden mutlu olmaya başlayın.")
    print ("Sonuç = Azcık Bişey Depresif.")
elif sonuc >= 31:
    print ("Dostum keyifsiz misin yoksa? Olaylara gereğinden fazla önem verme. Her şey olacağına")
    print ("varır.")
    print ("Sonuç = Depresif.")
elif sonuc >= 21:
    print ("Depresyon seziyorum. Bana kalırsa seni yargılamayacak birine tüm dertlerini anlat.")
    print ("İçini dök iyi gelir. Fazla kendini de yorma. Sen değerlisin.")
    print ("Sonuç = Azcık fazla depresif.")
elif sonuc >= 11:
    print ("Hmm Depresyon. Kendini üzecek her şeyden kurtul. Biliyorum söylemesi kolay ve kendini")
    print ("kendini yorgun hissediyorsun. Ancak hissettiğin şeyleri inancınla değiştirebilirsin.")
    print ("Sen değerlisin. Kirlenen yakutun değeri değişmez.")
    print ("Sonuç = Fazla depresif.")
elif sonuc >= 1:
    print ("Benimle aynı çıktın! :) Konuşmak istersen numaram: 5537316580. Hayat ne kadar olabilir ki")
    print ("Dertlerin var biliyorum ancak dertler çözülmek içindir unutma. Canını sıkma, rahat ol.")
    print ("Kendine bir dinleyici bul. Elbet düzelir her şey!")
    print ("Sonuç = Aşırı depresif.")

print (" ")
print ("100 üzerinden çıkan sonucun" , sonuc)
print (" ")
print ("----------------------------------------------------------------------------------------------------")
print (" ")
print ("Ekin Aslan                 5537316580                 vnymea@gmail.com                 05180000097  ")
print (" ")
print ("Hakları bana ait falan değil çalabilirsiniz.")
print (" ")
print ("====================================================================================================")