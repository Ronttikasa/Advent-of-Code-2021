def read():
    with open("day2_data.txt", "r") as file:
        data = []
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            parts = row.split(" ")
            data.append((parts[0], int(parts[1])))
    return data

def position():
    data = read()
    horizontal = 0
    depth = 0

    for row in data:
        direction = row[0]
        dist = row[1]
        if direction == "forward":
            horizontal += dist
        elif direction == "down":
            depth += dist
        elif direction == "up":
            depth -= dist

    print("horizontal position is", horizontal)
    print("depth is", depth)
    print("puzzle answer:", horizontal*depth)

def position_with_aim():
    data = read()
    horizontal = 0
    depth = 0
    aim = 0

    for row in data:
        direction = row[0]
        dist = row[1]
        if direction == "down":
            aim += dist
        if direction == "up":
            aim -= dist
        if direction == "forward":
            horizontal += dist
            depth += aim * dist

    print("horizontal position is", horizontal)
    print("depth is", depth)
    print("puzzle answer:", horizontal*depth)

position_with_aim()
