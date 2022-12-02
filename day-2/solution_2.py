HANDS_CIPHER = dict(A="r", B="p", C="s", X="r", Y="p", Z="s")
HAND_SCORES = dict(r=1, p=2, s=3)
ROUND_SCORES = dict(loss=0, draw=3, win=6)


def decrypt_hand(encrypted_hand: str) -> str:
    return HANDS_CIPHER[encrypted_hand]


def get_hand_score(hand: str) -> int:
    return HAND_SCORES[hand]


def get_round_outcome(hand: str, opposing_hand: str) -> str:
    if hand == opposing_hand:
        return "draw"
    if hand == "r" and opposing_hand == "s":
        return "win"
    if hand == "r" and opposing_hand == "p":
        return "loss"
    if hand == "p" and opposing_hand == "r":
        return "win"
    if hand == "p" and opposing_hand == "s":
        return "loss"
    if hand == "s" and opposing_hand == "p":
        return "win"
    if hand == "s" and opposing_hand == "r":
        return "loss"


def get_round_score(hand: str, opposing_hand: str) -> int:
    score = get_hand_score(hand)
    score += ROUND_SCORES[get_round_outcome(hand, opposing_hand)]
    return score


def parse_encrypted_hands(line: str) -> tuple:
    encrypted_opposing_hand = line[0]
    encrypted_hand = line[2]
    return (encrypted_hand, encrypted_opposing_hand)


def decrypt_rounds(input_path="./input.txt") -> list:
    with open(input_path, "r") as input_data:
        rounds = list()
        for line in input_data:
            encrypted_hands = parse_encrypted_hands(line)
            rounds.append(
                (decrypt_hand(encrypted_hands[0]), (decrypt_hand(encrypted_hands[1])))
            )
    return rounds


def get_total_score(rounds: list) -> int:
    return sum([get_round_score(curr_round[0], curr_round[1]) for curr_round in rounds])


def write_answers(answers: list, path="./answer.txt") -> None:
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer))
            answer_data.write("\n")


def main():
    rounds = decrypt_rounds()
    total_score = get_total_score(rounds)
    print(total_score)
    write_answers([total_score])


if __name__ == "__main__":
    main()
