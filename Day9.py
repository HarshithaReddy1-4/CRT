w = 0
s1, s2 = input().split()
d = {}
if len(s1) == len(s2):
    for i in s1:
        d[i] = 1 if i not in d else d[i] + 1
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            break
    if all(i == 0 for i in d.values()):
        w = 1
if w:
    print("Anagram")
else:
    print("Not an Anagram")
s = input().lower()
d = {}
for i in range(97, 123):
    d[chr(i)] = 0
for i in s:
    if i in d.keys():
        d[i] += 1
if all(i>0 for i in d.values()):
    print("Pangram")
else:
    print("Not a pangram")

l = [1, 5, 0, 2, 6, 0, 0, 1, 2, 3, 1]
k = 1
i, j, s, m = 0, 0, 0, 0
while j < len(l):
    s += l[j]
    while s > k:
        s -= l[i]
        i += 1
    if s == k:
        m = max(m, j -i + 1)
    j += 1
print(m)

