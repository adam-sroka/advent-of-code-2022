INPUT_PATH = "inputs/input_10.txt"
SIGNAL_CHECKS = [20, 60, 100, 140, 180, 220]

from utils import utils


def read_program(input_path: str = INPUT_PATH):
    with open(input_path) as input_data:
        return input_data.read().splitlines()


def find_register_values(program: list):
    register_values = [1]
    for line in program:
        split_line = line.split()
        register_values.append(register_values[-1])
        if split_line[0] == "addx":  # pass if noop, as last value gets copied anyway
            register_values.append(register_values[-1] + int(split_line[1]))
    return register_values


def sum_signal_strengths(register_values: list, signal_checks: list = SIGNAL_CHECKS):
    return sum([register_values[i - 1] * i for i in signal_checks])  # i-th check at index i-1


def draw_crt(register_values: list) -> str:
    display = ""
    crt_width = 40
    for cycle, value in enumerate(register_values):
        if cycle % crt_width == 0:
            display += "\n"
        if cycle % crt_width in [value, value - 1, value + 1]:
            display += "#"
        else:
            display += "."
    return display[:-2]  # last two character extra


def main():
    program = read_program()
    register_values = find_register_values(program)
    display = draw_crt(register_values)
    signal_strengths_sum = sum_signal_strengths(register_values)
    utils.write_answers_to_file(signal_strengths_sum, display, file_name="answer_10.txt")
    print(signal_strengths_sum, display)


if __name__ == "__main__":
    main()
