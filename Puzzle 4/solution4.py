def clean_list(list):
    valid_nums = []
    for i in list:
        if i == "":
            continue
        elif i.endswith("\n"):
            valid_nums.append(i.split("\n")[0])
        else:
            valid_nums.append(i)
    return valid_nums


def solution1():
    answer = 0

    with open("./Puzzle 4/puzzle_4_input.txt", "r") as file:
        for line in file:
            match = False
            base = 2
            exponent = -1

            card = line.split(":")

            scratch_win = card[1].split("|")[0]
            win_nums = clean_list(scratch_win.split(" "))

            scratch_card = card[1].split("|")[1]
            nums = clean_list(scratch_card.split(" "))

            for i in win_nums:
                for j in nums:
                    if i == j:
                        match = True
                        exponent += 1

            if match == True:
                value = base**exponent
                answer = answer + value

            print(win_nums, nums)

    print(answer)


solution1()
