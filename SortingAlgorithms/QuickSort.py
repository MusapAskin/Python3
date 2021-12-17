#Şu ana kadar bilinen 
# en gözde ev hızlı algoritmadır. 
# Uygulama adımlarını şu şekilde sıralayabiliriz:

#Diziden herhangi bir eleman al(pivot elaman)
#Pivot elemanından küçük olanları bir diziye, büyükleri bir diziye topla.
#Bu alt dizilerden yukarıdaki gibi pivot elemanları seçip aynı işlemi uygula. İç içe en küçük parçalara ulaşana kadar bu yöntemi sürdür.
#Oluşan dizicikleri birleştir
arr=[3,44,38,5,47,15,26,27,2,46,4,19,50,48]

def parcalama(arr,low,high): 
    i = (low-1)       
    pivot_deger = arr[high]    
    for j in range(low , high): 
        if(arr[j] < pivot_deger): 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def QuickShort(arr,low,high): 
    if(low < high): 
        pivot_deger = parcalama(arr,low,high) 
        QuickShort(arr, low, pivot_deger-1) 
        QuickShort(arr, pivot_deger+1, high) 
        
QuickShort(arr,0,len(arr)-1)