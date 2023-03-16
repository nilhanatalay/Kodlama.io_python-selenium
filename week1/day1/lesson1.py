print("Kodlamaio")

baslik = "Taşıt Kredisi"    #Değişkene atamak istediğimiz değeri atadık. Metinsel bir ifade olduğu için " " içine yazıyoruz.
print(baslik)

#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

#int, integer => tam sayı
vade = 36    #numeric ifade
vade2 = "36" #metinsel ifade
ekVade = 6

#float , decimal , double
aylikOdeme = 200.50

#bool , boolean => True veya False
yuselisteMi = False

# matematiksel operatörler

#Toplama +
print(5 + 5)
print(vade + 12)  #Değişken tutup toplama yapabiliriz.
print (vade + ekVade)

#Çıkarma -
print(5 - 5)
print(vade - 12)
print (vade - ekVade)

#Çarpma *
print(5 * 5)
print(vade * 12)
print (vade * ekVade)

#Bölme /
print(5 / 5)
print(vade / 12)
print (vade / ekVade)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# mod operator %
print(10%2)
print (vade % 5)
print (vade % ekVade)
print (30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

#Birden fazla satırı yorum satırı haline getirmek için: CTRL K + CTRL C

print (1 != 1) #eşit değildir.
print(1 !=2)

# or and

# or => veya
print( 1 > 2 or 5 > 2)

# and => ve
print( 1 > 2 and 5 > 2)

print( 1 > 2 or 5 > 2 and 3 >2 )
print( 1 > 2 and 5 > 2 and 3 >2 )
print ( 2 > 1 or 1 > 2 and 3 >2)


# karar yapıları
# if else

sayi1 = 10
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır.
#condition

#indent
if sayi1 > sayi2:
    print("Sayı 1,Sayı 2'den büyüktür.")
    print("Hala if bloğunun içerisindeyim.")
print("Burası if bloğunun dışıdır.")

sayi1 = 20
sayi2 = 15

if sayi1 > sayi2:
    print("Sayı 1,Sayı 2'den büyüktür.")
    print("Hala if bloğunun içerisindeyim.")
print("Burası if bloğunun dışıdır.")

sayi1 = 15
sayi2 = 15

if sayi1 < sayi2:
    print("Sayi 1,Sayi 2'den küçüktür.")
#eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("İki sayı eşittir.")
#eğer if ve else if bloklarında hiçbirine girmez ise
else:
    print(Sayi 1, Sayi 2'den büyüktür.')

print("Burası if bloğunun dışıdır.")



if sayi1 == sayi2:
    print("İki sayı eşittir.")
else:
     print("Sayi1  Sayi2'den büyüktür.")

print("Burası if bloğunun dışıdır.")



















