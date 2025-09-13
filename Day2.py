n = int(input())
for i in range(1, n+1):
    print(2 ** i, end= " ")
print()

n = int(input())
i = n - 1
while n > 0:
    print(i, end = " ")
    i += 2
    n -= 1
print()

n = int(input())
i = 65
for j in range(i, i+n):
    print(j, end = " ")
print()

n = int(input

())
i = 97
while n > 0:
    print(i, end = " ")
    i += 2
    n -= 1
print()

n= int(input())
for i in range(n):
    print("*$@")

n = int(input())
for i in range(n):
    print(chr(i + 65) + chr(122 - i))

n = int(input())
for i in range(n):
    print(chr(i + 97) + chr(i + 65))

n = int(input())
m = int(input())
for i in range(n):
    for i in range(n + 1):
        print("*", end = " ")
    print()

n = int(input())
m = int(input())
for i in range(2 * n):
    for j in range(m):
        if i % 2 == 0:
            print("$@",end = "")
        else:
            print(f"*{j+1}", end = "")
    print()

n = int(input())
m = int(input())
for i in range(n):
    for j in range(1, m+1):
        print(m * i + j, end = ' ')
    print()

n = int(input())
m = int(input())
p = m - 1
for i in range(n):
    for j in range(m):
        if j < p:
            print("*", end = " ")
        else:
            print("@", end = " ")
    p -= 1
    print()
