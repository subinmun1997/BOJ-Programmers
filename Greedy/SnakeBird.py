n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in range(n):
    if h[i] <= l:
        l += 1

print(l)