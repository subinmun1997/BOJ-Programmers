def solution(s):
    #s.upper()
    countp = 0
    county = 0
    for i in s:
        if i == 'P' or i == 'p':
            countp += 1
        elif i == 'Y' or i == 'y':
            county += 1
        else:
            continue
    if countp == county:
        answer = True
    elif countp != county:
        answer = False
    else:
        answer = True
    return answer