def solution(genres, plays):
    answer = []
    mapping: dict = {}
    for idx, genre in enumerate(genres):
        if genre not in mapping:
            mapping[genre] = [(plays[idx], idx)]
        else:
            mapping[genre].append((plays[idx], idx))

    sorted_mapping = sorted(mapping.items(), key=lambda x: -sum(p[0] for p in x[1]))

    for (_, plays_) in sorted_mapping:
        plays_.sort(key=lambda x: (-x[0], x[1]))
        plays_ = plays_[:2]
        answer.append([p[1] for p in plays_])
    answer = sum(answer, [])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

answer = solution(genres, plays)
print(f"answer >> {answer}")