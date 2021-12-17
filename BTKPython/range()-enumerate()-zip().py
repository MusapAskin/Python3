for i in range(1,10,2):
    print(i)

print(list(range(1,10,2)))

gretting='Hello'
for index,letter in enumerate(gretting):
    print(index,letter)
    
l1=[1,2,3]
l2=['a','b','c']
l3=[10,20,30]
print(list(zip(l1,l2,l3)))
for item in zip(l1,l2,l3):
    print(item)
    