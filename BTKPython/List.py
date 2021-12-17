from datetime import datetime

stdA=["Yiğit","Bilgi",2010,[70,60,70]]
#print(f"{stdA[0]} {stdA[1]}, {datetime.now().year-stdA[2]} yasinda ve not ortalaması {round((stdA[3][0]+stdA[3][1]+stdA[3][2])/3,2)}")

numbers=[1,4,2,9,6,8,5]
numbers.append(8)#Listenin sonuna eleman ekler. 
numbers.insert(3,3)#Listenin 3.indecine 3 sayısını koyar.
numbers.insert(-1,7)#Sondaki sayıyı sola kaydırıp son indexe 7 koyar.
numbers.pop()#Listeden son elemanı çıkarır.
numbers.pop(0)#Listeden 0 indexindeki elemanı çıkarır.
numbers.remove(5)#Listeden 5 sayısını siler.
numbers.sort()#Liste sıralanır.
numbers.reverse()#Listeyi ters çevirir.
numbers.count(1) #Listede 1 elemanından kaç tane olduğunu bulur.
min=min(numbers)#Listedeki en küçük değeri bulur.
max=max(numbers)#Listedeki en büyük değeri bulur.
numbers.clear()#Listeyi temizler.

print("Üç tane araba markası giriniz...")
brands=[]
i=1
while( i<=3 ):
    brands.append(input(f"{i}.marka: "))
    i+=1
print(brands)
