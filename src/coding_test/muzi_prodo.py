from collections import Counter



def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for r in set(report):
        a,b = r.split()
        reported[b] += 1

    for r in set(report):
        a,b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer


# def solution(id_list, report, k):
#     answer = []
#     sued = []
    
#     report_set = list(set(report))
#     # 각 이용자별 신고당한 횟수
#     for case in report_set:
#         sued.append(case.split(' ')[1])
        
#     counter = Counter(sued)
#     stopped_ids = [key for key, count in counter.items() if count >= k]
    
#     # 신고한 ID
#     sued_map: dict = {}
#     sued_count_map: dict = {}
    
#     for id in id_list:
#         for case in report:
#             sue_id, sued_id = case.split(' ')
#             if id == sue_id:
#                 if id not in sued_map:
#                     sued_map[id] = [sued_id]
#                 else:
#                     sued_map[id].append(sued_id)
        
#         print(f"sued_map >> {sued_map}")
                        
#         for stopped_id in stopped_ids:
#             if id not in sued_map:
#                 sued_count_map[id] = 0

#             if stopped_id in sued_map.get(id, []):
#                 if id not in sued_count_map:
#                     sued_count_map[id] = 1
#                 else:
#                     sued_count_map[id] += 1

#     print(sued_count_map)
#     answer = list(sued_count_map.values())
#     if len(answer) == 0:
#         answer = [0 for _ in range(len(id_list))]
#     print(answer)
            
    
        
#     return answer

solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    2
)
solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
)