def solution(year):
    x = year % 100
    if x == 0:
        return year // 100
    else:
        return year // 100 + 1
