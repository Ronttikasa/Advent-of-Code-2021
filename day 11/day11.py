def read(file):
    with open (file, "r") as f:
        data = []
        for row in f:
            data.append(row.strip())
    return [[int(c) for c in row] for row in data if not row == ""]

# data = read("day11_testdata.txt")
data = read("day11_data.txt")

# make borders to data so won't have to deal with invalid indices
data = [['x']*(len(data[0])+2)] + [['x'] + row + ['x'] for row in data] + [['x']*(len(data[0])+2)]

# ------------------------- part 1 -----------------------------

flashes_count = 0

for step in range(400):
    # energy level of each octopus increases by one
    data = [[x+1 if isinstance(x, int) else x for x in row] for row in data]

    # any octopus with energy level greater than 9 flashes, which increases the energy
    # level of the octopi around it, this continues until there are no more flashes this round.
    # an octopus can't flash more than once per round.
    flashes = True
    while flashes:
        flashes = False
        for i, row in enumerate(data):
            if i == 0 or i == len(data)-1:
                continue
            for j, elem in enumerate(row):
                if j == 0 or j == len(data[0])-1:
                    continue
                elif elem > 9:
                    flashes = True
                    flashes_count += 1
                    data[i][j] = -1
                    for (dy, dx) in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                        if isinstance(data[i+dy][j+dx], int) and not data[i+dy][j+dx] == -1:
                            data[i+dy][j+dx] += 1
    
    #set the energy of flashed octopuses back to zero
    data = [[0 if isinstance(x, int) and x == -1 else x for x in row] for row in data]

    if step == 99:
        print("Part 1: total flashes after 100 steps:", flashes_count)

    # check if all octopuses have flashed during the current step
    for row in data:
        if not set(row) == set(['x', 0]) and not set(row) == set(['x']):
                break
    else:
        print("Part 2: all the octopuses flash for the first time during step", step+1)
        break





# for row in data:
#     print(row)


