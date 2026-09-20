
    # Largest three numbers
print("Find the largest of three numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

# Whether leap year or not
print("Check if a year is leap year or not:")

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Whether character is vowel or consonant
print("Check if a character is vowel or consonant:")

ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

# Divisible by both 5 and 11
print("Check if a number is divisible by both 5 and 11:")

n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

# Sum of first N number using while
print("Sum of first N numbers:")

n = int(input("Enter N: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)

# Multiplication table using while
print("Multiplication table:")

n = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1

# Pyramid pattern
print("Pyramid pattern:")
for i in range(1, 5):
    print(" " *(4 -i)+"**" * (2 * i - 1))

# Number pattern
print("Number pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
