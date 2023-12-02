def solution(verbose=False):
    with open("./Puzzle 2/puzzle_2_input.txt", "r") as file:
        final_count = 0
        for line in file:
            game = line.split(":")[0]
            game_number = int(game.split(" ")[1])
            result_sets = line.split(":")[1].split(";")
            game_possible = True
            for set_number, result_set in enumerate(result_sets):
                if verbose:
                    print(game, ": set", set_number + 1, ":", result_set.strip())

                for attempt in result_set.strip().split(","):
                    count = int(attempt.strip().split(" ")[0])
                    color = attempt.strip().split(" ")[1]

                    if (
                        (color == "red" and count > 12)
                        or (color == "green" and count > 13)
                        or (color == "blue" and count > 14)
                    ):
                        game_possible = False
                    else:
                        pass

                    if verbose:
                        print(count, color, game_possible)

            if game_possible:
                final_count += game_number

        return final_count


print(solution())
