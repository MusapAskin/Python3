#Key-Value şeklinde çalışır.
#print(plates['istanbul']) => 34
# Dictionary={'Key' : 'Value'}
# plates={'istanbul':34}
#print(plates['istanbul'])
# plates['Ankara']=6
#print(plates)
# users={
#     'Musap Aşkın':{
#         'age':23,
#         'roles':['admin','user'],
#         'email':'musapfc.tr@gmail.com',
#         'adress':'İstanbul/Turkey',
#         'phone':'05318368520'
#     }
# }
#print(users['Musap Aşkın']['roles'][0])

#Dictionary Application

Students={}
while True:
    print("---------------------------------\n"
          "1 - Yeni Öğrenci\n"
          "2 - Öğrenci Ara\n"
          "3 - Çıkış"
          "\n---------------------------------")
    num=input()
    if(num=='1'):
        number=int(input("Numarası: "))
        name=input("Adı: ")
        surname=input("Soyadı: ")
        phone=int(input("Telefonu: "))
        Students.update({
            number:{
                'ad':name,
                'soyad':surname,
                'telefon':phone
                }
        }) 
    elif(num=='2'):
            number=int(input("Öğrenci Numarası: "))
            if(number in Students):
                print(f"\nAradığınız {number} nolu öğrencinin ; "
                      f"Adı: {Students[number]['ad']}, "
                  f"Soyadı: {Students[number]['soyad']}, "
                  f"Telefonu: {Students[number]['telefon']}\n")
            else:
                print("\n\t\tYanlış numara!.Tekrar Deneyiniz...\n")
    elif(num=='3'):
        break    
    else:
        print("---------------------------------\n"
               "Hatalı Giriş. Tekrar deneyiniz...\n"
              "---------------------------------")
   
        

            
            
            
    
    

    