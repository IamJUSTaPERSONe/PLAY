#Hello World Yopt ot komandu BDSM - Black/Dungeon/System/Managment
import random
from DeadFate import*
def Vsadniki():
  VAwords = ["Война", "Смерть", "Чума", "Голод"] # - Массив действий -
  # - Описание игры -
  print("«Всадники Апокалипсиса»")
  print("Игра заключается в том, чтобы последовательность слов сохранялось,\nто есть: «Война-Смерть, Смерть-Чума, Чума-Голод, Голод-Война» и так по кругу.")
  print("Победа в том случае, если Вы напишите слово в той последовательности,\nкоторая будет перед словом Противника. Например: Противник - Чума, а Вы - Смерть.")
  print("В случае победы Противника, то наоборот. Например: Вы - Голод, а Противник - Чума.")
  print("Ничья также присутствует в этой игре. Например: Противник - Смерть, а Вы - Смерть.\nИли же когда последовательности у обоих разные: Противник - Война, а Вы - Чума.")
  print("Начнём же игру...")

  # - Описание игры -
  def Game(): # - Функция вызова игры -
    Score = 0
    bot = random.choice(VAwords)
    print(f"Cписок выбора: {VAwords}")
    player = str(input())
    while Score == 0: # - Цикл с проверкой условий -
      if bot == VAwords[1] and player == VAwords[0]:
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      elif bot == VAwords[2] and player == VAwords[1]:
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      elif bot == VAwords[3] and player == VAwords[2]:
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      elif bot == VAwords[0] and player == VAwords[3]:
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      else:
        Score = 2
        break
    while Score == 2: # - Цикл с проверкой условий -
      if bot == VAwords[0] and player == VAwords[1]:
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      elif bot == VAwords[1] and player == VAwords[2]:
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      elif bot == VAwords[2] and player == VAwords[3]:
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      elif bot == VAwords[3] and player == VAwords[0]:
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      else:
        Score = 3
        break
    if Score == 3: # - Проверка условий на ничью -
        print(f"Противник выбрал {bot}, а Вы {player}. Ничья.")
        Game()
    elif Score == 1: # - Проверка игрока на победу -
      print("Вы победили!")
    elif Score == -1: # - Проверка игрока на поражение -
      print("Вы проиграли...")
      Knight()
  Game()