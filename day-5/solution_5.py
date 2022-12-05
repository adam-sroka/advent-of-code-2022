STACK_WIDTH = 3
STACK_GAP = 1
CRATE_START = "["
INPUT_PATH = "./input.txt"
NUM_BOXES_INDEX = 1
TAKING_STACK_INDEX = 3
RECEIVING_STACK_INDEX = 5


def get_stack_number(crate_start_pos: int) -> int:
    return crate_start_pos // (STACK_WIDTH + STACK_GAP) + 1


def parse_stacks_row(line: str) -> dict:
    stacks_elements = dict()
    for pos, element in enumerate(line):
        if element == CRATE_START:
            stacks_elements[get_stack_number(pos)] = line[pos + 1]
    return stacks_elements


def read_stacks(input_path=INPUT_PATH) -> dict:
    stacks = dict()
    with open(input_path, "r") as input_data:
        for line in input_data:
            if line == "\n":
                return stacks
            stacks_row = parse_stacks_row(line)
            for stack_id, element in stacks_row.items():
                if stack_id in stacks:
                    # insert is O(n), could just append and then work with reversed stacks
                    stacks[stack_id].insert(0, element)
                else:
                    stacks[stack_id] = [element]


def parse_procedure_step(line: str) -> tuple:
    split_line = line.split()
    return int(split_line[NUM_BOXES_INDEX]), int(split_line[TAKING_STACK_INDEX]), int(split_line[RECEIVING_STACK_INDEX])


def read_procedure(input_path=INPUT_PATH) -> list:
    procedure = list()
    with open(input_path, "r") as input_data:
        for line in input_data:
            if line[:4] == "move":
                procedure.append(parse_procedure_step(line))
    return procedure


def execute_procedure(stacks, procedure):
    for step in procedure:
        num_boxes = step[0]
        taking_stack_id = step[1]
        receiving_stack_id = step[2]
        for _ in range(num_boxes):
            stacks[receiving_stack_id].append(stacks[taking_stack_id].pop())
    return stacks


def get_top_crates_names(stacks):
    top_crates_names = ""
    for i in range(len(stacks.keys())):
        top_crates_names += stacks[i + 1][-1]
    return top_crates_names


def write_answers(answers: list, path="./answer.txt") -> None:
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer))
            answer_data.write("\n")


def main():
    stacks = read_stacks()
    procedure = read_procedure()
    stacks = execute_procedure(stacks, procedure)
    top_crates_names = get_top_crates_names(stacks)
    write_answers([top_crates_names])
    print(top_crates_names)


if __name__ == "__main__":
    main()
