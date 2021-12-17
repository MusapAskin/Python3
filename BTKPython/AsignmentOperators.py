x,y,z=2,5,107
numbers=1,5,7,10,6

number1=int(input("Birinci sayı: "))
number2=int(input("İkinci sayı: "))
result=(number1*number2)-(x+y+z)

# y'nin x'e kalansız bölünümü
# result=y //x 
#x,y,z toplaamının mod 3'ü
# result=(x+y+z)%3 
# y'nin x. kuvveti
# result=y**x 
x,*y,z = numbers
# z'nin küpü
# result=z**3
#y'nin elemanları toplamı
total=0;
for item in range(0,len(y)):
    total +=y[item]
print(total)


