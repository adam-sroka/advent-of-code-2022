
def get_all_elves_cal():
    with open("./input.txt", "r") as input_data:
        all_elves_calories = list()
        elf_calories = list()
        for line in input_data:
            if line != "\n":
                elf_calories.append(int(line))
            else:
                all_elves_calories.append(elf_calories.copy())
                elf_calories.clear()
    return all_elves_calories


def find_max_total_cal(all_elves_calories):
    return max([sum(elf_calories) for elf_calories in all_elves_calories])


def write_solution(solution):
    with open("./solution.txt", "w") as solution_data:
        solution_data.write(str(solution))
        solution_data.write("\n")


if __name__ == "__main__":
    all_elves_calories = get_all_elves_cal()
    max_total_cal = find_max_total_cal(all_elves_calories)
    write_solution(max_total_cal)
    print(max_total_cal)
