def solution(s):
    answer: list = []

    for idx, value in enumerate(s[:-2]):
        if value == s[idx+1] and value == s[idx+2]:
            answer.append(value)
    
    max_number = max(answer)
    if len(answer) == 0:
        return -1
    else:
        return max_number * 3

answer = solution("111999333")
print(f"answer >> {answer}")