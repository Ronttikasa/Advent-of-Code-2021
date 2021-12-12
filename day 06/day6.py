import time

def read():
    with open("day6_data.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            parts = row.split(",")
            data = [int(x) for x in parts]
    return data

# iterates lists, works for days < 100
def pass_day_naive(fishes: list):
    aged_fishies = []
    new_fishesss = []

    for fish in fishes:
        if fish == 0:
            aged_fishies.append(6)
            new_fishesss.append(8)
        else:
            aged_fishies.append(fish-1)

    return aged_fishies + new_fishesss

# dictionary, works for longer time periods as well
def pass_days_dict(fishes_list: list, days: int):
    # initialize dictionary
    fishies = {}
    for day in range(10):
        fishies[day] = 0

    for fish in fishes_list:
        fishies[fish] += 1

    # this happens in one day
    def pass_one_day():
        for timer in fishies:
            fish_amount = fishies[timer]
            if timer == 0:
                fishies[7] += fish_amount # these fish go to the start of the cycle
                fishies[9] += fish_amount # baby fish do doo do do do do
                fishies[0] = 0
            else:
                fishies[timer-1] = fish_amount
                fishies[timer] = 0
        
    for _ in range(days):
        pass_one_day()    

    
    fish_total = sum(fishies.values())
    print(fish_total, "fish in total")


def main():
    t1 = time.time()
    data = read()
    pass_days_dict(data,256)
    t2 = time.time()

    print("time used", t2-t1, "s")


def main_naive():
    t1 = time.time()
    data = read()

    # naive implementation, works when days < 100
    for _ in range(80):
        data = pass_day_naive(data)
        # print(data)

    print(len(data))
    t2 = time.time()
    print("time used (naive)", t2-t1, "s")

main()
