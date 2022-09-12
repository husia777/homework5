import random
content = []
flag = 1
guessed_words = []
dict_points = { 3 : 3,
                4 : 6,
                5 : 7,
                6 : 8}


name_user1 = []
name_user2 = []

dict_letters = {"а": 8, "б": 2, "в": 4, "г": 2, "д": 4, "е": 8, "ё": 1, "ж": 1, "з": 2, "и": 5, "й": 1, "к": 4, "л": 4,
             "м": 3, "н": 5, "о": 10, "п": 4, "р": 5, "с": 5, "т": 5, "у": 4, "ф": 1, "х": 1, "ц": 1, "ч": 1, "ш": 1,
             "щ": 1, "ъ": 1, "ы": 2, "ь": 2, "э": 1, "ю": 1, "я": 2}


# буквы которые есть у пользователей
user1_letters = []
user2_letters = []


#очки пользователей
user1_points = []
user2_points = []


#буква которую добовляем пользователю
user1_letters_to_be_added = []
user2_letters_to_be_added = []


#Функция приветствия и расфасовки каждому игроку по 7 букв для начала игры
def start_game():
    print('Привет.')
    print('Мы начинаем играть в Scrabble')
    print('Как зовут первого игрока?')
    global name_user1
    name_user1 = input('Введите ваше имя')
    print('Как зовут второго игрока?')
    global name_user2
    name_user2 = input('Введите ваше имя')
    print(f'{name_user1} vs {name_user2}')
    print('Раздаю случайные буквы')

    # распределение первых 7 букв
    for i in range(6):
        user1_letters.append(random.choice(list(dict_letters)))
        user2_letters.append(random.choice(list(dict_letters)))
    removing_letters_from_the_dictionary1(user1_letters)
    removing_letters_from_the_dictionary2(user2_letters)
    print(f'{name_user1} - буквы {" ".join(user1_letters)}')
    print(f'{name_user2} - буквы {" ".join(user2_letters)}')


#удаление букв из словаря которые выдали пользователю 1
def removing_letters_from_the_dictionary1(word):
    for letter in word:
        if letter in dict_letters:
            dict_letters[letter] -= 1
            if dict_letters[letter] == 0:
                del dict_letters[letter]


# удаление букв из словаря которые выдали пользователю 2
def removing_letters_from_the_dictionary2(word):
    for letter in word:
        if letter in dict_letters:
            dict_letters[letter] -= 1
            if dict_letters[letter] == 0:
                del dict_letters[letter]


# Ход и проверка хода первого игрока
def user1_move():
    print(f'Ходит  {name_user1}')
    print(f'{name_user1} - буквы {" ".join(user1_letters)}')
    while True:
        user1_input = input('Введите слово')
        print(f'Вы ввели слово {user1_input}')
        with open('ru_word.txt') as file:
            for line in file.readlines():
                line = line.rstrip('\n')
                content.append(line)

        if user1_input in content and 3 <= len(user1_input) <= 6 and user1_input not in guessed_words and list(user1_input).sort() == user1_letters:
            print('Такое слово есть.')
            print(f'{name_user1} получает {dict_points[len(user1_input)]} баллов')
            guessed_words.append(user1_input)
            user1_points.append(dict_points[len(user1_input)])
            global user1_letters_to_be_added
            user1_letters_to_be_added.clear()
            for i in range(len(user1_input) + 1):
                user1_letters_to_be_added.append(random.choice(list(dict_letters)))
            print(f'Добавляю буквы {str(user1_letters_to_be_added)}')
            user1_letters.extend(user1_letters_to_be_added)
            removing_letters_from_the_dictionary1(user1_letters_to_be_added)
            user1_letters_to_be_added.clear()
            for i in user1_input:
                if i in user1_letters:
                    user1_letters.remove(i)
            break

        else:
            print('Такого слова нет или это слово уже отгадывалось или вас нет нужных букв.')
            print(f'{name_user1} не получает очков.')
            user1_letters_to_be_added.append(random.choice(list(dict_letters)))
            print(f'Добавляю букву {str(user1_letters_to_be_added)}')
            user1_letters.extend(user1_letters_to_be_added)
            removing_letters_from_the_dictionary1(user1_letters_to_be_added)
            user1_letters_to_be_added.clear()
            break




# Ход и проверка хода второго игрока
def user2_move():
    print(f'Ходит  {name_user2}')
    print(f'{name_user2} - буквы {" ".join(user2_letters)}')
    while True:
        user2_input = input('Введите слово')
        print(f'Вы ввели слово {user2_input}')

        with open('ru_word.txt') as file:
            content = file.read()
            content = content.split('\n')
        if user2_input in content and 3 <= len(user2_input) <= 6 and user2_input not in guessed_words and list(user2_input).sort() == user2_letters:
            print('Такое слово есть.')
            print(f'{name_user2} получает {dict_points[len(user2_input)]} баллов')
            guessed_words.append(user2_input)
            content.remove(user2_input)
            print(content)
            user2_points.append(dict_points[len(user2_input)])
            global user2_letters_to_be_added
            user2_letters_to_be_added.clear()
            for i in range(len(user2_input) + 1):
                user2_letters_to_be_added.append(random.choice(list(dict_letters)))
            user2_letters.extend(user2_letters_to_be_added)
            print(f'Добавляю буквы {str(user2_letters_to_be_added)}')
            removing_letters_from_the_dictionary2(user1_letters_to_be_added)
            user2_letters_to_be_added.clear()
            for i in user2_input:
                if i in user2_letters:
                    user2_letters.remove(i)
            break

        else:
            print('Такого слова нет или это слово уже отгадывалось или вас нет нужных букв.')
            print(f'{name_user2} не получает очков.')
            user2_letters_to_be_added.append(random.choice(list(dict_letters)))
            print(f'Добавляю букву {str(user2_letters_to_be_added)}')
            user2_letters.extend(user2_letters_to_be_added)
            removing_letters_from_the_dictionary2(user2_letters_to_be_added)
            user2_letters_to_be_added.clear()
            break



#вывод победителя
def victory():
    if sum(user1_points) > sum(user2_points):
        print(f'Победил {name_user1}')
        print(f'{sum(user1_points)} : {sum(user2_points)}')

    elif sum(user1_points) < sum(user2_points):
        print(f'Победил {name_user2}')
        print(f'{sum(user2_points)} : {sum(user1_points)}')

    else:
        print('Ничья')
        print(f'{sum(user1_points)} : {sum(user2_points)}')


#старт игры
def start():
    while True:
        game = input('Нажмите старт для начала или стоп для выхода из игры')
        if game == 'старт':
            start_game()
            while len(dict_letters) > 0:
                user1_move()
                user2_move()
                print(dict_letters)

            else:
                break
                print('Игра окончена')
                victory()

        else:
            break
            victory()

    else:
        victory()


start()