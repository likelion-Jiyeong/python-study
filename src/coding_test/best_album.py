from typing import Dict

def solution(genres, plays):
    answer = []
    # 딕셔너리로 classic : [값 append]

    # classic: [{0:500}, {2:150}, {3,800}], pop: [600, 2500]
    # classic 에서 가장 높은 거 순으로 sort 하기

    mapping1: Dict[list] = {}
    mapping2: Dict[list] = {}

    for idx, genre in enumerate(genres):
        if genre not in mapping1:
            mapping1[genre] = [(plays[idx], idx)]
        else:
            mapping1[genre].append((plays[idx], idx))
        if genre not in mapping2:
            mapping2[genre] = [plays[idx]]
        else:
            mapping2[genre].append(plays[idx])

    print(f"mapping1 >> {mapping1}")
    print(f"mapping2 >> {mapping2}")
    
    sorted_mapping2 = sorted(mapping2.items(), key=lambda x: sum(x[1]), reverse=True)
    
    for genre, plays in sorted_mapping2:
        sorted_mapping1 = sorted(mapping1[genre], key=lambda x: x[0], reverse=True)
        answer.append([idx[1] for idx in sorted_mapping1[:2]])
    answer = sum(answer, [])
    print(f"answer >> {answer}")
    return answer


solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
)