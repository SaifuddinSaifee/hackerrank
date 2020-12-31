n = int(input())

l1, l2, d1 = [], [], {}

for x in range(n):
    a = input()
    b = float(input())
    d1[a] = b
    l1.append(b)

l1 = list(set(l1))
l1.sort()
v1 = l1[1]

for k, v  in d1.items():
    if v1 == v:
        l2.append(k)

l2.sort()
print(*l2, sep = "\n")