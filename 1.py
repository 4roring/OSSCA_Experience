QUIZ_MAP = {"취존": "취향존중", "솔까말": "솔직히까놓고말해서", "케바케": "케이스바이케이스"}


def quiz():
    correct_count = 0
    for question, answer in QUIZ_MAP.items():
        print(f"{question}은 어떤 문장의 줄임말인가요?")
        input_answer = input()
        input_answer.replace(" ", "")
        if answer == input_answer:
            correct_count += 1
        else:
            print(input_answer)

    print(f"{len(QUIZ_MAP)}개 퀴즈 중 {correct_count}개 정답")


if __name__ == "__main__":
    quiz()
