def change_minutes(time):
    hour = time // 100
    minutes = time % 100
    return hour*60+minutes


def solution(schedules, timelogs, startday):
    answer = 0

    # 요일 파악하기
    holiday = [6, 7]

    for i in range(len(schedules)):
        current_day = startday
        schedule = change_minutes(schedules[i])
        for j in timelogs[i]: # 7일
            if current_day in holiday:
                current_day += 1
                if current_day == 8:
                    current_day = 1
                continue
            time = change_minutes(j)
            if schedule + 10 < time:
                break
            else:
                current_day += 1
        else:
            answer += 1
    print(f"answer >> {answer}")
    return answer


solution(
    [700, 800, 1100],
    [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]],
    5
)

solution(
    [730, 855, 700, 720], 
    [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]],
    1
)