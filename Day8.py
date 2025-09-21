#maximum
l = list(map(int, input().split()))
k = int(input())
t, r = [], []
i, j = 0, 0
while i < len(l) -k + 1:
    while len(t) != 0 and l[j] > t[-1]:
            t.pop(-1)
    t.append(l[j])
    if j - i + 1 == k:
        r.append(t[0])
        if l[i] == t[0]:
            t.pop(0)
        i += 1
    j += 1
print(*r)

#minimum
l = list(map(int, input().split()))
k = int(input())
t, r = [], []
i, j = 0, 0
while i < len(l) -k + 1:
    while len(t) != 0 and l[j] < t[-1]:
            t.pop(-1)
    t.append(l[j])
    if j - i + 1 == k:
        r.append(t[0])
        if l[i] == t[0]:
            t.pop(0)
        i += 1
    j += 1
print(*r)

#first negative
l = list(map(int, input().split()))
k = int(input())
t, r = [], []
i, j = 0, 0
while i < len(l) -k + 1:
    while len(t) != 0 and l[j] < t[-1]:
            t.pop(-1)
    if l[j] < 0:
        t.append(l[j])
    if j - i + 1 == k:
        r.append(t[0] if len(l) else 0)
        if len(t) > 0 and l[i] == t[0]:
            t.pop(0)
        i += 1
    j += 1
print(*r)
