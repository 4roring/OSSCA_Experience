from random import randint

MAX_INPUT_COUNT = 3


def check_num(input_num, answer) -> bool:
    if input_num == answer:
        print("정답")
        return True

    failed_message = "다운" if input_num > answer else "업"
    print(failed_message)

    return False


def up_down():
    answer = randint(1, 20)
    print(answer)

    for _ in range(MAX_INPUT_COUNT):
        input_num = int(input())
        if check_num(input_num, answer):
            return

    print("실패")


if __name__ == "__main__":
    up_down()
