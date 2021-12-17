#Verinin hafızada sıralı tutulması için geliştirilen sıralama 
# algoritmalarından bir tanesidir.
# Basitçe sıralanacak olan diziyi ikişer elemanı kalan parçalara 
# inene kadar sürekli olarak ikiye böler daha sonra bu parçaları
# kendi içlerinde sıralayarak birleştirilir. Sonuçta elde edilen
# dizi sıralı dizinin kendisidir.
# Bu açıdan bir parçala fethet (divide and conquere) yaklaşımıdır.
# Sıralı iki veri grubunu
# birleştirerek üçüncü bir sıralı veri grubu elde etmeye dayanır.
arr=[3,44,38,5,47,15,26,27,2,46,4,19,50,48]

def merge(sol, sag):
	if not len(sol) or not len(sag):
		return sol or sag
	sonuc = []
	i, j = 0, 0
	while (len(sonuc) < len(sol) + len(sag)):
		if sol[i] < sag[j]:
			sonuc.append(sol[i])
			i+= 1
		else:
			sonuc.append(sag[j])
			j+= 1
		if i == len(sol) or j == len(sag):
			sonuc.extend(sol[i:] or sag[j:])
			break 
	return sonuc
def mergesort(arr):
	if len(arr) < 2:
		return arr
	orta = len(arr)//2
	sol = mergesort(arr[:orta])
	sag = mergesort(arr[orta:])

	return merge(sol, sag)