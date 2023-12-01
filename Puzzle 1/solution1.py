def check_numbers(puzzle_string: str):
    new_puzzle_string = []

    for i, char in enumerate(puzzle_string):
        if char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            new_puzzle_string.append(char)
        for idx, num in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if puzzle_string[i:].startswith(num):
                new_puzzle_string.append(str(idx + 1))
    print(new_puzzle_string[0], new_puzzle_string[-1])
    return int(new_puzzle_string[0] + new_puzzle_string[-1])


def solution():
    final_sum = 0
    with open("./Puzzle 1/puzzle_1_input.txt", "r") as file:
        for line in file:
            calibration = check_numbers(line)
            final_sum = final_sum + calibration
    return final_sum


print(solution())
