HANDS_CIPHER = dict(A="r", B="p", C="s", X="r", Y="p", Z="s")
OUTCOME_CIPHER = dict(X="loss", Y="draw", Z="win")
HAND_SCORES = dict(r=1, p=2, s=3)
ROUND_SCORES = dict(loss=0, draw=3, win=6)


def decrypt_hand(encrypted_hand: str) -> str:
    return HANDS_CIPHER[encrypted_hand]


def decrypt_outcome(encrypted_outcome: str) -> str:
    return OUTCOME_CIPHER[encrypted_outcome]


def get_hand_score(hand: str) -> int:
    return HAND_SCORES[hand]


def get_outcome_score(outcome: str) -> int:
    return ROUND_SCORES[outcome]


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


def find_correct_hand(opposing_hand: str, round_outcome: str) -> str:
    if round_outcome == "draw":
        return opposing_hand
    if round_outcome == "win" and opposing_hand == "r":
        return "p"
    if round_outcome == "win" and opposing_hand == "p":
        return "s"
    if round_outcome == "win" and opposing_hand == "s":
        return "r"
    if round_outcome == "loss" and opposing_hand == "r":
        return "s"
    if round_outcome == "loss" and opposing_hand == "p":
        return "r"
    if round_outcome == "loss" and opposing_hand == "s":
        return "p"


def get_round_score(hand: str, opposing_hand: str) -> int:
    score = get_hand_score(hand)
    score += get_outcome_score(get_round_outcome(hand, opposing_hand))
    return score


def parse_encrypted_hands(line: str) -> tuple:
    encrypted_opposing_hand = line[0]
    encrypted_hand = line[2]
    return (encrypted_hand, encrypted_opposing_hand)


def parse_encrypted_hands_and_outcomes(line: str) -> tuple:
    encrypted_opposing_hand = line[0]
    encrypted_outcome = line[2]
    return (encrypted_opposing_hand, encrypted_outcome)


def decrypt_rounds(input_path="./input.txt") -> list:
    with open(input_path, "r") as input_data:
        rounds = list()
        for line in input_data:
            encrypted_hands = parse_encrypted_hands(line)
            rounds.append(
                # (hand, opposing_hand)
                (decrypt_hand(encrypted_hands[0]), (decrypt_hand(encrypted_hands[1])))
            )
    return rounds


def decrypt_opposing_hands_and_outcomes(input_path="./input.txt") -> list:
    with open(input_path, "r") as input_data:
        opposing_hands_and_outcomes = list()
        for line in input_data:
            opposing_hand_and_outcome = parse_encrypted_hands_and_outcomes(line)
            opposing_hands_and_outcomes.append(
                # (opposing_hand, outcome)
                (
                    decrypt_hand(opposing_hand_and_outcome[0]),
                    (decrypt_outcome(opposing_hand_and_outcome[1])),
                )
            )
    return opposing_hands_and_outcomes


def get_total_score(rounds: list) -> int:
    return sum([get_round_score(curr_round[0], curr_round[1]) for curr_round in rounds])


def get_correct_total_score(opposing_hands_and_outcomes: list) -> int:
    score = 0
    for opposing_hand_and_outcome in opposing_hands_and_outcomes:
        opposing_hand = opposing_hand_and_outcome[0]
        outcome = opposing_hand_and_outcome[1]
        hand = find_correct_hand(opposing_hand, outcome)
        score += get_outcome_score(outcome) + get_hand_score(hand)
    return score


def write_answers(answers: list, path="./answer.txt") -> None:
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer))
            answer_data.write("\n")


def main():
    rounds = decrypt_rounds()
    total_score = get_total_score(rounds)
    opposing_hands_and_outcomes = decrypt_opposing_hands_and_outcomes()
    correct_total_score = get_correct_total_score(opposing_hands_and_outcomes)
    print(total_score, correct_total_score)
    write_answers([total_score, correct_total_score])


if __name__ == "__main__":
    main()
