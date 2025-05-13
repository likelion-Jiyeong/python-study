def solution(survey, choices):
    answer = ''
    score_map = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
                 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for idx, test in enumerate(survey):
        if choices[idx] >= 5:
            score_map[test[1]] += choices[idx] - 4
        elif choices[idx] <= 3:
            score_map[test[0]] += 4 - choices[idx]

    sorted_score_map = sorted(score_map.items(), key=lambda x: (-x[1], x[0]))
    keys_list = [x[0] for x in sorted_score_map]

    personality_list = ['RT', 'CF', 'JM', 'AN']
    for p in personality_list:
        answer += keys_list[min(keys_list.index(p[0]), keys_list.index(p[1]))]
    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
answer = solution(survey, choices)

print(f"answer >> {answer}")