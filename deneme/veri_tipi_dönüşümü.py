isOnline = True
a=20
b=3.4

isOnline = str(isOnline)

print(isOnline)
print(type(isOnline))

a= float(a)

print(a)
print(type(a))

b= int(b)
print(b)
print(type(b))

#------------------------

'''
Daire Alanı = π * r * r
daire çevre = 2 * π * r

'''
b = input ("Yarıçapı giriniz: ")

a = 3.14 * float(b) * float(b)

c= 2* 3.14 * float(b)

print("Dairenin alanı: ", a)
print("Dairenin çevresi: ", c)

print("Dairenin alanı: "+ str(a) + "Dairenin çevresi: " + str(c))
