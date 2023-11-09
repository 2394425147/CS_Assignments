import random

def game_loop() -> (bool, int):
    guess_count = 0
    number_to_guess = random.randint(1, 100)
    while True:
        user_guess = int(input("请猜: "))
        is_correct = user_guess == number_to_guess

        if is_correct:
            return (True, number_to_guess)

        if guess_count == 4:
            return (False, number_to_guess)

        if user_guess > number_to_guess:
            print("大了")
        else:
            print("小了")

        guess_count += 1
    pass

while True:
    has_won, number = game_loop()
    should_continue = input(("猜对了，继续游戏" if has_won else f"游戏失败，答案是{number}，要继承游戏吗") + "? (YES/NO)").upper() == "YES"
    if not should_continue:
        break
