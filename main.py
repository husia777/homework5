import random

#список для считывания файла
content = []
#список слов которые были отгаданы
guessed_words = []
dict_points = {3 : 3,
               4 : 6,
               5 : 7,
               6 : 8}

#ввод игроков
user1_input = ''
user2_input = ''

#имя игроков
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


#Функция начисления балла при отрицательном ответе
def add_points(name_user, user_letters_to_be_added, user_letters,  ):
    print(f'{name_user} не получает очков.')
    user_letters_to_be_added.append(random.choice(list(dict_letters)))
    print(f'Добавляю букву {str(user_letters_to_be_added)}')
    user_letters.extend(user_letters_to_be_added)
    removing_letters_from_the_dictionary(user_letters_to_be_added)
    user_letters_to_be_added.clear()


#Функция приветствия и расфасовки каждому игроку по 7 букв для начала игры
def start_game(name_user1, name_user2, user1_letters, user2_letters):
    '''

    :return:
    '''
    print('Привет.')
    print('Мы начинаем играть в Scrabble')
    print(f'{name_user1} vs {name_user2}')
    print('Раздаю случайные буквы')

    # распределение первых 7 букв
    for i in range(50):
        user1_letters.append(random.choice(list(dict_letters)))
        user2_letters.append(random.choice(list(dict_letters)))
    removing_letters_from_the_dictionary(user1_letters)
    removing_letters_from_the_dictionary(user2_letters)
    print(f'{name_user1} - буквы {" ".join(user1_letters)}')
    print(f'{name_user2} - буквы {" ".join(user2_letters)}')

#удаление букв из словаря
def removing_letters_from_the_dictionary(word):
    for letter in word:
        if letter in dict_letters:
            dict_letters[letter] -= 1
            if dict_letters[letter] == 0:
                del dict_letters[letter]




# Ход и проверка хода  игрока
def user_move(name_user, user_letters, user_input, guessed_words, user_letters_to_be_added, dict_letters):
    """:param name_user: имя игрока
    :param user_letters: буквы которые есть у пользователя
    :param user_input: ввод слова
    :param guessed_words: список слов которые уже были разгаданы
    :param user_letters_to_be_added: буквы которые получит игрок
    :param dict_letters: словарь букв
    :return: функция прекращается при вводе пользователем exit
    """
    print(f'Ходит  {name_user}')
    print(f'{name_user} - буквы {" ".join(user_letters)}')
    print(f'Вы ввели слово {user_input}')
    with open('ru_word.txt', encoding='utf-8') as file:
        open_file = file.read().splitlines()
        # Проверяем есть ли слово введенное пользователем в файле и что его длина соответсвтует минимальной и максимальной длине слов в файле
    if user_input in open_file:
        #Проверяем не повторяется ли введенное слово
        if user_input not in guessed_words:
                #Проверяем имеются ли у нас все буквы для составления данного слова
                if list(user_input).sort() == user_letters.sort():
                    print('Такое слово есть.')
                    score = len(user_input)
                    print(score)
                    print(f'{name_user} получает {dict_points[score]} баллов')
                    guessed_words.append(user_input)
                    user1_points.append(dict_points[len(user_input)])
                    user_letters_to_be_added.clear()
                    for i in range(len(user_input) + 1):
                        user_letters_to_be_added.append(random.choice(list(dict_letters)))
                    print(f'Добавляю буквы {str(user_letters_to_be_added)}')
                    user_letters.extend(user_letters_to_be_added)
                    removing_letters_from_the_dictionary(user_letters_to_be_added)
                    user_letters_to_be_added.clear()
                    for i in user_input:
                        if i in user_letters:
                            user_letters.remove(i)


                else:
                    add_points(name_user, user_letters_to_be_added, user_letters)
                    print('У вас нет нужных букв.')
        else:
            add_points(name_user, user1_letters_to_be_added, user_letters)
            print('Это слово уже отгадывалось')

    else:
        add_points(name_user, user_letters_to_be_added, user_letters)
        print('Этого слова нет в файле')



#функция вывода победителя
def victory(user1_points, user2_points, name_user1, name_user2):
    if sum(user1_points) > sum(user2_points):
        print(f'Победил {name_user1}')
        print(f'{sum(user1_points)} : {sum(user2_points)}')
    elif sum(user1_points) < sum(user2_points):
        print(f'Победил {name_user2}')
        print(f'{sum(user2_points)} : {sum(user1_points)}')

    else:
        print('Ничья')
        print(f'{sum(user1_points)} : {sum(user2_points)}')

def exit(user_input):
    if user_input == 'exit':
        return False
    return True




#старт игры
def start():
    counter = 0
    print(dict_letters)
    user1_input = input('Как зовут первого игрока')
    user2_input = input('Как зовут второго игрока')
    start_game(user1_input, user2_input, user1_letters, user2_letters)
    while True:
        counter += 1
        if counter % 2 == 0:
            user_input = input(f'Ходит {user2_input}. Введите слово')
            if not exit(user_input):
                break
            user_move(user1_input, user2_letters, user_input, guessed_words, user2_letters_to_be_added,dict_letters)
        else:
            user_input = input(f'Ходит {user1_input}. Введите слово')
            if not exit(user_input):
                break
            user_move(user2_input, user1_letters, user_input, guessed_words, user1_letters_to_be_added, dict_letters)
    print('Игра окончена')
    victory(user1_points, user2_points, user1_input, user2_input)


start()