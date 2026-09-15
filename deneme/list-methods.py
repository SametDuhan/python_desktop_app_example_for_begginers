numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49) # APPEND METODU LİSTENİN SONUNA ELEMAN EKLER
numbers.append(59)
numbers.insert(3, 78) # INSERT METODU BELİRTİLEN İNDEXE ELEMAN EKLER
numbers.insert(-1,52)

# numbers.pop() POP METODU LİSTENİN SONUNDAN ELEMAN SİLER
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59) REMOVE METODU BELİRTİLEN ELEMANI SİLER


numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()


print(numbers)
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count('a'))

numbers.clear()
print(numbers)