def solution(n, w, num):
    answer = 0
    h = n//w+1
    x = 1
    storage = []

    for i in range(h):
        t = []
        for j in range(w):
            if x <= n:
                t.append(x)
                x += 1
            else:
                t.append(0)
        if i % 2 == 0:
            storage.append(t)
        else:
            t.reverse()
            storage.append(t)
    print(f"storage >> {storage}")

    for i in range(len(storage)):
        for j in range (len(storage[0])):
            if storage[i][j] == num:
                d = i
                while d < h and storage[d][j]:
                    answer += 1
                    d += 1

    print(f"answer >> {answer}")




solution(13, 3, 6)
solution(22, 6, 8)