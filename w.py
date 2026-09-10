
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("\n")


sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400) 

print(sum1)
print(sum2)
print(sum3)

print("\n")

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

print("\n")

x = 10

x += 5

print(x)

print("\n")

age = 18

print(age == 18)
print(age > 20)
print(age < 20)

print("\n")

age = 18
print(age == 28 or age >=23 )

is_raining = True
is_not_sunny = False
print(not is_raining)
print(not is_not_sunny)

print("\n")

gender = input("whats your gender:")

if gender =="male":
  print("you are such a gentleman")
elif gender =="female":
  print("you are such a cutie princess")
else:
    print("enter an actual gender or be at risk of getting rejected")  
