#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def read():
    patterns = []
    output = []
    with open("day8_data.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            parts = row.split("|")
            patterns.append(parts[0])
            output.append(parts[1])
    return [patterns, output]
        

def get_patterns(data):
    return [sorted(pattern.split(" ")[:-1], key=len) for pattern in data[0]]

def get_outputs(data):
    return [pattern.split(" ")[1:] for pattern in data[1]]
    
def easy_digits():
    data = read()
    data = get_outputs(data)

    count = 0
    for row in data:
        for val in row:
            if len(val) in [2,3,4,7]:
                count += 1

    print(f"Part 1: digits 1, 4, 7, 8 appear {count} times")

def all_digits():
    data = read()
    signals = get_patterns(data)
    outputs = get_outputs(data)
    signals_decoded = []

    # The original display segments (see image above) are mapped a=0, b=1, ..., g=6
    # The segments dict is used to keep tabs of the values a...g that are
    # possible candidates for that segment of the physical seven segment display
    segments = {}

    for row in signals:
        mappings = [""]*10 # the pattern corresponding to the index value
        for x in range(7):
            segments[x] = [] # clear the segment dict

        # loop through the row so long that we find all the digits
        # we want to find 1, 7 and 4 first, then 9, then 6 and 0, then 2, 5, 3.
        # (8 is a trivial case that can be found at any point)

        while True:
            for val in row:
                # finds 1
                if len(val) == 2 and not mappings[1]:
                    mappings[1] = val
                    for char in val:
                        segments[2].append(char)
                        segments[5].append(char)
                # finds 7
                if len(val) == 3 and not mappings[7]:
                    mappings[7] = val
                    for char in val:
                        if char not in mappings[1]:
                            segments[0].append(char)
                            break
                # finds 4
                if len(val) == 4 and not mappings[4]:
                    mappings[4] = val
                    for char in val:
                        if char not in mappings[1]:
                            segments[1].append(char)
                            segments[3].append(char)

                # these are the last signals to be decoded
                if len(val) == 5 and mappings[0] and mappings[6]:
                    for char in val:
                        if char in segments[1]:
                            mappings[5] = val
                            break
                        elif char in segments[4]:
                            mappings[2] = val
                            break
                    else:
                        mappings[3] = val

                # finds 9
                if len(val) == 6 and not mappings[9]:
                    extra = ""
                    for char in val:
                        if char not in mappings[4] and char not in mappings[7]:
                            extra += char
                    if len(extra) == 1:
                        mappings[9] = val
                        segments[6].append(char)
                        continue

                # finds 6 and 0
                if len(val) == 6 and mappings[9]:
                    if segments[4] == []:
                        for char in val:
                            if char not in mappings[9]:
                                break   
                        segments[4].append(char)
                    for char in mappings[1]:
                        if char not in val and not mappings[6]:
                            mappings[6] = val
                            segments[5].remove(char)
                            segments[2].remove(segments[5][0])
                            break
                    else:
                        if not mappings[0]:
                            mappings[0] = "".join(sorted(val))
                            for char in mappings[4]:
                                if char not in val:
                                    segments[1].remove(char)
                                    segments[3].remove(segments[1][0])

                # finds 8
                if len(val) == 7 and not mappings[8]:
                    mappings[8] = val

            # break when we have all the five-segment digits
            if mappings[2] and mappings[3] and mappings[5]:
                break
        
        signals_decoded.append(mappings)        

    # form outputs and sum them
    sum_of_output = 0                

    for i in range(len(outputs)):
        output_str = ""
        for output in outputs[i]:
            for j, val in enumerate(signals_decoded[i]):
                if "".join(sorted(output)) == "".join(sorted(val)):
                    output_str += str(j)
                    break
        sum_of_output += int(output_str)
        
    print(f"Part 2: output values added up: {sum_of_output}")



easy_digits()
all_digits()