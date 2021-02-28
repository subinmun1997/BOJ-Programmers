n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0
for i in data: # 1 2 2 2 3
    count += 1
    if count >= i:
        result += 1
        count = 0
    else:
        continue

print(result)