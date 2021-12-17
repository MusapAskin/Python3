# name=input("Adınız: ")
# age=int(input("Yaşınız: "))
# education=input("Eğitim durumunuz: ")
# if(age>=18 and (education=='lise' or  education=='üniversite') ):
#     print(f"Merhaba {name}, ehliyet alabilirsin.")
# else:
#     print("Ehliyet alma şartlarını sağlamıyorsunuz.")

# vize=int(input("Vize: "))
# vize2=int(input("Vize2: "))
# final=int(input("final: "))
# avr=(vize+vize2+final)/3
# if(avr>=0 and avr<=24 ):
#     print("Notunuz: 0")
# elif(avr>=25 and avr<=44 ):
#     print("Notunuz: 1")
# elif(avr>=45 and avr<=54 ):
#     print("Notunuz: 2")
# elif(avr>=55 and avr<=69 ):
#     print("Notunuz: 3")
# elif(avr>=70 and avr<=84 ):
#     print("Notunuz: 4")
# else:
#     print("Notunuz: 5")
from datetime import date, datetime
date=input('Aracınızın trafiğe çıkış tarihi:(yıl/ay/gün) ').split('/')
trafficReleaseDate=datetime(int(date[0]),int(date[1]),int(date[2]))
pastDay=(datetime.now()-trafficReleaseDate).days
if pastDay<=365:
    print('1.Servis')
elif pastDay>365 and pastDay<=365*2:
    print('2.Servis')
elif pastDay>365*2 and pastDay<=365*3:
    print('2.Servis')
else:
    print('Hatalı süre.')    