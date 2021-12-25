def score(i):
    if i < 60:
        return "Bad"
    if i < 90:
        return "Good"
    if i < 100:
        return "Great"
    return "Perfect"


print(score(int(input())))
