from statistics import median

def read(file):
    with open (file, "r") as f:
        data = []
        for row in f:
            if not row.strip() == "":
                data.append(row.strip())
    return data

# data = read("day10_testdata.txt")
data = read("day10_data.txt")
data_incomplete = []

# -------------- part 1 -----------------

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0

for row in data:
    stack = []
    for char in row:
        if char in "([{<":
            stack.append(char)
        else:
            if f"{stack.pop()}{char}" in ["()", "[]", "{}", "<>"]:
                continue
            else:
                score += points[char]
                break
    else:
        # filter the data for part 2
        data_incomplete.append(row)

print("Part 1: the score is", score)


# -------------- part 2 -----------------

points = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

for row in data_incomplete:
    stack = []
    score = 0
    for char in row:
        if char in "([{<":
            stack.append(char)
        else:
            stack.pop()
    else:
        while len(stack) > 0:
            score *= 5
            score += points[stack.pop()]
        scores.append(score)

print("Part 2: The middle score is", median(scores))