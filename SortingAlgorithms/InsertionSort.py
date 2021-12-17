
#Yerleştirerek sıralama işlevi belirli bir anda dizinin belirli
# bir kısmını sıralı tutarak ve bu kısmı her adımda biraz daha
# genişleterek çalışmaktadır. Sıralı kısım işlev son bulunca dizinin
# tamamına ulaşmaktadır. Elemanların sırasına uygun olarak 
# listeye tek tek eklenmesi ile gerçekleştirilen sıralamadır.

arr=[3,44,38,5,47,15]

for i in range(1,len(arr)):
    value = arr[i]
    j = i-1
    while(j>= 0 and value < arr[j]):
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = value

print(arr)