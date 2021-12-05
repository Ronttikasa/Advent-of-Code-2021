def read():
    with open("day5_data.txt", "r") as file: 
    # with open("day5_testdata.txt", "r") as file:
        data = []
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            parts = row.split(" ")
            start = parts[0].split(",")
            end = parts[2].split(",")
            data.append([(int(start[0]), int(start[1])), (int(end[0]), int(end[1]))])
    return data

# rakennetaan apuruudukko
def create_grid(data: list):
    max_x = 0
    max_y = 0
    for line in data:
        x = max(line[0][0], line[1][0])
        y = max(line[0][1], line[1][1])
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    grid = []
    for i in range(max_y+1):
        grid.append([0]*(max_x+1))
    
    return grid


def crossing_lines():
    data = read()
    grid = create_grid(data)

    # merkitään suorat apuruudukkoon
    for line in data:
        start = line[0]
        end = line[1]

        # pystysuuntaiset suorat
        if start[0] == end[0]:
            if start[1] > end[1]:
                start, end = end, start
            for i in range(start[1], end[1]+1):
                grid[i][start[0]] +=1

        # vaakasuuntaiset suorat    
        elif start[1] == end[1]:
            if start[0] > end[0]:
                start, end = end, start
            for i in range(start[0], end[0]+1):
                grid[start[1]][i] += 1

        # vinottaiset suorat
        else:
            if start[0] > end[0]:
                start, end = end, start

            # laskevat suorat
            if start[1] < end[1]:
                j = start[0]
                for i in range(start[1], end[1]+1):
                    grid[i][j] += 1
                    j += 1
            # nousevat suorat
            if start[1] >= end[1]:
                j = end[0]
                for i in range(end[1], start[1]+1):
                    grid[i][j] += 1
                    j -= 1

    

    # lasketaan leikkauskohdat
    overlaps = 0

    for row in grid:
        # print(row)
        for point in row:
            if point >= 2:
                overlaps += 1

    return overlaps

print(crossing_lines())