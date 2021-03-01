data = input()
count0 = 0 # 모두 0으로 바꿈
count1 = 0 # 모두 1로 바꿈

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))