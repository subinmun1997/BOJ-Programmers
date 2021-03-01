data = input()

half = len(data) // 2

left = 0
right = 0
for i in range(0, half):
    left += int(data[i])
for j in range(half,len(data)):
    right += int(data[j])

if left == right:
    print("LUCKY")
else:
    print("READY")