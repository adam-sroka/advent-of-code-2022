INPUT_PATH = "inputs/input_6.txt"

from utils import utils


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


def main():
    data = read_data()
    packet_start_index = find_packet_start_index(data)
    message_start_index = find_message_start_index(data)
    utils.write_answers_to_file(packet_start_index, message_start_index, file_name="answer_6.txt")
    print(packet_start_index, message_start_index)


if __name__ == "__main__":
    main()
