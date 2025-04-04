def solution(s):
    answer = s
    map_dict = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "zero": 0
    }
    for key, value in map_dict.items():
        answer = answer.replace(key, str(value))
    print(f"answer >> {answer}")
    return answer

solution(
    "23four5six7"
)