def read():
    with open("day1_data.txt", "r") as file:
        data = []
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            data.append(int(row))
    return data

def simple_increases():
    data = read()
    increases = 0
    previous = data[0]

    for measurement in data:
        if measurement > previous:
            increases += 1
        previous = measurement

    print("Increases:", increases)

def sliding_window_increases():
    data = read()
    # data = [199,200,208,210,200,207,240,269,260,263]
    increases = 0
    previous_sum = sum(data[0:3])
    

    for i in range(len(data)-2):
        next_sum = sum(data[i:i+3])
        if next_sum > previous_sum:
            increases += 1
        previous_sum = next_sum

    print("Increases:", increases)


sliding_window_increases()