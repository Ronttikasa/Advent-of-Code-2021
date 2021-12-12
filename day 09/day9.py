def read(file):
    with open (file, "r") as f:
        data = []
        for row in f:
            row = row.strip()
            if row == "":
                continue
            data.append(row)
    data = [[int(c) for c in row] for row in data]
    return data

def find_neighbours(data, i, j):
    if i == 0:
        y_up = 10
    else:
        y_up = data[i-1][j]
    if i == len(data) - 1:
        y_down = 10
    else:
        y_down = data[i+1][j]
    if j == 0:
        x_left = 10
    else:
        x_left = data[i][j-1]
    if j == len(row)-1:
        x_right = 10
    else:
        x_right = data[i][j+1]

    return y_up, y_down, x_left, x_right

# data = read("day9_testdata.txt")
data = read("day9_data.txt")

low_points = []

for i, row in enumerate(data):
    for j, char in enumerate(row):
        y_up, y_down, x_left, x_right = find_neighbours(data, i, j)

        if char < y_up and char < y_down and char < x_left \
            and char < x_right:
            low_points.append((char, (i,j)))
        
print("Part 1: Sum of risk levels of the low points is", sum(x for x,_ in low_points)+len(low_points))

# ------------------- part 2 ---------------------

basins = [0]
visited = [[0]*len(data[0]) for _ in data]
count = 0

for low in low_points:
    y, x = low[1]
    def find(data, y, x):
        if data[y][x] == 9:
            return
        elif visited[y][x]:
            return
        else:
            visited[y][x] = 1
        if y > 0:
            find(data, y-1, x)
        if y < len(data)-1:
            find(data, y+1, x)       
        if x > 0:
            find(data, y, x-1)
        if x < len(data[0])-1:
            find(data, y, x+1)
        else:
            return
    
    find(data, y, x)

    basins.append(sum([sum(c for c in row) for row in visited]) - sum(basins))

result = sorted(basins, reverse=True)

print("Part 2: three largest basins multiplied together is", result[0]*result[1]*result[2])








