INPUT_PATH = "./input.txt"


def find_packet_start_index(data: str, unique_char_num: int = 4) -> int:
    for i in range(len(data)):
        if len(set(data[i : i + unique_char_num])) == unique_char_num:
            return i + unique_char_num
    return -1


def find_message_start_index(data: str) -> int:
    return find_packet_start_index(data, unique_char_num=14)


def read_data(input_path: str = INPUT_PATH) -> str:
    with open(input_path, "r") as input_data:
        return input_data.readlines()[0]


def write_answers(answers: list, path: str = "./answer.txt") -> None:
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer))
            answer_data.write("\n")


def main():
    data = read_data()
    packet_start_index = find_packet_start_index(data)
    message_start_index = find_message_start_index(data)
    write_answers([packet_start_index, message_start_index])
    print(packet_start_index, message_start_index)


if __name__ == "__main__":
    main()
