#Dizinin elemanları üzerinden ilk elemandan başlayarak ve her geçişte
# sadece yan yana bulunan iki eleman arasında sıralama yapılır. 
# Dizinin başından sonuna kadar tüm elemanlar bir kez işleme tabi
# tutulduğunda dizinin son elemanı (küçükten büyüğe sıralandığında)
# en büyük eleman haline gelecektir. Bir sonraki tarama ise bu
# en sağdaki eleman dışarıda bırakılarak gerçekleştirilmektedir. 
# Bu dışarıda bırakma işlemi de dış döngüdeki sayaç değişkeninin değerinin 
# her işletimde bir azaltılmasıyla sağlanmaktadır. 
# Sayaç değişkeninin değeri 1 değerine ulaştığında ise dizinin solunda kalan son 
# iki eleman da sıralanmakta ve sıralama işlemi tamamlanmaktadır.

arr=[4,3,2,1,5]

for i in range(len(arr)-1):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]
print(arr)