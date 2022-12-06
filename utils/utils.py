from typing import Union


def write_answers_to_file(
    *answers: Union[str, int, float], file_name: str = "answer.txt", dir_path: str = "./answers"
) -> None:
    path = dir_path + "/" + file_name
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer) + "\n")
