def read():
    with open("day3_data.txt", "r") as file:
        data = []
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            data.append(row)
    return data

def power_consumption():
    data = read()
    # data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    # data = ["00100"]
    zeros = [0]*len(data[0])
    ones = [0]*len(data[0])
    for row in data:
        for i, char in enumerate(row):
            if char == "0":
                zeros[i] += 1
            elif char == "1":
                ones[i] += 1
    gamma_rate = ""
    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    gamma_rate_dec = int(gamma_rate,2)
    epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)
    epsilon_rate_dec = int(epsilon_rate,2)

    print(f"{gamma_rate_dec} * {epsilon_rate_dec} = {gamma_rate_dec*epsilon_rate_dec}")

def most_common_values(data):
    zeros = [0]*len(data[0])
    ones = [0]*len(data[0])
    for row in data:
        for i, char in enumerate(row):
            if char == "0":
                zeros[i] += 1
            elif char == "1":
                ones[i] += 1
    result = ""
    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            result += "0"
        else:
            result += "1"

    return result

def least_common_values(data):
    zeros = [0]*len(data[0])
    ones = [0]*len(data[0])
    for row in data:
        for i, char in enumerate(row):
            if char == "0":
                zeros[i] += 1
            elif char == "1":
                ones[i] += 1
    result = ""
    for i in range(len(zeros)):
        if zeros[i] <= ones[i]:
            result += "0"
        else:
            result += "1"

    return result

def oxygen_gen_rating():
    data = read()
    # data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    length = len(data[0])

    for i in range(length):
        criteria = most_common_values(data)
        if len(data) == 1:
            break
        keep = []
        for number in data:
            if number[i] == criteria[i]:
                keep.append(number)
        data = keep

    return data[0]

def co2_scrubber_rating():
    data = read()
    # data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    length = len(data[0])

    for i in range(length):
        criteria = least_common_values(data)
        if len(data) == 1:
            break
        keep = []
        for number in data:
            if number[i] == criteria[i]:
                keep.append(number)
        data = keep
    return data[0]
            
def life_support_rating():
    oxygen = int(oxygen_gen_rating(),2)
    co2 = int(co2_scrubber_rating(),2)
    print("The life support rating is", oxygen*co2)

life_support_rating()
