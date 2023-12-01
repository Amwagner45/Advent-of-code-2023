puzzle_string = "hcpjssql4kjhbcqzkvr2fivebpllzqbkhg"

min_num = None
max_num = None


def check_numbers(puzzle_string, min_num=None, max_num=None):
    for char in puzzle_string:
        if char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            max_num = char
        if char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            if min_num == None:
                min_num = char
            else:
                pass
    return int(min_num + max_num)


def solution():
    final_sum = 0
    with open("./Puzzle 1/puzzle_1_input.txt", "r") as file:
        for line in file:
            calibration = check_numbers(line)
            final_sum = final_sum + calibration
    return final_sum


print(solution())
