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


def sum_each_elfs_calories(all_elves_calories):
    return [sum(elf_calories) for elf_calories in all_elves_calories]


def find_max_total_cal(all_elves_calories):
    return max(sum_each_elfs_calories(all_elves_calories))


def find_top_three_max_total_cal(all_elves_calories):
    sorted_total_cals = sorted(sum_each_elfs_calories(all_elves_calories), reverse=True)
    return sum(sorted_total_cals[:3])


def write_answers(answers, path="./answer.txt"):
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer))
            answer_data.write("\n")


def main():
    all_elves_calories = get_all_elves_cal()
    max_total_cal = find_max_total_cal(all_elves_calories)
    top_three_max_total_cal = find_top_three_max_total_cal(all_elves_calories)
    write_answers((max_total_cal, top_three_max_total_cal))
    print(max_total_cal, top_three_max_total_cal)

if __name__ == "__main__":
    main()
