import sys

n = int(input())
sum, prod = 0, 1
while n > 0:
    sum += n
    prod *= n
    n -= 1
print("sum: ", sum)
print("prod: ", prod)


#given base to other
n = int(input())
g = int(input())
d = int(input())
m = n
while (m > 0):
    if m % 10 > g:
        print("Invalid No.")
        sys.exit()
    m = m // 10

if not (g == 10 or d == 0):
    count, sum = 0, 0
    while n > 0:
        p = n % 10
        sum += (p * (g ** count))
        count += 1
        n = n // 10
    ans, count = 0, 0
    while sum > 0:
        p = sum % d
        ans += (p * (10 ** count))
        count += 1
        sum = sum //d
    print(ans)
else:
    ans, count = 0, 0
    while n > 0:
        p = n % d
        ans += (p * (g ** count))
        count += 1
        n = n //d
    print(ans)

#coverting given no. into its highest base and displaying its reversed decimal
n = int(input())
h, m = 0, n
sum, count = 0, 0
while m > 0:
    p = m % 10
    if p > h:
        h = p
    m = m // 10
while n > 0:
    p = n % h
    sum += (p * (10 ** count))
    count += 1
    n = n//h
r = 0
while sum > 0:
    p = sum % 10
    r = (r * 10) + p
    sum = sum // 10
ans, count = 0, 0
while r > 0:
    p = r % 10
    ans += (p *(h ** count))
    count += 1
    r = r // 10
print(ans)

#sum of factorial of digits in given number
n = int(input())
sum = 0
while n > 0:
    p = n % 10
    prod = 1
    while p > 0:
        prod *= p
        p -= 1
    sum += prod
    n //= 10
print(sum)

n = int(input())
sum = 0
while n > 9:
    p = n % 100
    r = 0
    while p > 0:
        r = (r * 10) + (p % 10)
        p = p//10
    sum += r
    n = n // 10
print(sum)

n = int(input())
place = 1
m = 0
while n > 0:
    p = n % 10
    if place % 2 != 0:
        m = (m * 10)  + p
    place += 1
    n = n // 10
h, l = 0, 9
while m > 0:
    p = m % 10 
    if p > h:
        h = p
    if p < l:
        l = p
    m = m // 10
prodh, prodl = 1, 1
for i in range(1, h + 1):
    prodh *= i
for i in range(1, l + 1):
    prodl *= i
print(prodh + prodl)

n = int(input())
l, m = 9, n
sum, count = 0, 0
while m > 0:
    p = m % 10
    if p < h:
        l = p
    m = m // 10
while n > 0:
    p = n % h
    sum += (p * (10 ** count))
    count += 1
    n = n//h
r = 0
s = 0
while sum > 0:
    p = sum % 10
    f= 0
    for i in range(1, p+1):
        f *= i
    s += f
print(s)
