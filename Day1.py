#Basic Fundamentals
integer = int(input())
string = input()
floating = float(input())
print(integer, string, floating)

num1 = int(input())
num2 = int(input())
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)

l = int(input("Length: "))
b = int(input("Breadth: "))
print("Perimeter =", 2 * (l + b) )
print("Area =", l * b)

r = float(input("radius: "))
print(f"Diameter = {r * 2}")
print(f"Circumference = {2 * 3.14 * r}")
print(f"Area = {3.14 * r * r}")

cm = int(input("Cm: "))
m = cm / 100
km = m / 1000
print(f"m = {m} km = {km}")

c = int(input())
f = (9 / 5) * c + 32
print(f)

f = int(input())
c = (f - 32) * ( 5 / 9)
print(c)

daystotal = int(input())
year = daystotal // 365
weeks = (daystotal % 365) // 7
days = (daystotal % 365) % 7
print(f"{year} years {weeks} weeks {days} days")

x = int(input())
y = int(input())
print(x ** y)

n = int(input())
print(n ** 0.5)

ang1 = int(input())
ang2 = int(input())
print(180 - (ang1 + ang2))

b = int(input())
h = int(input())
print(0.5 * b * h)

l = int(input())
print(((3 ** 0.5) / 4) * (l ** 2))

a = list(map(int, input().split()))
print(sum(a), sum(a)/ len(a), sum(a) / 100)

p = int(input())
t = int(input())
r = float(input())
print((p * t * r)/100)

p = int(input())
t = int(input())
r = float(input())
n = int(input())
print(p * ((1 + (r / n)) ** t))

# If - else

a = eval(input())
b = eval(input())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Equal")

a, b, c = map(eval, input().split())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

n = eval(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

n = int(input())
if n % 5 == 0 and n % 11 == 0:
    print("Yes")
else:
    print("Not divisible")

n = eval(input())
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

c = input()
if c.isalpha():
    print("Alphabet")
else:
    print("Not an alphabet")

c = input().lower()
if c in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

c = input()
if c.isalpha():
    print("Alphabet")
elif c.isdigit():
    print("Digit")
else:
    print("Special Character")

c = input()
if c.isalpha():
    if ord(c) >= 65 and ord(c) <= 90:
        print("UpperCase")
    else:
        print("Lowercase")

week = int(input())
if week == 1:
    print("Sunday")
elif week == 2:
    print("Monday")
elif week == 3:
    print("Tuesday")
elif week == 4:
    print("Wednesday")
elif week == 5:
    print("Thursday")
elif week == 6:
    print("Friday")
else:
    print("Saturday")

month = int(input())
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)

a, b, c = map(eval, input().split())
if a + b + c == 180 and a != 0 and b != 0 and c != 0:
    print("Valid triangle")
else:
    print("invalid triangle angles")

a, b, c = map(eval, input().split())
if (a + b) > c and (b + c) > a and (a + c) > b:
    print("Valid")
else:
    print("Invalid")

a, b, c = map(eval, input().split())
if a == b == c:
    print("Equilateral")
elif a==b or a == c or b==c:
    print("Isosceles")
else:
    print("Scalene")

a, b, c = map(eval, input().split())
d = b**2 - 4*a*c
if d > 0:
    x = (-b + d**0.5) / (2*a)
    y = (-b - d**0.5) / (2*a)
    print("real roots:", x, y)
elif d == 0:
    x = -b / (2*a)
    print("One real root:", x)
else:
    x = -b / (2*a)
    y = abs(d)**0.5 / (2*a)
    print("Complex roots:", f"{x}+{y}j", f"{x}-{y}j")

cp = eval(input())
sp = eval(input())
if sp > cp:
    print("Profit: ", sp - cp)
elif sp < cp:
    print("Loss", cp - sp)
else:
    print("No loss No profit")

marks = list(map(int, input().split()))
total = sum(marks)
p = (total / 5)
if p >= 90:
    print("Grade A")
elif p >= 80:
    print("Grade B")
elif p >= 70:
    print("Grade C")
elif p >= 60:
    print("Grade D")
elif p >= 40:
    print("Grade E")
else:
    print("Grade F")

bs = eval(input())
if bs <= 10000:
    hra, da = bs * 0.20, bs * 0.80
elif bs <= 20000:
    hra, da = bs * 0.25, bs * 0.90
else:
    hra, da = bs * 0.30, bs * 0.95
print(bs + hra + da)

units = eval(input())
if units <= 50:
    total = units * 0.50
elif units <= 150:
    total = 25 + (units - 50) * 0.75
elif units <= 250:
    total = 100 + (units - 150) * 1.20
else:
    total = 220 + (units - 250) * 1.50
surcharge = total * 0.20
print(total + surcharge)

#Switch - case

week = int(input())
match week:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")

month = int(input())
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(31)
    case 2:
        print(28)
    case _:
        print(30)

a = input().lower()
if a.isalpha():
    match a:
        case 'a'|'e'|'i'|'o'|'u':
            print('Vowel')
        case _:
            print("Consonant")

a, b = map(eval, input().split())
match a > b:
    case True:
        print(a)
    case False:
        print(b)

a = eval(input())
match a % 2 == 0:
    case True:
        print("Even")
    case False:
        print("Odd")

a = eval(input())
match a > 0:
    case True:
        print("positive")
    case False:
        match a == 0:
            case True:
                print("Zero")
            case False:
                print("Negative")

a, b, c = map(eval, input().split())
d = b**2 - 4*a*c
match d > 0:
    case True:
        x = (-b + d**0.5) / (2*a)
        y = (-b - d**0.5) / (2*a)
        print("real roots:", x, y)
    case False:
        match d == 0:
            case True:
                x = -b / (2*a)
                print("One real root:", x)
            case False:
                x = -b / (2*a)
                y = abs(d)**0.5 / (2*a)
                print("Complex roots:", f"{x}+{y}j", f"{x}-{y}j")

a, b, c = input().split()
match b:
    case '+':
        print(int(a) + int(c))
    case '-':
        print(int(a) - int(c))
    case '*':
        print(int(a) * int(c))
    case '/':
        print(int(a) / int(c))
    case '%':
        print(int(a) % int(c))
    case '//':
        print(int(a) // int(c))
