l = [5, 5, 6, 3, 5, 3, 2, 1, 1, 1]
d = {}.fromkeys(l, 0)
for i in d.keys():
    d[i] = l.count(i)
for i, j in d.items():
    print(i, ':', j)
print(max(d.items(), key = lambda x: x[1])[0])
l, h = min(l), max(l)
for i in range(l, h + 1):
    if i not in d.keys():
        print(i,': 0')

l = [5, 6, 5, 3, 4, 8, 5, 6]
a = []
for i in range(1, len(l)+1):
    a.append(l[0:i].count(l[i-1]))
print(a)
for i in range(0, len(l)):
    c = 0
    for j in range(0, i + 1):
        if l[i] == l[j]:
            c += 1
    print(c, end = " ")
print()
for i in range(len(l)):
    c = 0
    for j in range(i, len(l)):
        if l[i] == l[j]:
            c+=1
    print(c, end = " ")
print()
for i in l:
    print(l.count(i), end = " ")
print()

#leftrotate
n = int(input())
l = [5, 4, 6, 2, 1, 17, 25]
for i in range(n):
    for j in range(len(l)-1, 0, -1):
        l[j], l[j-1] = l[j-1], l[j]
print(l)

#rightrotate
n = int(input())
l = [5, 4, 6, 2, 1, 17, 25]
for i in range(n):
    for j in range(len(l)-1):
        l[j], l[j+1]= l[j+1], l[j]
print(l)

s1 = int(input())

#selection
l = [5, 4, 6, 2, 1, 17, 25]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)

#bubble
l = [5, 4, 1, 3, 2]
while True:
    w = 0
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            w = 1
            l[i], l[i+1] = l[i + 1], l[i]
    if not w:
        break
print(l)

#shifting
l = [5, 4, 7, 14, 1, 3, 2, 8]
s1 = int(input())
s2 = int(input())
t1 = input().lower()[0]
if t1 == 'l':
    for j in range(s2, s1 - 1, -1):
        l[j], l[j-1] = l[j-1], l[j]
elif t1 == 'r':
    for j in range(s1, s2+1):
        l[j], l[j+1] = l[j+1], l[j]
else:
    print("Invalid")
print(l)

#insertion
l = [5, 4, 7, 14, 1, 3, 2, 8]
for i in range(1, len(l)):
    key = l[i]
    j = i - 1
    while j >= 0 and key <= l[j]:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = key
print(l)
