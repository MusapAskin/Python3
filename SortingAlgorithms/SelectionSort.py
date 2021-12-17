#Selection Sort (Seçerek Sıralama) aslında performans bakımından 
# diğer sıralama algoritmalarına kıyasla bir tık zayıf kalsa da zor
# durumlarımızda bize yardımcı oluyor. Uygulaması oldukça basit olan
# bu algoritma dizinin ilk elemanının en küçük eleman olduğunu varsayıyor.
# Ardından tek tek bu elemanı diğer elemanlarla karşılaştırıyor.
# Eğer karşılaştırdığı eleman daha küçük ise onu en küçük değer olarak 
# alıyor ve ilk eleman yerine artık diğer elemanları onunla karşılaştırıyor.
# Dizinin sonuna vardığında ise en küçük elemanı dizinin başına yazıyor.
# Ardından bu işlemi 2. elemandan başlayarak yapıyor ve bulduğu en küçük
# değeri 2. sıraya koyuyor benzer şekilde işlemi dizinin son elemanına kadar
# aynı şekilde tekrarlıyor. 
# Selection Sort’un kodlaması kısmı ise şu şekilde :
array =[1,44,43,25,67]

for i in range(len(array)):
    minId=i
    for j in range(i+1,len(array)):
        if array[j]<array[minId]:
            minId=j
    array[i],array[minId]=array[minId],array[i]
print(array)