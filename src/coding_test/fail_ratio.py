def solution(N, stages):
    answer = []
    result_map = {}

    total_people = len(stages)
    for i in range(1, N+1):
        if stages.count(i) == 0:
            fail_ratio = 0
        else:
            fail_ratio = stages.count(i) / total_people
            total_people -= stages.count(i)
        result_map[i] = fail_ratio
        
    result_map = sorted(result_map.items(), key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in result_map]

    return answer

N = 2
stages = [1, 1, 1, 1]
answer = solution(N, stages)
print(f"answer >> {answer}")