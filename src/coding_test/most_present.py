def solution(friends, gifts):
    answer = [0] * len(friends)
    table = [[0 for _ in range(len(friends))] for __ in range(len(friends))]

    # 지수 계산
    gift_index = [0] * len(friends)
    for gift in gifts:
        give, take = gift.split()
        give_idx, take_idx = friends.index(give), friends.index(take)
    
        gift_index[give_idx] += 1
        gift_index[take_idx] -= 1
        table[give_idx][take_idx] += 1

    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            if table[i][j] > table[j][i]:
                answer[i] += 1
            elif table[i][j] == table[j][i]:
                if gift_index[i] > gift_index[j]:
                    answer[i] += 1

    return max(answer)

result = solution(
    ["muzi", "ryan", "frodo", "neo"],
    ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
)
print(f"result >> {result}")