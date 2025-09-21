#sliding window
l = list(map(int, input().split()))
k = int(input())
for i in range(0, len(l)-k + 1):
    sum = 0
    for j in range(i,k+i):
        sum += l[j]
    print(sum)

#sliding window 2
s = 0
i = 0
j = 0
while i < len(l) - k + 1:
    while j - i + 1 <= k:
        s += l[j]
        j += 1
    print(s)
    s -= l[i]
    i += 1

#maximum sum
s = 0
i = 0
j = 0
h = 0
while i < len(l) - k + 1:
    while j - i + 1 <= k:
        s += l[j]
        j += 1
    if s > h:
        h = s
    s -= l[i]
    i += 1
print(h)

#unique substring
s = input()
k = int(input())
for i in range(len(s) - k + 1):
    a = ''
    for j in range(i, k+i):
        a += s[j]
    if len(a) == len(set(a)):
        print(a)

s = input()
k = int(input())
a = set()
i = 0
j = 0
while i < len(s) - k + 1:
    while j - i + 1 <= k:
        a.add(s[j])
        j += 1
    if len(a) == k:
        print(''.join(a))
        a.discard(s[i])
    i += 1

#techiedelight
l = list(map(int, input().split()))
k = int(input())
w = 0
i = 0
while i < len(l) - 1:
    if w == 0:
        j = i + 1
        while j - i <= k and j < len(l):
            if l[i] == l[j]:
                w = 1
                print(True)
                break
            j += 1
    i += 1
if not w:
    print(False)
