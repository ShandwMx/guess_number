from random import randint

number = randint(1, 2)
print("Угадай число от 1 до 2")
while True:
    guess = int(input("Ваше число:"))
    if guess == number:
        print(f"Поздравляю, это число было {number}")
        break
    else:
        print("Неудача( Попробуй ещё раз!")
