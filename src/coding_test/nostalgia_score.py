def solution(name, yearning, photo):
    answer = []
    # name과 yearning을 묶어준다
    info = dict(zip(name, yearning))
    
    for name_list in photo:
        scores = [info.get(key, 0) for key in name_list]
        answer.append(sum(scores))
    return answer

solution(
    ["may", "kein", "kain", "radi"], 
    [5, 10, 1, 3 ],
    [[ "may", "kein", "kain", "radi" ],
     [ "may", "kein", "brin", "deny" ],
     [ "kon", "kain", "may", "coni" ]]
)