def solution(numbers):
    result=0
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(list(set(answer)))