def coin_change(n, coins):
    count = 0
    for coin in coins:
        count += n//coin
        n %= coin
    return count

coins = [500, 100, 50, 10]
n = 1260
# print(coin_change(n, coins))

# 종료시간이 가장 빠른 것을 기준으로 정렬
def max_meetings(meetings):
    count = 0
    meetings.sort(key=lambda x: x[1])
    print(f"meetings >> {meetings}")
    end_time = 0

    for meeting in meetings:
        if meeting[0] >= end_time:
            end_time = meeting[1]
            count += 1
    print(f"count >> {count}")
    return count

meetings = [(1, 4), (2, 3), (3, 5), (6, 7), (8, 9)]
max_meetings(meetings)


