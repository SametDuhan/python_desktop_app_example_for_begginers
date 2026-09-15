name="Alice"
surname="Johnson"
age=25

print("my name is {} {}".format(name,surname))

print("my name is {1} {0}".format(name,surname))

print("my name is {s} {n}".format(n=name,s=surname))

print("{0} {1} is {2} years old".format(name,surname,age))

print(f"my name is {surname} {name}")


result=100/589

print("The result is {r:1.3f}".format(r=result))