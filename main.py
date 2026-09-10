import random


def show_welcome():
    print("=" * 40)
    print("       ИГРА «УГАДАЙ ЧИСЛО»")
    print("=" * 40)
    print("Компьютер загадывает число — вы отгадываете.")
    print("Подсказки: «больше» — нужно число побольше,")
    print("«меньше» — поменьше. Удачи!")
    print("=" * 40)


def get_number(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.lstrip("-").isdigit():
            return int(raw)
        print("Пожалуйста, введите целое число.")


def pick_secret(low, high):
    return random.randint(low, high)


def play_one_round(low, high, max_tries):
    secret = pick_secret(low, high)
    print(f"\nЯ загадала число от {low} до {high}.")
    print(f"Попыток осталось: {max_tries}\n")

    for attempt in range(1, max_tries + 1):
        guess = get_number(f"Попытка {attempt}: ")

        if guess == secret:
            print(f"\nВерно! Число было {secret}.")
            print(f"Вы угадали за {attempt} попыток.")
            return attempt

        direction = "меньше" if guess > secret else "больше"
        remaining = max_tries - attempt
        hint = f"Загаданное число {direction}."

        if remaining > 0:
            print(f"{hint} Осталось попыток: {remaining}\n")
        else:
            print(hint)

    print(f"\nПопытки закончились. Загаданное число — {secret}.")
    return -1


def ask_to_repeat():
    while True:
        answer = input("\nСыграем ещё? (да / нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Введите «да» или «нет».")


def main():
    show_welcome()

    low, high = 1, 100
    max_tries = 12
    wins = 0
    losses = 0

    keep_playing = True
    while keep_playing:
        result = play_one_round(low, high, max_tries)
        if result == -1:
            losses += 1
        else:
            wins += 1
        print(f"\nСчёт — побед: {wins}, поражений: {losses}")
        keep_playing = ask_to_repeat()

    print("\nСпасибо за игру! До встречи.")


if __name__ == "__main__":
    main()

