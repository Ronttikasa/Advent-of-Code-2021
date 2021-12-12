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
            data.append([int(start[0]), int(start[1]), int(end[0]), int(end[1])])
    return data

# rakennetaan apuruudukko
def create_grid(data: list):
    max_x = 0
    max_y = 0
    for line in data:
        x = max(line[0], line[1])
        y = max(line[2], line[3])
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
        x1, y1, x2, y2 = line[0], line[1], line[2], line[3]

        # pystysuuntaiset suorat
        if x1 == x2:
            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for i in range(y1, y2+1):
                grid[i][x1] +=1

        # vaakasuuntaiset suorat    
        elif y1 == y2:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            for i in range(x1, x2+1):
                grid[y1][i] += 1

        # vinottaiset suorat
        else:
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1

            # laskevat suorat
            if y1 < y2:
                j = x1
                for i in range(y1, y2+1):
                    grid[i][j] += 1
                    j += 1
            # nousevat suorat
            if y1 >= y2:
                j = x2
                for i in range(y2, y1+1):
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