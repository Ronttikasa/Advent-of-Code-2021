def read():
    with open("day4_data.txt", "r") as file: 
    # with open("day4_testdata.txt", "r") as file:
        data = []
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            parts = row.split(" ")
            parts = [part for part in parts if part != ""]
            data.append(parts)
    data[0] = data[0][0].split(",")
    return data

# järjestellään data bingoruudukoiksi, ensimmäisenä alkiona arvottavat numerot
def make_bingo_boards():
    data = read()
    result = [data[0]]
    data = data[1:]
    for i, line in enumerate(data):
        if i % 5 == 0:
            board = [line]
            continue
        board.append(line)
        if i % 5 == 4:
            result.append(board)

    return result

# merkitään numero osumaksi
def mark(number: str, row: list):
    for i, elem in enumerate(row):
        if elem == number:
            row[i] += "*"
            break

# tarkistetaan bingot
def check_bingo(board: list):
    # vaakasuuntaiset
    for row in board:
        for elem in row:
            if not "*" in elem:
                break
        else:
            return True
    # pystysuuntaiset
    for i in range(len(board[0])):
        for j in range(len(board)):
            if not "*" in board[j][i]:
                break
        else:
            return True
    return False

# pelataan bingoa, palauttaa voittavan laudan
def play(boards):
    numbers = boards[0]

    for number in numbers:
        for board in boards[1:]:
            for row in board:
                if number in row:
                    mark(number, row)
                    break
        for board in boards[1:]:
            board_wins = check_bingo(board)
            if board_wins:
                return [board, number] 

# pelataan bingoa, palauttaa viimeisenä voittavan laudan
def play_last_to_win(boards):
    numbers = boards[0]
    winning_boards = []

    for number in numbers:
        for board in boards[1:]:
            for row in board:
                if number in row:
                    mark(number, row)
                    break
        for i, board in enumerate(boards[1:]):
            if not i in winning_boards:
                board_wins = check_bingo(board)
                if board_wins:
                    if len(winning_boards) == len(boards[1:]) - 1:
                        return [board, number]
                    winning_boards.append(i)

# lasketaan voittajalaudan pisteet
def score(winning_board):
    board = winning_board[0]
    last_number = int(winning_board[1])

    unmarked = []
    for row in board:
        for elem in row:
            if not "*" in elem:
                unmarked.append(int(elem))
    
    sum_unmarked = sum(unmarked)

    score = sum_unmarked * last_number

    return score

boards = make_bingo_boards()
board = play_last_to_win(boards)
print(score(board))
