def solution(numbers):
    result=0
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)
    answer.sort()
    return answer