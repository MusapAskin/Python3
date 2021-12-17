from datetime import datetime

def  retirement():
    '''
    DOCSTRING: Ise giris tarihinize göre emekliliginizi hesaplar.
    INPUT: Ise baslangic tarihi.
    OUTPUT: Emeklilige kalan gün yazilir.
    '''
    jobBeginsDate=input('İşe Başlangıç Tarihiniz:(yıl/ay/gün) ').split('/')
    date=datetime(int(jobBeginsDate[0]),int(jobBeginsDate[1]),int(jobBeginsDate[2]))
    remainingdays=10000-(datetime.now()-date).days
    if  remainingdays>0:
        print(f'Emekliliğinize {remainingdays} gün kaldı.')
    else:
        print('Halihazırda emeklisiniz') 

print(retirement())