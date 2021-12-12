import time

# ------------------------------------------------------------------
# the idea here is to take the initial positions of the crabs and 
# calculate how much fuel is consumed if all the crabs left/right of 
# a certain point moved to that point. then we find the smallest fuel
# consumption by finding the point where the sum of left and right 
# is the lowest.
# ------------------------------------------------------------------

def read():
    with open("day7_data.txt", "r") as file:
        for row in file:
            row = row.replace("\n", "")
            if row == "":
                continue
            parts = row.split(",")
            data = [int(x) for x in parts]
    return data


# ------------------------------------------------------------------
# moving costs 1 fuel per 1 step
# ------------------------------------------------------------------    
def align_crabs_constant_consumption():
    data = read()
    length = max(data)+1

    # initial positions of the crabs
    init_pos = [0]*length
    for crab in data:
        init_pos[crab] += 1

    crabs_from_left = [0]*length
    crabs_left_cumul = [0]*length
    crabs_from_right = [0]*length
    crabs_right_cumul = [0]*length

    for i in range(1,length):
        neighbour_crabs = init_pos[i-1]
        crabs_from_afar = crabs_from_left[i-1]
        crabs_from_left[i] = neighbour_crabs + crabs_from_afar
        crabs_left_cumul[i] = crabs_left_cumul[i-1] + crabs_from_left[i]

    for i in range(length-2,-1,-1):
        neighbour_crabs = init_pos[i+1]
        crabs_from_afar = crabs_from_left[i+1]
        crabs_from_right[i] = neighbour_crabs + crabs_from_afar
        crabs_right_cumul[i] = crabs_right_cumul[i+1] + crabs_from_right[i]

    # all crabs move from one end of the line to the next,
    # the fuel consumption should be less than that
    least_fuel = length * len(data) 
    for i in range(length):
        fuel_to_move = crabs_left_cumul[i] + crabs_right_cumul[i]       
        if  fuel_to_move < least_fuel:
            least_fuel = fuel_to_move
            best_position = i

    print(
        f"The best position is {best_position} and it takes {least_fuel} fuel to get all the crabs there"
        )



# -----------------------------------------------------------------------------------------
# pt.2: here moving further costs increasingly more: 1 step = 1 fuel, 2 steps = 2 fuel etc
# -----------------------------------------------------------------------------------------

def fuel_consumed(steps: int):
    result = [0]*(steps+1)
    result[1] = 1

    for x in range(2,steps+1):
        result[x] = result[x-1] + x

    return result


def align_crabs_growing_consumption():
    data = read()
    length = max(data)+1

    # ----------time-----------
    t1 = time.time()
    # -------------------------

    # fuel consumed by crab at n steps
    fuel_list = fuel_consumed(length)

    # initial positions of the crabs
    init_pos = [0]*length
    for crab in data:
        init_pos[crab] += 1

    fuel_consumption_left = [0]*length
    fuel_consumption_right = [0]*length

    # lists fuel consumption at all possible positions
    def calculate_consumption():
        for i in range(1,length):
            neighbour_crabs = init_pos[i-1]
            for j in range(i,1,-1):
                crabs_with_steps[j] = crabs_with_steps[j-1]
            crabs_with_steps[1] = neighbour_crabs
            fuel_consumption = 0
            for s in crabs_with_steps.keys():
                fuel_consumption += fuel_list[s] * crabs_with_steps[s]
            if from_left:
                fuel_consumption_left[i] = fuel_consumption
            else:
                fuel_consumption_right[i] = fuel_consumption

    from_left = True
    crabs_with_steps = {1:0}

    # crabs moving from left
    calculate_consumption()

    from_left = False        
    init_pos = init_pos[::-1]
    crabs_with_steps = {1:0}

    # crabs moving from right
    calculate_consumption()

    fuel_consumption_right = fuel_consumption_right[::-1]

    least_fuel = fuel_list[length] * len(data)
    for i in range(length):
        fuel_to_move = fuel_consumption_left[i] + fuel_consumption_right[i]     
        if  fuel_to_move < least_fuel:
            least_fuel = fuel_to_move
            best_position = i

    print(
        f"The best position is {best_position} and it costs {least_fuel} fuel to get all the crabs there"
        )

    # ----------time---------------------
    t2 = time.time()
    print("run time for part 2:", t2-t1)
    # -----------------------------------


align_crabs_constant_consumption()
align_crabs_growing_consumption()