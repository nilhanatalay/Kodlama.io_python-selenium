faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(vade + 12)
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
# print(int(krediAdi)) hata verir.
faiz=str(faiz)
print(str(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz:"))
print(type(vade))
print(vade + 12)

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade:" + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade:{vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = input("İsminizi giriniz:")
metin = "Merhaba {name}".format(name=isim)
print(metin)

# f-string
metin = f"Hoşgeldiniz{1+1}"
print(metin)

# listeler
# döngüler
# fonksiyonlar

dizi = ["İhtiyaç Kredisi",10,5.2,True]
print(dizi)


krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #lenght
#print(krediler[3]) hata verir.

krediler.append("Özel Kredi") #listenin son elemanına ekler.
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop() #listedeki son elemanı siler
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi") #index sırasına göre bu isimde bulduğu ilk elemanı siler.
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

# for
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)

print("*******************")

for i in range(5,10):
    print(i)

print("*******************")

for i in range(0,51,10): #1.eleman başlangıç elemanı , 2.eleman varış elemanı , 3.eleman ilgili i değişkeninin kaçar kaçar artacağını belirleyen kısım.
    print(i)

#print("*******************")
#for i in range(0.1,0.5):
 #   print(i)


krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("************************")
for i in range(len(krediler)):
    print(krediler[i])
print("************************")

# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("***********************")

while True:
    print("X")
    break

print("**************")
krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]
i = 0
while i < len(krediler):
    print(i)
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break

print("**************************")

i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break


# fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat , indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Nilhan")
sayHello("Burak")


def calculateAndReturn(price,discount):
    return price - discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

print("*************")

def calculateAndReturn(price,discount):
    return ["1","2"]

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)


def calculatePrice(price , discount):
    print(price - discount)


def calculateAndReturn(price, discount):
    return price - discount









