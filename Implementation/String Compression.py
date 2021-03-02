def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    return answer

arr = []
arr = input().split()
divisor = int(input())
elem = solution(arr, divisor)
print(elem)
