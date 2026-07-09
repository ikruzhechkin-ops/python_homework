'''Задача 5. Недоделка
Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители. У предыдущего программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них. Однако программист, на место которого вы пришли, перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта.

Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит, победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор, пока он не угадает загаданное.

Что нужно сделать
Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».'''

from random import randint

def rock_paper_scissors():
    wins = 0
    while wins != 1:
        enemy_uses = randint(1, 3)
        player_uses = int(input("Камень - 1, Ножницы - 2, Бумага - 3: "))
        if (enemy_uses == 1 and player_uses == 2) or (enemy_uses == 2 and player_uses == 3) or (enemy_uses == 3 and player_uses == 1):
            print("Поражение!")
            wins += 1
        elif (enemy_uses == 2 and player_uses == 1) or (enemy_uses == 3 and player_uses == 2) or (enemy_uses == 1 and player_uses == 3):
            print("Победа!")
            wins += 1
        else:
            print("Ничья!")

def guess_the_number():
    guessed_number = randint(1, 10)
    number = 0
    while number != guessed_number:
        number = int(input("Угадайте число от 1 до 10: "))
    print("Вы угадали!")

def main_menu(game):
    if game == 1:
        rock_paper_scissors()
    else:
        guess_the_number()

main_menu(int(input("Во что вы хотите поиграть: 1 - камень, ножницы, бумага; 2 - угадай число: ")))