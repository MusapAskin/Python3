fruits={'orange','banana','apple'}
#print(fruits[0]) indilenemez, sıralanamaz ve b,r elemandan yalnızca bir tane içerir.

for i in fruits:
    print(i)
fruits.add('cherry')
fruits.update(['mango','grape','apple'])
fruits.remove('apple')
fruits.discard('cherry')
fruits.clear()