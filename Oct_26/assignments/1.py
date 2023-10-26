import random

roundsPlayed = 0
numberToGuess = random.randint(0, 1000)
guessed = False

while not guessed:
    roundsPlayed += 1
    guess = int(input("请输入一个整数: "))
    if guess > numberToGuess:
        print("大了")
    elif guess < numberToGuess:
        print("小了")
    else:
        guessed = True

print(f"经过{roundsPlayed}次回答，答对了")

