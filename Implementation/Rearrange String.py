s = input()
total = 0
alphabet = []

for i in s:
    if i.isalpha():
        alphabet.append(i)
    else:
        total += int(i)

alphabet.sort()

if total != 0:
    alphabet.append(str(total))

print(''.join(alphabet)) # 리스트를 문자열로 바꿔주는 join
