fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0]) indekslenemez

# SET İN LİST DEN FARKI SET DEĞERLİLERİ TEKRAR ETMEZ VE İNDEKSLENEMEZ

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])

fruits.remove('mango')
fruits.discard('apple')
fruits.pop()

fruits.clear()

print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))