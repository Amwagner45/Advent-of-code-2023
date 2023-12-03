def solution():
    schematic = []
    with open("./Puzzle 3/puzzle_3_test.txt", "r") as file:
        for line in file:
            temp_chars = []
            for char in line:
                if char == "\n":
                    pass
                else:
                    temp_chars.append(char)
            print(line)
            schematic.append(temp_chars)
    return schematic


def spacer():
    print("#" * 20)


df = solution()
print(df)
spacer()
print(df[1][3])

valid_numbers_loc = []

for idy, line in enumerate(df):
    for idx, char in enumerate(line):
        number_start = -1
        number_end = -1

        ## If number not yet started
        if number_start == -1 and str.isnumeric(char):
            number_start = idx
            while str.isnumeric(line[idx + 1]):
                number_end = idx + 1

        valid_numbers_loc.append([number_start, number_end])

    print(line)
print(valid_numbers_loc)


## Need a data structure that makes sense to check values in a 1x1 grid around each complete number
## Thinking it should be a vector array so I can check if squares around are a wildcard

## Need to find beginning and end of number then search around them
## Beginning of number is first digit at index 0 or first digit with non-digit before it

## Need to account for edge cases in the corners of the array
