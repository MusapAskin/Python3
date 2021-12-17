import random

numberOfRights=int(input('Kaç hakkınız olsun? : '))
nor=numberOfRights
randomNumber=random.randint(1,10)
count=0
while True:
    if numberOfRights!=0:
        guss=int(input('Tahmin ettiğiniz sayı nedir? : '))
        count+=1
        if randomNumber==guss:
            print(f'Tebrikler! {count}. Tahmininiz Doğru. Puanınız: {100-(100/nor)*(count-1)}')
            break
        elif randomNumber<guss:
            print('Aşağı')
            numberOfRights-=1
        elif randomNumber>guss:
            print('Yukarı')
            numberOfRights-=1
    else:
        print('Üzgünüm! Hakkınız kalmadı.Doğru cevap:',randomNumber)
        break    