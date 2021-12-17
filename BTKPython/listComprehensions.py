numbers=[x for x in range(10)]

for x in range(10):
    numbers.append(x)
#Yukardaki iki kullanımda aynı işi yapar.

numbs=[x**2 for x in range(10)]

for x in range(10):
    numbs.append(x**2)
#Yukardaki iki kullanımda aynı işi yapar.

myStr='Hello'
myLs=[]

for letter in myStr:
    myLs.append(letter)
    
myLs2=[letter for letter in myStr]
#Yukardaki iki kullanımda aynı işi yapar.
#Farklı kullanımları;
result=[x if x%2==0 else 'Tek' for x in range(1,10)]
numbers2=[(x,y) for x in range(3) for y in range(3)]


