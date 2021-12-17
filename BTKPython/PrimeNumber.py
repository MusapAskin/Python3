number=int(input('Sayı(1 hariç): '))
isPrime=True

for i in range(2,number):
    if number==2:
        break
    elif(number%i==0):
        isPrime=False
        break
if isPrime:
    print(number, ' asal sayıdır.')
else:
    print(number, 'asal değildir.')