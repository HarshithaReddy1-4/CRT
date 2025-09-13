#factors of the number
n = int(input())
a = [1, n]
for i in range(2, int(n ** 0.5)+ 1):
    if n % i == 0:
        if i == n//i:
            a.append(i)
        else:
            a.extend([i, n//i])
print(*sorted(a), sep = ', ')
print(len(a))

if (len(a) % 2 != 0):
    print("Perfect Square")
else:
    print("Non Perfect Square")

if len (a) == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

#perfect sqaure or not
n = int(input())
sq = n ** 0.5
if sq == int(sq):
    print("Perfect Square")
else:
    print("Non Perfect square")

#prime or composite
n = int(input())
c = 56
for i in range(2, int(n ** 0.5)+ 1):
    if n % i == 0:
        c = 0
        break
if c:
    print("Prime Number")
else:
    print("Composite number")

#no. of primes btw given range
s = int(input())
e = int(input())
pc, cc = 0, 0
for k in range(s, e + 1):
    n = k
    c = 56
    for i in range(2, int(n ** 0.5)+ 1):
        if n % i == 0:
            c = 0
            break
    if c:
        pc += 1
    else:
        cc += 1
print("Prime Number count:", pc)
print("Composite number count:", cc)

n = int(input())
m = n
pc, npc = 0, 0
h = 0
while m > 0:
    p = m % 10
    c = 56
    for i in range(2, int(p ** 0.5)+ 1):
        if p % i == 0:
            c = 0
            break
    if c:
        pc += 1
    else:
        if p > h:
            h = p
        npc += 1
    m //= 10
print(pc, npc)
f = h
for i in range(2, h):
    f *= i 
print(f)

#fibonacci
n = int(input())
f1, f2 = 0, 1
if n == 1:
    print(f1)
elif n == 2:
    print(f1, f2)
else:
    print(f1, f2, end = " ")
    for i in range(n - 2):
        f3 = f1 + f2 
        print(f3, end = " ")
        f1, f2 = f2, f3
print()

#2 3 0 5 8 13 26 n1=2, n2=3, n3=0, n=7
n1, n2, n3 = map(int, input().split())
n = int(input())
print(n1, n2, n3, end = " ")
sum = n1 + n2 + n3
for i in range(n-3):
    ans = n1 + n2 + n3
    print(ans, end = " ")
    sum += ans
    n1 = n2
    n2 = n3 
    n3 = ans
print(f"\n{sum}")

#gcd
n = list(map(int, input().split()))
a, b = max(n), min(n)
r = b % a
while r != 0:
    b = a
    a = r
    r = b % a
print(a)
#lcm
print((max(n) * min(n))/a)

#sort according to the index 1 in each list
a = [[4, 3, 6], [3,1, 6], [2, 5, 7], [1, 6, 4]]
print(sorted(a, key = lambda x: x[1]))
