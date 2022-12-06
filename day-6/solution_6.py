INPUT_PATH = "./input.txt"


def find_packet_start_index(data: str) -> int:
    for i in range(len(data)):
        if len(set(data[i : i + 4])) == 4:
            return i + 4
    return -1


def read_data(input_path=INPUT_PATH):
    with open(input_path, "r") as input_data:
        return input_data.readlines()[0]


def main():
    data = read_data()
    start_index = find_packet_start_index(data)
    print(start_index)


if __name__ == "__main__":
    main()
