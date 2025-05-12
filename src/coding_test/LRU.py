def solution(cacheSize, cities):
    answer = 0
    cache: list = []

    for city in cities:
        city = city.lower()
        if len(cache) > cacheSize:
            del cache[0]

        if city not in cache:
            cache.append(city)
            answer += 5
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer

cacheSize = 3
cities = ["a", "b", "a", "c", "d", "a"]
answer = solution(cacheSize, cities)
print(f"answer >> {answer}")