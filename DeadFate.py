#Hello World Yopt ot komandu BDSM - Black/Dungeon/System/Managment
import random
import time
from random import randint

def printdelay(text, delay=0.08):  # -Плавное появление текста-
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print("")

Masstr = ("━━━", "━━━━", "┣━━━━┫", "┗━━━━┛", "┳", "┻", "╋", "┗━",
          "━┛", "┣━", "━┫", "┏━", "━┓", "━", "══", "  ", "┃", "║", " ")
# ----------0------1---------2----------3------4----5----6-----7----
# ---------8------9----10----11----12----13---14----15----16---17---18
# номера элементов в массиве конструкторе
TimeDead = time.perf_counter()

masssmert = ["Ваши глаза залились кровью вскоре вы захлебнулись ею,", "Ваши кости прорвали плоть,",
"Вы перестали видить и слышать но начав кричать на вас сбежались крысы, съев вас заживо"]
pers = [" ◯  ", "    "]

semak = 0
godOfDead = 4
MASSODETOSTI = [0, 0]
massloot = {"меч": 0, "щит": 0, "зелье лечения": 0, "большое зелье лечения": 0, "крысиное мясо": 0, "ключ от выхода": 0, "ключ от черной двери": 0, "ключ от красной двери": 0}
masssearch = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ZackLive = 1
OctopusLive = 1
Knightlive1 = 1
Knightlive2 = 1
TimeNamePerson = []
# ----- ---------------------------------------------- Битва ------------------------------------------------
emeni = [] # враг
Mas = [100, 10, 2]# -Hp, Dps, Defence-
Mas1 = []  # -Бафф перса-
masspers = []
ChoiseR = ""
smenper = 1
# ----- двери
DoorEx = 14
# ----- 15 = открыта
DoorBs = 14
# ----- 15 = открыта
DoorZag = 17
# ----- 18 = открыта

image = open("image.txt", "r", encoding="utf8")
young = 0
sl = image.readlines()
massimage = [[], [], [], [], [], [], []]
for rich in sl:
    if rich != '//\n' and rich != '//':
        massimage[young].append(rich)
    elif rich == '//\n' or rich == '//':
        young += 1
image.close()
def vyvodimage(kelvin):
    for i in massimage[kelvin]:
        i = i.replace("\n", "")
        print(f"{i}")
    print("--------------------------------------------------------------------")
# Массив лута
lootkey = ["ключ от черной двери", "крысиное мясо"]
lootstartroom = ["меч", "щит", "зелье лечения", "тряпье"]
lootand = ["ключ от выхода"]
lootanroom = ["зелье лечения", "крысиное мясо", "большое зелье лечения", "большое зелье лечения", "кость", "старую тряпку", "сгоревший труп", "камень"]
lootzagadka = ["ключ от красной двери"]
grib = ""
#-----------------------------------------------------Диалоги и сообщения------------------------------------
def ZackDialog():
    global ChoiseR, ZackLive, godOfDead, TimeNamePerson
    print("За дверью были слышны чьи то возгласы, после того как я зашёл в комнату, оказалось, что крики исходили от пожилого человека, с виду - ему было уже за 80 лет.")
    print("Я решаюсь подойти к нему и спросить его.")
    print(f"{TimeNamePerson[0]} - Ты что тут делаешь, старик ?")
    print("Зак - Я пришёл за другом, он совсем недавно пропал, теперь ищу его везде.")
    print("Тут же я замечаю, что на полу лежит игрушка, когда я её взял, то вдруг заметил, что на ней есть надпись - |Зак|")
    print(f"{TimeNamePerson[0]} - Это случайно не он ?")
    print("Зак - Да! Это мой друг! Отдай же его живо!")
    print(f"{TimeNamePerson[0]} - А что будет, если не отдам ?")
    print("Зак - Ох зря ты сюда полез... У тебя теперь 2 варианта развития событий")
    print("Зак - Первый вариант, сразиться со мною.")
    print("Зак - Второй вариант, отгадать мои загадки.")
    print("Зак - Что ты выбираешь ?")
    while godOfDead != 0:
        ChoiseR = input("Сделайте выбор: -- Сразиться || Игру --\n")
        if ChoiseR == "Сразиться" or ChoiseR == "сразиться":
            print(f"{TimeNamePerson[0]} - Сразить тебя будет не трудно...")
            Zack()
            printdelay("Убив старика, вы находите ключ")
            break
        elif ChoiseR == "Игру" or ChoiseR == "игру":
            print(f"{TimeNamePerson[0]} - Раз уж так, то давай сыграем в игру!")
            HeadAche()
            printdelay("После победы в игре, вы получили ключ от красной двери")
            break
        else:
            karmauma()
    massloot["ключ от красной двери"] += 1
    ZackLive = 0
    GameNa()

def KnightDialog1():
    global ChoiseR, godOfDead, Knightlive1, TimeNamePerson
    print("Приоткрыв дверь и пройдя дальше к центру комнаты, я увидел там силуэт человека, стоящего возле колонны, как будто охраняя что-то.")
    while godOfDead != 0:
        ChoiseR = input("Ваш выбор -- Атаковать || Подойти --\n")
        if ChoiseR == "Атаковать" or ChoiseR == "атаковать":
            print("\nСилуэтом в кромешной тьме оказался рыцарем, в схватке с ним будет сложно.\n")
            Knight()
        elif ChoiseR == "Подойти" or ChoiseR == "подойти":
            print("\nПодойдя к силуэту ближе, я увидел, что это стражник в стальных доспехах. Я заговорил с ним.\n")
            print(
                f"{TimeNamePerson[0]} - Здравствуй, страж!\nСтраж - Приветствую тебя, странник! Не часто здесь встретишь души, сбившиеся с пути.\n{TimeNamePerson[0]} - А я не думал встретить здесь стража, который не захочет меня убить.\n"
                f"Страж - В этом также мало смысла, как и в моём пребывании здесь. Ты и так уже мёртв, а порядок в здешних местах меня мало волнует.\n{TimeNamePerson[0]} - Может тогда скажешь, как отсюда выбраться?")
            print(
                "Страж - Нет, но я видел здесь одного безумца, говорившего загадками. Он меня утомил, но тебе может и помочь.\n"
                f"{TimeNamePerson[0]} - Спасибо, страж!\nСтраж - Постой, я уже потерял счёт времени-каждый день и каждая ночь здесь проходит абсолютно одинаково. Кто знает, сколько веков мне ещё суждено охранять это дьявольское место, могу я тебя попросить об услуге?\n{TimeNamePerson[0]} - О какой ?")
            print(
                "Страж - Сыграем в Блэкджек? Ощущение азарта заставляет меня чувствовать себя живым, да и ты с дороги отдохнёшь, приведёшь мысли в порядок.\n")
            while godOfDead != 0:
                ChoiseR = input("Сделайте выбор: Сыграть || Отказаться\n")
                if ChoiseR == "Сыграть" or ChoiseR == "сыграть":
                    print("\nПочему бы и нет ?\nСтраж - Партия будет интересной")
                    game.start()
                    break
                elif ChoiseR == "Отказаться" or ChoiseR == "отказаться":
                    print("\nСтраж - Тогда готовься к битве!")
                    Knight()
                    break
                else:
                    karmauma()
            break
        else:
            karmauma()
    Knightlive1 = 0
    GameNa()

# ----------------------------------------------------------------------Игра Всадники Апокалипсиса----------------------------------------------------------------------
def Vsadniki():
  VAwords = ["Война", "Смерть", "Чума", "Голод"] # - Массив действий -
  VAwords1 = ["война", "смерть", "чума", "голод"] # - Массив действий -
  # - Описание игры -
  print("«Всадники Апокалипсиса»")
  print("Игра заключается в том, чтобы последовательность слов сохранялось,\nто есть: «Война-Смерть, Смерть-Чума, Чума-Голод, Голод-Война» и так по кругу.")
  print("Победа в том случае, если Вы напишите слово в той последовательности,\nкоторая будет перед словом Противника. Например: Противник - Чума, а Вы - Смерть.")
  print("В случае победы Противника, то наоборот. Например: Вы - Голод, а Противник - Чума.")
  print("Ничья также присутствует в этой игре. Например: Противник - Смерть, а Вы - Смерть.\nИли же когда последовательности у обоих разные: Противник - Война, а Вы - Чума.")
  print("Начнём же игру...")

  def Game(): # - Функция вызова игры -
    Score = 0
    bot = random.choice(VAwords)
    print(f"Cписок выбора: {VAwords}")
    player = str(input())
    while Score == 0: # - Цикл с проверкой условий -
      if bot == VAwords[1] and (player == VAwords[0] or player == VAwords1[0]):
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      elif bot == VAwords[2] and (player == VAwords[1] or player == VAwords1[1]):
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      elif bot == VAwords[3] and (player == VAwords[2] or player == VAwords1[2]):
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      elif bot == VAwords[0] and (player == VAwords[3] or player == VAwords1[3]):
        print(f"Противник выбрал {bot}, а Вы {player}. Победа.")
        Score = 1
        break
      else:
        Score = 2
        break
    while Score == 2: # - Цикл с проверкой условий -
      if bot == VAwords[0] and (player == VAwords[1] or player == VAwords1[1]):
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      elif bot == VAwords[1] and (player == VAwords[2] or player == VAwords1[2]):
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      elif bot == VAwords[2] and (player == VAwords[3] or player == VAwords1[3]):
        print(f"Противник выбрал {bot}, а Вы {player}. Поражение.")
        Score = -1
        break
      elif bot == VAwords[3] and (player == VAwords[0] or player == VAwords1[0]):
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
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def KnightDialog2():
    global ChoiseR, godOfDead, Knightlive2, TimeNamePerson
    print("Зайдя в комнату, я услышал вдруг топот человека в доспехах в мою сторону. Хотелось уже убежать из этой комнаты, но дверь назад захлопнулась. ")
    while True:
        ChoiseR = input("Сделайте выбор: Атаковать || Подойти \n")
        if ChoiseR == "Атаковать" or ChoiseR == "атаковать":
            print("К оружию!")
            Knight()
            break
        elif ChoiseR == "Подойти" or ChoiseR == "подойти":
            print(f"{TimeNamePerson[0]} - Здравствуй рыцарь!")
            print(f"Рыцарь - И тебе не хворать.")
            print(f"Рыцарь - Какими судьбами тебя завело в это ужасное место ?")
            print(f"{TimeNamePerson[0]} - Это долгая история...")
            print(f"{TimeNamePerson[0]} - Лучше расскажи, как можно покинуть это чистилище ?")
            print(f"Рыцарь - Знал бы я ответ, то и тебе я его рассказал.")
            print(f"Рыцарь - Много лет я тут торчу, кажется, что тут выхода и вовсе нет.")
            print(f"Рыцарь - Но возможно есть тут один вариант, видел я неподалёку комнату с каким то огромным монстром-осьминогом.")
            print(f"Рыцарь - Может и он ответ на этот вопрос знает, только вот к нему все заблудшие души в этом чистилище боятся подойти, он вроде как повелитель этого места.")
            print(f"{TimeNamePerson[0]} - Спасибо рыцарь, попробую аккуратнее ходить по тем местам.")
            print(f"Рыцарь - Подожди... У меня для тебя есть одна игра, я думаю - тебе она понравится, не желаешь сыграть ?")
            while True:
                ChoiseR = input("Сделайте выбор: Сыграть || Отказаться \n")
                if ChoiseR == "Сыграть" or ChoiseR == "сыграть":
                    print(f"{TimeNamePerson[0]} - Считай, что я уже выиграл!")
                    Vsadniki()
                    break
                elif ChoiseR == "Отказаться" or ChoiseR == "отказаться":
                    print("Рыцарь - Очень плохо, что ты отказался. Я думаю, мне стоит сразиться с тобою, может так я себя развеселю.")
                    Knight()
                    break
                else:
                    karmauma()
            break
        else:
            karmauma()
    Knightlive2 = 0
    GameNa()

def OctopusLiveDialog():
    global masssmert, OctopusLive
    Octopus()
    OctopusLive = 0
    GameNa()

def Deadofgod():
    global masssmert, godOfDead
    dead = str(random.choices(masssmert))
    chars_to_remove = ["[", "]", "'"]
    for char in chars_to_remove:
        dead = dead.replace(char, "")
    TimeDead = int(time.perf_counter())
    print(f"{dead} мучения продлились {TimeDead} секунд")
    godOfDead = 0
    hod()
#--------------------------------------------------Информация о существах------------------------------------

def Rat():

  global emeni
  emeni = [" крысой", 50, [3, 6]]
  Versus()
  emeni = []
  massloot["крысиное мясо"] += 1

def Goblin():
  global emeni
  emeni = [" гоблином", 40, [8, 12]]
  Versus()
  emeni = []
  massloot["зелье лечения"] += 1

def Knight():
  global emeni
  emeni = ["о стражом", 180, [10, 15]]
  Versus()
  emeni = []
  massloot["большое зелье лечения"] += 1

def Zack():
  global emeni
  emeni = [" Заком", 100, [2, 3, 4, 5, 6, 7, 8, 9, 90]]
  Versus()
  emeni = []

def Octopus():
    global emeni
    emeni = [" Монстром-Осьминогом", 270, [12, 15, 18, 21]]
    Versus()
    emeni = []

def Versus():
    global emeni, Mas, Mas1
    Enemie = True
    Characters = True
    defend_buff = 0
    defend_deactivate = 0
    print("Вы вошли в бой с" + emeni[0])
    while Enemie == True and Characters == True:
        if emeni[1] <= 0 and Mas[0] <= 0:
            Enemie = False
            Characters = False
            break
        elif emeni[1] <= 0:
            Enemie = False
            break
        elif Mas[0] <= 0:
            Characters = False
            break
        print("Ваши действия:\n")
        print("Атака")
        print("Применить предмет")
        print("Защититься\n")

        a = input()
        if a == "Атака" or a == "атака":
            print("")
            print("Вы наносите увечья врагу...")
            if defend_buff == 1 and defend_deactivate == 0:
                eff = randint(15, 40)
                Mas1.append(Mas[1])
                Mas1[0] = (Mas1[0] / 100) * eff
                Mas[1] = Mas[1] + round(Mas1[0])
                if defend_buff == 1:
                    Mas1[0] = round(Mas1[0])
                    print(f"Вы получили бафф к урону ({Mas1[0]}) за действие защиты!")
                print(Mas1[0])
                print(Mas[1])
                emeni[1] = emeni[1] - Mas[1]
                defend_deactivate = 1
                defend_buff = 0
            else:
                emeni[1] = emeni[1] - Mas[1]
            Mas[0] = Mas[0] - random.choice(emeni[2])
            if Mas[0] <= 0:
                Mas[0] = 0
            if emeni[1] <= 0:
                emeni[1] = 0
            print("Ваше здоровье: " + str(Mas[0]), "Hp")
            print("Здоровье противника: " + str(emeni[1]), "Hp")
            print("")
        if a == "Защититься" or a == "защититься":
            print("")
            print("Вы защищаетесь...")
            print("")
            if Mas[2] >= random.choice(emeni[2]):
                print("Вы защитились от урона.")
                print("Ваше здоровье: " + str(Mas[0]), "Hp")
                print("Здоровье противника: " + str(emeni[1]), "Hp")
                print("")
                defend_buff = 1
            elif Mas[2] >= 1:
                print("В попытках защититься, вы поглотили часть урона.")
                Mas[0] = (Mas[0] + Mas[2]) - random.choice(emeni[2])
                defend_buff = 1
                if Mas[0] <= 0:
                    Mas[0] = 0
                print("Ваше здоровье: " + str(Mas[0]), "Hp")
                print("Здоровье противника: " + str(emeni[1]), "Hp")
                print("")
            else:
                print("Вам нечем было защищаться, вы получили полный урон.")
                Mas[0] = Mas[0] - random.choice(emeni[2])
                defend_buff = 1
                if Mas[0] <= 0:
                    Mas[0] = 0
                print("Ваше здоровье: " + str(Mas[0]), "Hp")
                print("Здоровье противника: " + str(emeni[1]), "Hp")
                print("")
        if a == "Применить предмет" or a == "применить предмет":
            Inventary()
    if (Enemie == False or Enemie == True) and Characters == False:
        Deadofgod()
    elif Enemie == False and Characters == True:
        print("Вы победили противника!")

# смена местоположение игрока
def smena():
    masspers.clear()
    for i in range(0, 17):
        if i == smenper:
            masspers.append(pers[0])
        else:
            masspers.append(pers[1])
smena()

# Отображение карты


def MapVision():
    level0 = Masstr[11] + Masstr[0] + Masstr[4] + Masstr[13] + Masstr[DoorEx] + Masstr[13] + Masstr[4] + \
             Masstr[1] + Masstr[4] + Masstr[0] + Masstr[12]
    level1 = Masstr[16] + masspers[0] + Masstr[16] + masspers[1] + Masstr[18] + masspers[2] + Masstr[16] + \
             masspers[3] + Masstr[16]
    level2 = Masstr[9] + Masstr[15] + Masstr[13] + Masstr[6] + Masstr[1] + Masstr[6] + Masstr[13] + Masstr[15] + Masstr[
        13] + Masstr[6] + Masstr[13] + Masstr[DoorBs] + Masstr[10]
    level3 = Masstr[16] + masspers[4] + Masstr[16] + masspers[5] + Masstr[18] + masspers[6] + Masstr[18] + \
             masspers[7] + Masstr[16]
    level4 = Masstr[9] + Masstr[15] + Masstr[13] + Masstr[6] + Masstr[13] + Masstr[15] + Masstr[13] + Masstr[6] + \
             Masstr[1] + Masstr[6] + Masstr[0] + Masstr[10]
    level5 = Masstr[16] + masspers[8] + Masstr[18] + masspers[9] + Masstr[DoorZag] + masspers[10] + Masstr[18] + \
             masspers[11] + Masstr[16]
    level6 = Masstr[9] + Masstr[15] + Masstr[13] + Masstr[6] + Masstr[1] + Masstr[6] + Masstr[1] + Masstr[6] + Masstr[
        13] + Masstr[15] + Masstr[10]
    level7 = Masstr[16] + masspers[12] + Masstr[16] + masspers[13] + Masstr[18] + masspers[14] + Masstr[18] + masspers[
        15] + Masstr[16]
    level8 = Masstr[7] + Masstr[0] + Masstr[5] + Masstr[1] + Masstr[5] + Masstr[1] + Masstr[5] + Masstr[0] + Masstr[8]
    print(f"{level0}\n{level1}\n{level2}\n{level3}\n{level4}\n{level5}\n{level6}\n{level7}\n{level8}")
    print("Меню-Вверх-Вниз-Влево-Вправо-Искать")


#---------------------------------------------------Лут и его генерация----------------------------------
def ResetLoot():
    if grib == "меч":
        massloot["меч"] += 1

    elif grib == "щит":
        massloot["щит"] += 1

    elif grib == "зелье лечения":
        massloot["зелье лечения"] += 1

    elif grib == "большое зелье лечения":
        massloot["большое зелье лечения"] += 1

    elif grib == "крысиное мясо":
        massloot["крысиное мясо"] += 1

    elif grib == "ключ от выхода":
        massloot["ключ от выхода"] += 1

    elif grib == "ключ от черной двери":
        massloot["ключ от черной двери"] += 1

def poisk():
    global masssearch, smenper, grib, idx
    for i in range(-1, 16):
        if i == smenper:
            if i == 0 and masssearch[i] == 1:
                grib = random.choice(lootkey)
                ResetLoot()
                masssearch[i] = 0
                print(f"Вы видите старый сундук, открыв его вы нашли {grib}")
                idx = lootkey.index(grib)
                del lootkey[idx]
            elif i == 1 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 2 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 3 and masssearch[i] == 1:
                grib = random.choice(lootand)
                ResetLoot()
                print(f"После долгой битвы вы решили обыскать комнату но было пусто м подойдя ближе к трупу монстра вы нашли в нем {grib}")
                masssearch[i] = 0
            elif i == 4 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 5 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 6 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 7 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 8 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 9 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 10 and masssearch[i] == 1:
                grib = random.choice(lootanroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
            elif i == 11 and masssearch[i] == 1:
                grib = random.choice(lootstartroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли в ящике {grib}")
                masssearch[i] = 0
                idx = lootstartroom.index(grib)
                del lootstartroom[idx]
            elif i == 12 and masssearch[i] == 1:
                grib = random.choice(lootkey)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
                idx = lootkey.index(grib)
                del lootkey[idx]
            elif i == 13 and masssearch[i] == 1:
                grib = random.choice(lootstartroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
                idx = lootstartroom.index(grib)
                del lootstartroom[idx]
            elif i == 14 and masssearch[i] == 1:
                grib = random.choice(lootstartroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли в трупе {grib}")
                masssearch[i] = 0
                idx = lootstartroom.index(grib)
                del lootstartroom[idx]
            elif i == 15 and masssearch[i] == 1:
                grib = random.choice(lootstartroom)
                ResetLoot()
                print(f"Вы обыскали комнату, и нашли {grib}")
                masssearch[i] = 0
                idx = lootstartroom.index(grib)
                del lootstartroom[idx]
            else:
                print("Здесь пусто")

#---------------------------------------------hehе это режимы------------------------------------------------------
random.seed()
class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
        self.score = 0
        self.bot_score = 0

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Страж - Тебе попалась карта {current}. У тебя {score} очков.')
        else:
            print(f'Стражнику попалась карта {current}. У Стражника {score} очков')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Туз':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)

        while True:
            newgame = ""
            choice = input('Страж - Будешь брать карту? Да || Нет || Отказаться\n')
            if choice == 'Да' or choice == 'да':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 23:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 23:
                    print('Страж - ХА-ХА, ты серьёзно думал, что сможешь меня обыграть? Ну ничего, когда-нибудь и тебе повезёт.\n')
                    Knight()
                    break
                elif score == 21 and bot_score == 23:
                    print('Страж - Карты у обоих - свелись в одно число. Ничья!\n')
                    print("Переигровка")
                    game.start()
                    break
                elif score == 21 or bot_score > 23:
                    print('Кажется, стража проигрышь только сильнее раззадорил, вам даже показался блеск его давно безжизненных глаз. Или это отражение от шлема?\nСтраж - Неплохо, странник, удачи!.')
                    break
            elif choice == 'нет' or choice == 'Нет':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 23:
                    print(f'Страж - Ты проиграл.\n у Вас {bot_score} очков, у Стражника {score} очков\nСтраж - ХА-ХА, ты серьёзно думал, что сможешь меня обыграть? Ну ничего, когда-нибудь и тебе повезёт.\n')
                    Knight()
                    break
                else:
                    print(f'Страж - Ты победил.\n у Вас {bot_score} очков, у Стражника {score} очков\nСтраж - Неплохо, странник, удачи!.')
                    break
            elif choice == 'Отказаться' or choice == 'отказаться':
                print(f'Жаль, но ты выбрал не тот путь')
                Knight()
                break
            else:
                karmauma()
    def start(self):
        random.shuffle(self.deck)
        print('Страж - Игра в Блэкджэк началась')
        print('Страж - В Блэкджеке десятки, валеты, дамы и короли стоят по 10 очков. Туз может стоить 1 или 11 очков')
        print('----------------------------------')
        self.choice()
game = BlackJack()

def HeadAche():
    lvl_quest = 0  # -Счётчик уровня-
    Voprosnik = [["Lost", "Soul", "Surprize"], ["Page", "List", "Clay"], ["Joker", "Sup", "Array"]]  # -Вопросы-
    a = random.choice(Voprosnik[0])
    print("И так, пришло время загадок\n")
    while lvl_quest == 0:
        if lvl_quest == 0:  # -Цикл с выбором вопросов-
            if a == "Lost":
                print('''Если в дом зайдёт-убьёт,
Без ножа, огня и стрел.
Вся семья глаз не сомкнёт,
Пока не похоронит тел.''')
                print("")
                print("Варианты ответа: Чума, Война, Dota 2.")
                b = str(input())
                if b == "Чума" or b == "чума":
                    lvl_quest = 1
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Война" or b == "война") or (b == "Dota 2" or b == "dota 2"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
            if a == "Soul":
                print('''Я подношу удары и сюрпризы.
Коль зла я – будешь в жертву принесен.
Ирония – сносить мои капризы.
Дарю подарки я, и мной ты наделен.''')
                print("")
                print("Варианты ответа: Балий, Оруженосец, Судьба.")
                b = str(input())
                if b == "Судьба" or b == "судьба":
                    lvl_quest = 1
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Балий" or b == "балий") or (b == "Оруженосец" or b == "оруженосец"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
            if a == "Surprize":
                print('''Один лечу легко и незаметно.
Когда нас много, тяжелы мы все равно.
Я раны исцеляю, но известно: 
проверку мной пройти немногим суждено.''')
                print("")
                print("Варианты ответа: Воля, Время, Птица")
                b = str(input())
                if b == "Время" or b == "время":
                    lvl_quest = 1
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Воля" or b == "воля") or (b == "Птица" or b == "птица"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
    a = random.choice(Voprosnik[1])
    while lvl_quest == 1:
        if lvl_quest == 1:  # -Цикл с выбором вопросов-
            print("")
            print("И так, следующая загадка.")
            print("")
            if a == "Page":
                print("Перед ним волы вспахивали белое поле, он держал плуг и сеял чёрные семена.")
                print("")
                print("Варианты ответа: Летописец, Пастух, Портной.")
                b = str(input())
                if b == "Летописец" or b == "летописец":
                    lvl_quest = 2
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Пастух" or b == "пастух") or (b == "Портной" or b == "портной"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
            if a == "List":
                print("Общей кормилицей всех, кто на свете живёт, я называюсь, пышно я летом цвету, зимою холодную мёрзну")
                print("")
                print("Варианты ответа: Вода, Земля, Трава.")
                b = str(input())
                if b == "Земля" or b == "земля":
                    lvl_quest = 2
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Вода" or b == "вода") or (b == "Трава" or b == "трава"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
            if a == "Clay":
                print("Гладок мой верхний конец, а нижний вовсе не гладок. Ловкой руке то одной, то другой стороной я полезен. То, что создаст одна моя часть, уничтожит другая.")
                print("")
                print("Варианты ответа: Молоток, Карандаш, Кисть.")
                b = str(input())
                if b == "Карандаш" or b == "карандаш":
                    lvl_quest = 2
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Молоток" or b == "молоток") or (b == "Кисть" or b == "кисть"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
    a = random.choice(Voprosnik[2])
    while lvl_quest == 2:
        if lvl_quest == 2:  # -Цикл с выбором вопросов-
            print("")
            print("В коем то веке - хоть кто-то дошёл до моей последней загадки...")
            print("")
            if a == "Joker":
                print("В мире есть дом; его голос звучит и шумит постоянно; Те же, что в доме живут, всегда молчаливы, безгласны; В вечном движении дом, и жители в вечном движении.")
                print("")
                print("Варианты ответа: Улей и пчелы, Муравейник и муравьи, Река и рыбы.")
                b = str(input())
                if b == "Река и рыбы" or b == "река и рыбы":
                    lvl_quest = 3
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Муравейник и муравьи" or b == "муравейник и муравьи") or (
                        b == "Улей и пчелы" or b == "улей и пчелы"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
            if a == "Sup":
                print("Нет у меня лица, но ничьё лицо мне не чуждо, дивный блеск изнутри ответит упавшему свету, но ничего не покажет, пока пред собой не увидит.")
                print("")
                print("Варианты ответа: Зеркало, Маска, Тень.")
                b = str(input())
                if b == "Зеркало" or b == "зеркало":
                    lvl_quest = 3
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Маска" or b == "маска") or (b == "Тень" or b == "тень"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
            if a == "Array":
                print("Всё строенье насквозь безвредным проникнуто жаром, страшный огонь всередине, но он никого не пугает, пышно разубран чертог, но люди в нём ходят нагие.")
                print("")
                print("Варианты ответа: Баня, Пожар в доме, Лагерь с костром.")
                b = str(input())
                if b == "Баня" or b == "баня":
                    lvl_quest = 3
                    print("Я тебя поздравляю, ты правильно ответил на мою загадку.")
                elif (b == "Пожар в доме" or b == "пожар в доме") or (
                        b == "Лагерь с костром" or b == "лагерь с костром"):
                    lvl_quest = -1
                else:
                    print("Вы неправильно ввели ответ. Не стоит ошибаться...")
    if lvl_quest == 3:  # -Победа игрока и получение ключа-
        print("")
        print("Ты очень догадлив путник! Я оставляю тебе ключ и можешь уходить прочь от этого места. Мне нужна тишина.")
        return
    if lvl_quest == -1:  # -Поражение игрока и вступление в бой с Заком-
        print("Ты ответил неправильно на мою загадку. Судьба всё предрешила, тебе придётся ответить за все свои грехи.")
        Zack()

# --------------------------------------------Смерти-------------------------------------------------
def karmauma():
    global godOfDead
    if godOfDead == 4:
        print("Вы чувствуете взгляд смотрящий на вас с презрением из-за вашей глупости")
        godOfDead -= 1
    elif godOfDead == 3:
        print("Вы чувствуете холод, вам стоит меньше ошибаться")
        godOfDead -= 1
    elif godOfDead == 2:
        print("Вы слышите крики доносящиеся из всех сторон")
        godOfDead -= 1
    elif godOfDead == 1:
        Deadofgod()
        godOfDead -= 1
        
#def sbroskarmu():
    #global godOfDead, semak, MASSODETOSTI, massloot, masssearch, ZackLive, OctopusLive, Knightlive1, Knightlive2, Mas, smenper, DoorEx, DoorBs, DoorZag, lootkey, lootstartroom, lootand, lootanroom, lootzagadka
    #godOfDead = 4
    #semak = 0
    #MASSODETOSTI = [0, 0]
    #massloot = {"меч": 0, "щит": 0, "зелье лечения": 0, "большое зелье лечения": 0, "крысиное мясо": 0,
                #"ключ от выхода": 0, "ключ от черной двери": 0, "ключ от красной двери": 0}
    #masssearch = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #ZackLive = 1
    #OctopusLive = 1
    #Knightlive1 = 1
    #Knightlive2 = 1
    #Mas = [100, 10, 4]
    #smenper = 1
    #DoorEx = 14
    #DoorBs = 14
    #DoorZag = 17
    #lootkey = ["ключ от черной двери", "крысиное мясо"]
    #lootstartroom = ["меч", "щит", "зелье лечения", "тряпье"]
    #lootand = ["ключ от выхода"]
    #lootanroom = ["зелье лечения", "крысиное мясо", "большое зелье лечения", "большое зелье лечения", "кость", "старую тряпку", "сгоревший труп", "камень"]
    #lootzagadka = ["ключ от красной двери"]
    #smena()

# --------------------------------------------Dead Fate-----------------------------------------------
def room0():
    global godOfDead, semak, smenper, DoorZag, DoorEx, DoorBs
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вниз" or ChoiseR == "вниз":
            print("Вы идете влево")
            smenper = 4
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room1():
    global godOfDead, semak, smenper, DoorEx
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
 
            smenper = 2
            smena()
            break
        elif ChoiseR == "Вверх" or ChoiseR == "вверх":
            if DoorEx == 14 and massloot["ключ от выхода"] == 0:
                print("Похоже на выход но дверь закрыта, надеюсь у меня получиться выйти")
            elif DoorEx == 14 and massloot["ключ от выхода"] == 1:
                print("Наконец эта дверь была открыта и один шаг до свободы, но мне рано идти....")
                DoorEx = 15
                massloot["Ключ от выхода"] = 0
                gameendall()
                semak = 1
                godOfDead = 0
                GameNa()
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room2():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Влево" or ChoiseR == "влево":
 
            smenper = 1
            smena()
            break
        elif ChoiseR == "Вниз" or ChoiseR == "вниз":
            smenper = 6
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room3():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вниз" or ChoiseR == "вниз":
            smenper = 7
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room4():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вверх" or ChoiseR == "вверх":
            smenper = 0
            smena()
            break
        elif ChoiseR == "Вниз" or ChoiseR == "вниз":
            smenper = 8
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room5():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
 
            smenper = 6
            smena()
            break
        elif ChoiseR == "Вниз" or ChoiseR == "вниз":
            smenper = 9
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room6():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
 
            smenper = 7
            smena()
            break
        elif ChoiseR == "Вверх" or ChoiseR == "вверх":
            smenper = 2
            smena()
            break
        elif ChoiseR == "Влево" or ChoiseR == "влево":
            smenper = 5
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room7():
    global godOfDead, godOfDead, semak, smenper, DoorBs
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Влево" or ChoiseR == "влево":
 
            smenper = 6
            smena()
            break
        elif ChoiseR == "Вверх" or ChoiseR == "вверх":
            if DoorBs == 14 and massloot["ключ от черной двери"] == 0:
                print("Огромная черная дверь кидает меня в дрожь, я не могу пройти, думаю мне стоит поискать ключ по комнатам")

            elif DoorBs == 14 and massloot["ключ от черной двери"] == 1:
                print("Я разглядел дверь чательнее и заметил круглые склизские отметины на ней \nОткрыв дверь ключ растворился,\nМне было видно в темноте лестницу ведущую вверх, я думаю это выход\nВскоре я зашел в длинный коридор и идя вперед, замечаю пьедистал и на нем древнего монстра")
                DoorBs = 15
                smenper = 3
                massloot["ключ от черной двери"] = 0
                smena()
                GameNa()

            elif DoorBs == 15:
                smenper = 3
                smena()
                GameNa()
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room8():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
 
            smenper = 9
            smena()
            break
        elif ChoiseR == "Вверх" or ChoiseR == "вверх":
            smenper = 4
            smena()
            break
        elif ChoiseR == "Вниз" or ChoiseR == "вниз":
            smenper = 12
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room9():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
 
            smenper = 10
            smena()
            break
        elif ChoiseR == "Влево" or ChoiseR == "влево":
            smenper = 8
            smena()
            break
        elif ChoiseR == "Вверх" or ChoiseR == "вверх":
            smenper = 5
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room10():
    global godOfDead, godOfDead, semak, smenper, DoorZag
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
 
            smenper = 11
            smena()
            break
        elif ChoiseR == "Влево" or ChoiseR == "влево":
            if DoorZag == 17 and massloot["ключ от красной двери"] == 0:
                print("Дверь покрывалась кровью столько раз что приобрела багровый цвет, я не могу пройти, думаю мне стоит поискать ключ по комнатам")
            elif DoorZag == 17 and massloot["ключ от красной двери"] == 1:
                print("Дверь покрывалась кровью столько раз, что приобрела багровый цвет, у меня есть красный ключ думаю он подойдет\nОткрыв дверь ключ застрял, я его оставил в замочной скважине,\nМне было видно лишь тьму, но вскоре глаза привыкли к ней и я прошел глубже\n")
                DoorZag = 18
                smenper = 9
                massloot["ключ от красной двери"] = 0
                smena()
                GameNa()
            elif DoorZag == 18:
                smenper = 9
                smena()
                GameNa()
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room11():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Влево" or ChoiseR == "влево":
            smenper = 10
            smena()
            break
        elif ChoiseR == "Вниз" or ChoiseR == "вниз":
            smenper = 15
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room12():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вверх" or ChoiseR == "вверх":
            smenper = 8
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room13():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
            smenper = 14
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room14():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вправо" or ChoiseR == "вправо":
            smenper = 15
            smena()
            break
        elif ChoiseR == "Влево" or ChoiseR == "влево":
            smenper = 13
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()

def room15():
    global godOfDead, godOfDead, semak, smenper
    while godOfDead > 0:
        ChoiseR = input()
        if ChoiseR == "Вверх" or ChoiseR == "вверх":
            smenper = 11
            smena()
            break
        elif ChoiseR == "Влево" or ChoiseR == "влево":
            smenper = 14
            smena()
            break
        elif ChoiseR == "Искать" or ChoiseR == "искать":
            poisk()
        elif ChoiseR == "Меню" or ChoiseR == "меню":
            Meny()
        else:
            karmauma()
#------------------------------------------------ИНВЕНТАРЬ И ТД--------------------------------------------------
def lootseychas():
    global massloot
    for item, count in massloot.items():
        n = 1
        if count >= 0 and count != 0:
            print(f"{item} - {count}")
            n += 1

def snyatieodev():
    global ChoiseR, MASSODETOSTI, Mas
    if (ChoiseR == "щит" or ChoiseR == "Щит") and massloot["щит"] != 0:
        if MASSODETOSTI[0] == 0:
            MASSODETOSTI[0] = 1
            print("Вы одели щит")
            Mas[2] += 3
        elif MASSODETOSTI[0] == 1:
            MASSODETOSTI[0] = 0
            print("Вы сняли щит")
            Mas[2] -= 3
        else:
            print("Я не знаю есть ли у меня этот предмет")
    elif (ChoiseR == "меч" or ChoiseR == "Меч") and massloot["меч"] != 0:
        if MASSODETOSTI[1] == 0:
            MASSODETOSTI[1] = 1
            print("Вы взяли в руку меч")
            Mas[1] += 7
        elif MASSODETOSTI[1] == 1:
            MASSODETOSTI[1] = 0
            print("Вы убрали меч")
            Mas[1] -= 7
        else:
            print("странно номер ошибки узнайте сами")

def proverka():
    global Mas
    if Mas[0] >= 115:
        Mas[0] = 115

def healzel():
    global ChoiseR
    if (ChoiseR == "крысиное мясо" or ChoiseR == "Крысиное мясо") and massloot["крысиное мясо"] != 0:
        Mas[0] += 22
        proverka()
        massloot["крысиное мясо"] -= 1
        print("Здоровье восстановилось на 22HP")
    elif (ChoiseR == "зелье лечения" or ChoiseR == "Зелье лечения") and massloot["зелье лечения"] != 0:
        Mas[0] += 35
        proverka()
        massloot["зелье лечения"] -= 1
        print("Здоровье восстановилось на 35HP")
    elif (ChoiseR == "Большое зелье лечения" or ChoiseR == "большое зелье лечения") and massloot["большое зелье лечения"] != 0:
        Mas[0] += 64
        proverka()
        massloot["большое зелье лечения"] -= 1
        print("Здоровье восстановилось на 64HP")
    else:
        print("Этого предмета у меня нет")

def srav():
    hlebushek = 0
    for i in massloot:
        if ChoiseR == i and massloot[i] != 0:
            hlebushek = 1
        if ChoiseR == "Крысиное мясо" and massloot["крысиное мясо"] != 0:
            hlebushek = 1
        elif ChoiseR == "Зелье лечения" and massloot["зелье лечения"] != 0:
            hlebushek = 1
        elif ChoiseR == "Большое зелье лечения" and massloot["большое зелье лечения"] != 0:
            hlebushek = 1
    if hlebushek >= 1:
        return True
    else:
        print("Этого предмета у меня нет")
        return False
def Vuborloot():
    global ChoiseR, karmauma
    klin = ""
    while semak != 1:
        ChoiseR = input("Введите ___(Название предмета) ИЛИ Вернитесь ___(Вернуться)\n")
        if ChoiseR == "Вернуться" or ChoiseR == "вернуться":
            break
        elif True == srav():
            while semak != 1:
                ChoiseRlocal = input("Вы точно хотите использовать предмет___(Да) --- (Нет)")
                if ChoiseRlocal == "да" or ChoiseRlocal == "Да":
                    print(ChoiseRlocal)
                    if ChoiseR == "меч" or ChoiseR == "Меч":
                        snyatieodev()
                        break
                    elif ChoiseR == "щит" or ChoiseR == "Щит":
                        snyatieodev()
                        break
                    elif (ChoiseR == "Зелье лечения" or ChoiseR == "зелье лечения") and massloot["зелье лечения"] != 0:
                        klin = "зелье лечения"
                        healzel()
                        print(f"Вы использовалили {klin}")
                        while massloot[klin] != 0:
                            ChoiseRlocal2 = input("Вы хотите использовать предмет еще раз___(Да) --- (Нет)")
                            if ChoiseRlocal2 == "Да" or ChoiseRlocal2 == "да":
                                healzel()
                                print(f"Вы использовалили {klin}")
                            elif ChoiseRlocal2 == "Нет" or ChoiseRlocal2 == "нет":
                                break
                        break
                    elif (ChoiseR == "Большое зелье лечения" or ChoiseR == "большое зелье лечения") and massloot["большое зелье лечения"] != 0:
                        klin = "большое зелье лечения"
                        healzel()
                        print(f"Вы использовалили {klin}")
                        while massloot[klin] != 0:
                            ChoiseRlocal2 = input("Вы хотите использовать предмет еще раз___(Да) --- (Нет)")
                            if ChoiseRlocal2 == "Да" or ChoiseRlocal2 == "да":
                                healzel()
                                print(f"Вы использовалили {klin}")
                            elif ChoiseRlocal2 == "Нет" or ChoiseRlocal2 == "нет":
                                break
                        break
                    elif (ChoiseR == "крысиное мясо" or ChoiseR == "Крысиное мясо") and massloot["крысиное мясо"] != 0:
                        klin = "крысиное мясо"
                        healzel()
                        print(f"Вы использовалили {klin}")
                        while massloot[klin] != 0:
                            ChoiseRlocal2 = input("Вы хотите использовать предмет еще раз___(Да) --- (Нет)")
                            if ChoiseRlocal2 == "Да" or ChoiseRlocal2 == "да":
                                healzel()
                                print(f"Вы использовалили {klin}")
                            elif ChoiseRlocal2 == "Нет" or ChoiseRlocal2 == "нет":
                                break
                        break
                    elif ChoiseR == "ключ от выхода" or ChoiseR == "Ключ от выхода":
                        print("Я не знаю где его использовать, возможно стоит найти подходящую дверь")
                        break
                    elif ChoiseR == "ключ от черной двери" or ChoiseR == "Ключ от черной двери":
                        print("Я не знаю где его использовать, возможно стоит найти подходящую дверь")
                        break
                    elif ChoiseR == "ключ от черной двери" or ChoiseR == "Ключ от черной двери":
                        print("Я не знаю где его использовать, возможно стоит найти подходящую дверь")
                        break
                    else:
                        karmauma()
                elif ChoiseRlocal == "Нет" or ChoiseRlocal == "нет":
                    break
                else:
                    karmauma()
        lootseychas()

def Inventary():
    lootseychas()
    Vuborloot()

def Meny():
    global semak, ChoiseR, godOfDead
    while godOfDead != 0:
        print("Инвентарь---Закончить---Продолжить")
        ChoiseR = input("")
        if ChoiseR == "Инвентарь" or ChoiseR == "инвентарь":
            Inventary()
        elif ChoiseR == "Закончить" or ChoiseR == "закончить":
            godOfDead = 0
            GameNa()
        elif ChoiseR == "Продолжить" or ChoiseR == "продолжить":
            print("-------____Вы продолжаете____-------")
            MapVision()
            break
        else:
            karmauma()

def GameNa():
    global godOfDead, semak, smenper, DoorZag, DoorEx, DoorBs
    time.perf_counter()
    while semak != 1:
        if godOfDead <= 0:
            break
        if semak == 1:
            break
        if random.randint(0, 10) == 1:
            if random.randint(0, 2) == 1:
                Goblin()
            else:
                Rat()
        if smenper == 0:
            MapVision()
            if Knightlive1 == 1:
                if smenper == 0 and Knightlive1 == 1:
                    KnightDialog1()
            room0()
        elif smenper == 1:
            MapVision()
            room1()
        elif smenper == 2:
            MapVision()
            room2()
        elif smenper == 3:
            MapVision()
            if OctopusLive == 1:
                OctopusLiveDialog()
            room3()
        elif smenper == 4:
            MapVision()
            room4()
        elif smenper == 5:
            MapVision()
            room5()
        elif smenper == 6:
            MapVision()
            room6()
        elif smenper == 7:
            MapVision()
            room7()
        elif smenper == 8:
            MapVision()
            room8()
        elif smenper == 9:
            MapVision()
            room9()
        elif smenper == 10:
            MapVision()
            if ZackLive == 1:
                ZackDialog()
            room10()
        elif smenper == 11:
            MapVision()
            room11()
        elif smenper == 12:
            MapVision()
            if Knightlive2 == 1:
                KnightDialog2()
            room12()
        elif smenper == 13:
            MapVision()
            room13()
        elif smenper == 14:
            MapVision()
            room14()
        elif smenper == 15:
            MapVision()
            room15()

hpddd = 0
vuborend = 0
def ppp():
    global hpddd
    if ZackLive == 1:
        hpddd += 1
    if Knightlive1 == 1:
        hpddd += 1
    if Knightlive2 == 1:
        hpddd += 1
    return
def gameendall():
    global ChoiseR, vuborend, godOfDead
    ppp()
    print("Пройдя в глубь вы видете 2 поворота налево и вправо")
    while True:
        ChoiseR = input("Сделайте выбор -- Влево || Вправо || Закончить -- ")
        if ChoiseR == "Влево" or ChoiseR == "влево" :
             printdelay("Вы идете влево")
             vuborend += 1
        elif ChoiseR == "Вправо" or ChoiseR == "вправо" :
             printdelay("Вы идете вправо")
             vuborend += 1
        elif ChoiseR == "Закончить" or ChoiseR == "закончить" :
             printdelay("")
             vuborend += 1
        else:
             karmauma()
        if vuborend == 4 and hpddd == 3:
             printdelay("Идя по бескрайним корридорам я наткнулся на длинный прямой путь, вскоре я увидел свет и пошел к нему... ")
             printdelay("Концовка - Начало бытия")
             godOfDead = 0
             hod()
        elif vuborend == 4 and hpddd <= 2:
             printdelay("Проходя корридоры, были слышны крики знакомых мне людей я даже забыл их, \nплутая я натыкался на множество дверей октрыв которые я видел лишь стены и очередная дверь решила мою дальнейшую судьбу.....")
             printdelay("Концовка - Неизвестная дверь")
             godOfDead = 0
             hod()
        elif vuborend == 2 and hpddd == 0:
             printdelay("Мне надоело ходить, и я решил вернуться, идя обратно я заметил что мир за мной \nпокружаеться в полный мрак и тень, заходить в него я не решился, мрак начал нагонять меня и видя лишь одну дверь я побежал к ней остался лишь только один шаг\nно я подвернул свою ногу и пытался ползти...")
             printdelay("Концовка - Предначертанная судьба")
             godOfDead = 0
             hod()
def hod():
    global ChoiseR, godOfDead, semak, smenper, DoorZag, DoorEx, DoorBs
    endgame = 0
    while endgame != 1:
        ChoiseR = input("Ваш выбор -- НАЧАТЬ -- игру или же -- ЗАКОНЧИТЬ -- . \n")
        if ChoiseR == "НАЧАТЬ" or ChoiseR == "Начать" or ChoiseR == "начать":
            NamePerson = str(input("Введите имя своего персонажа: "))
            if len(NamePerson) <= 10:
                TimeNamePerson.clear()
                TimeNamePerson.append(NamePerson)
                GameNa()
            elif len(NamePerson) > 10:
                print("Имя персонажа не может превышать 10 символов.")
        elif ChoiseR == "ЗАКОНЧИТЬ" or ChoiseR == "закончить" or ChoiseR == "Закончить":
            print("Жизнь была прекращена. \n")
            endgame += 1
        else:
            print("Пишите без ошибок в грамматике и логике, в игре это влияет на ваши шансы прохождения")
hod()
