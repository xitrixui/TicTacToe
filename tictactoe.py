# TICTACTOE
#............................... 
# 1) подключаем модули
# 2) ввод имен игроков и присваевание знаков
#   2.1) запрос на имя игрока_1
#   2.2) запрос на имя игрока_2
#   2.3) присваевание занака для игрока_1 choice_sign()
# 3) функция запуска игры main()
# 4) идет игра
# 5) функция для построения поля draw_field()
# 6) функция контроля ходов turn_control(sign)
# 7) функция для проверки победы win()
# 8) проверяем ничью
#...............................

# 1) подключаем модули
#...............................
import os   # модуль предоставляет функции для работы с операционной системой 
            # используем его для очищения консоли после каждого хода

import colorama                  # модуль позволяет менять цвет текста в терминале 
from colorama import init        # вызываем init для Windows
init(autoreset = True)           # autoreset контролирует сброс указанных вами цветов после каждого вывода
from colorama import Fore        # импортируем функцию Fore(меняет цвет текста): BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
#...............................

# список ячеек box
#...............................
box = list(range(1,10)) 
#...............................
#   1 2 3
#   4 5 6
#   7 8 9
#...............................

# дерево решений (англ. decision tree) decTree
#...............................
decTree = [(1,2,3),(4,5,6),(7,8,9), (1,4,7),(2,5,8),(3,6,9), (1,5,9),(3,5,7)] # -- LIST[TUPLE,...,TUPLE] -- список[кортеж,...,кортеж]
#...............................

# значения присваеваемые игрокам boxSign
#...............................
boxSign = [0] * 3 # создаем список 
                  # для простоты задействуем только индексы [1] и [2]
boxSign[1] = "X"  # 
boxSign[2] = "O"  # 
#...............................

# 2.1) запрос на имя игрока_1
# 2.2) запрос на имя игрока_2
#...............................
n1 = str(input("First player name: "))  # ввод и конвертация имени игрока_1
print("Hi, " + n1)                      # приветствуем игрока_1
print("")                               # пустая строка
n2 = str(input("Second player name: ")) # ввод и конвертация имени игрока_2
print("Hi, " + n2)                      # приветствуем игрока_2
#...............................

# 2.3) присваевание занака для игрока_1 choice_sign()
#...............................
def choice_sign():
    while True: # запускаем цикл

        # обработка исключений
        #...............................
        try: 
            # пользователь выбирает знак для игрока_1: 1 -- "X"; 2 -- "O"
            #...............................
            choice = input("choose X(1) or O(2): ") # ввод
            choice = choice.replace(" ","")         # удаляем все пробелы 
            choice = int(choice)                    # конвертируем ввод в INTEGER
            #...............................

            if not(choice in range(1,3)):             # если ввод не 1 или 2
                print(Fore.RED + "Incorrect input!")  # выводим ошибку
                continue                              # запускаем цикл заново

        except (ValueError, TypeError, NameError):    # если ввод имеет неверное значение
            print(Fore.RED + "Incorrect input!")      # выводим ошибку
            continue                                  # запускаем цикл заново
        #...............................
        
        return choice        # возвращаем это значение 
        break                # завершаем цикл
#...............................

# 5) функция для построения поля draw_field()
#...............................
def draw_field(): 
    print("")
    for i in range(3):
        # подробная работа цикла
        #...............................
        # 0 + 0 * 3 | 1 + 0 * 3 | 2 + 0 * 3
        # 0 + 1 * 3 | 1 + 1 * 3 | 2 + 1 * 3
        # 0 + 2 * 3 | 1 + 2 * 3 | 2 + 2 * 3
        #...............................
        # box[0] = 1 | box[1] = 2 | box[2] = 3
        # box[3] = 4 | box[4] = 5 | box[5] = 6
        # box[6] = 7 | box[7] = 8 | box[8] = 9
        #...............................
        print(Fore.WHITE + "\t  ", box[0 + i * 3], "  |  ", box[1 + i * 3], "  |  ", box[2 + i * 3])
        #...............................

        if (i < 2):
            print("\t----------------------")
        else:
            print("")
#...............................

# 6) функция контроля ходов turn_control(sign)
#...............................
def turn_control(p,s): # p -- player; s -- sign
    while True: # запускаем цикл

        # обработка исключений
        #...............................
        try:                           
            # выбор ячейки 
            #...............................
            val = input("Your turn " + p + "(" + s + "): ") # ввод номера ячейки
            val = val.replace(" ","")                       # удаляем все пробелы 
            val = int(val)                                  # конвертируем ввод в INTEGER
            #...............................         

            if not (val in range(1,10)):                        # если ввод не 1 -- 9
                print(Fore.RED + "Incorrect input!")            # выводим ошибку
                continue                                        # запускаем цикл заново

        except (ValueError, TypeError, NameError):              # если ввод имеет неверное значение
            print(Fore.RED + "Incorrect input!")                # выводим ошибку
            continue                                            # запускаем цикл заново
        #...............................

        # проверяем свободна ли ячейка
        #...............................
        if str(box[val - 1]) in 'XO':                     # если ячейка "X" "O"
            print(Fore.RED + "Box %i is not free" % val)  # выводим предупреждение, что ячейка уже занята
            continue                                      # запускаем цикл заново
        #...............................

        box[val - 1] = s # ячейка == sign и становится занята
        break
#...............................

# 7) функция для проверки победы win()
#...............................
def win(): 
    for each in decTree:
        # подробная работа цикла
        #...............................
        # decTree = [(1,2,3),(4,5,6),(7,8,9), 
        #            (1,4,7),(2,5,8),(3,6,9), 
        #            (1,5,9),(3,5,7)]           -- 8 ситуаций (0 -- 7)
        #...............................
        # each == decTree[0;1;2;3;4;5;6;7] => decTree[0;1;2;3;4;5;6;7][0;1;2]
        #...............................
        # decTree[0] == (1,2,3) -- 1 ситуация 
        # each[0] - 1 = 0       |==| each[1] - 1 = 1    |==| each[2] - 1 = O        -- DECTREE[TUPLE][INDEX_TUPLE] - 1 == INDEX_BOX -- выявляем index для ячейки box
        # box[0] = 1;"X";"O"    |==| box[1] = 2;"X";"O" |==| box[2] = 3;"X";"O"     -- BOX[INDEX_BOX] == [1;...;9]; BOXSIGN["X";"O"] -- пусто; знак "X" или "O"
        #
        # decTree[1] == (4,5,6) -- 2 ситуация
        # each[0] - 1 = 3       |==| each[1] - 1 = 4    |==| each[2] - 1 = 5 
        # box[3] = 4;"X";"O"    |==| box[4] = 5;"X";"O" |==| box[5] = 6;"X";"O"
        #
        # decTree[2] == (7,8,9) -- 3 ситуация
        # each[0] - 1 = 6       |==| each[1] - 1 = 7    |==| each[2] - 1 = 8 
        # box[6] = 7;"X";"O"    |==| box[7] = 8;"X";"O" |==| box[8] = 9;"X";"O"
        #
        # decTree[3] == (1,4,7) -- 4 ситуация
        # each[0] - 1 = 0       |==| each[1] - 1 = 3    |==| each[2] - 1 = 6 
        # box[0] = 1;"X";"O"    |==| box[3] = 4;"X";"O" |==| box[6] = 7;"X";"O"
        #
        # decTree[4] == (2,5,8) -- 5 ситуация
        # each[0] - 1 = 1       |==| each[1] - 1 = 4    |==| each[2] - 1 = 7 
        # box[1] = 2;"X";"O"    |==| box[4] = 5;"X";"O" |==| box[7] = 8;"X";"O"
        #
        # decTree[5] == (3,6,9) -- 6 ситуация
        # each[0] - 1 = 2       |==| each[1] - 1 = 5    |==| each[2] - 1 = 8 
        # box[2] = 3;"X";"O"    |==| box[5] = 6;"X";"O" |==| box[8] = 9;"X";"O"
        #
        # decTree[6] == (1,5,9) -- 7 ситуация
        # each[0] - 1 = 0       |==| each[1] - 1 = 4    |==| each[2] - 1 = 8 
        # box[0] = 1;"X";"O"    |==| box[4] = 5;"X";"O" |==| box[8] = 9;"X";"O"
        #
        # decTree[7] == (3,5,7) -- 8 ситуация
        # each[0] - 1 = 2       |==| each[1] - 1 = 4    |==| each[2] - 1 = 6 
        # box[2] = 3;"X";"O"    |==| box[4] = 5;"X";"O" |==| box[6] = 7;"X";"O"
        #...............................
        if (box[each[0] - 1] == box[each[1] - 1] == box[each[2] - 1]):
            # если знаки в 3х ячейках совпали, возвращаем знак в средней ячейке
            #...............................
            return box[each[1] - 1]
            #...............................
    else: # иначе цикл завершается и функция возвращает false
        #...............................
        return False
        #...............................
#...............................

# 3) функция запуска игры main()
#...............................
def main(): 

    # запускаем функцию (2.3)
    #...............................
    indexSign = choice_sign() # функция CHOICE_SIGN() возвращает 1 -- "X" или 2 -- "O"
    #...............................

    # параметры игрока
    #...............................
    player = [[0] * 3] * 3 # создаем список [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
                           # для простоты, снова, задействуем только индексы [1;2][1;2] и [1;2][1;2] 
    if (indexSign == 1):  # если функция CHOICE_SIGN() вернула нам 1 -- "X"
        player[1][1] = n1 # => [[0, 1, 2], [0, N1(имя игрока_1), 2], [0, 1, 2]] =>    
        player[2][2] = n2 # => [[0, 1, 2], [0, N1(имя игрока_1), 2], [0, 1, N2(имя игрока_2)]]
    else:                 # иначе, если функция CHOICE_SIGN() вернула нам 2 -- "O"
        player[1][2] = n1 # => [[0, 1, 2], [0, 1, N2(имя игрока_2)], [0, 1, 2]] =>
        player[2][1] = n2 # => [[0, 1, 2], [0, 1, N2(имя игрока_2)], [0, N1(имя игрока_1), 2]]
    #...............................


    turnCount = 0   # кол-во ходов
    playerCount = 1 # очередь игрока (первым ходит игрок_1)

    # 4) идет игра
    #...............................
    while True: # запускаем цикл

        os.system('cls') # очищаем консоль
        draw_field()     # запускаем функцию (5)

        # контроль ходов и очередности игроков
        #...............................
        if (turnCount > 0):        # если кол-во ходов больше 0
            if (playerCount == 1): # если была очередь игрока_1
                playerCount = 2    # ходит игрок_2
            else:                  # иначе если была очередь игрока_2
                playerCount = 1    # ходит игрок_1

            if (indexSign == 1): # если ходит игрок со знаком "X"
                indexSign = 2    # ходит игрок со знаком "O"
            else:                # иначе если ходит игрок со знаком "O"
                indexSign = 1    # ходит игрок со знаком "X"
        #...............................

        # запускаем функцию (6)
        #...............................
        sign = boxSign[indexSign]                           # присваеваем sign знак 
        name = player[playerCount][indexSign]               # присваеваем name имя игрока 
        turn_control(name, sign)                            # запускаем функцию и присваеваем ей переменные name и sign
        #...............................
        
        # запускаем функцию (7)
        #...............................
        if (turnCount > 3): # если кол-во ходов больше 3
            winner = win()  # запускаем функцию для проверки победы

            if winner:                                                              # если функцию вернула True
                os.system('cls')                                                    # очищаем консоль
                draw_field()                                                        # запускаем функцию (5)
                print(player[playerCount][indexSign] + " " + winner + " is winner") # выводим имя и знак победителя
                break                                                               # останавливаем цикл(игру)
        #...............................

        turnCount += 1 # прибавляем ход

        # 8) проверяем ничью
        #...............................
        if (turnCount > 8):  # если кол-во ходов больше 8
            os.system('cls') # очищаем консоль
            draw_field()     # запускаем функцию (5)
            print("Draw")    # (англ. ничья)
            break            # останавливаем цикл(игру)
        #...............................

    #...............................

#...............................

# запуск функцию (3)
#...............................
main()  # игра не начнется если не запустить главную функцию
input() # чтобы скомпилированная программа не закрывалась в конце игры, оставим это тут
#...............................