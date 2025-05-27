import time
from datetime import datetime, timedelta
import random

def create_pet(animal):
    print('Добро пожаловать! Это - игра-тамагочи для тех, кто хочет обрести нового друга.')
    while True:
        animals_list = ['собака', 'кошка','хомяк', 'попугай']
        animal_type = input('Для начала выберите, какое животное вы хотите завести: (собака, кошка, хомяк, попугай): ')
        if animal_type.lower() in animals_list:
            print('Отлично! Теперь вашему новому питомцу нужно придумать имя.')
            animal['type'] = animal_type
            while True:
                name = input('Введите имя: ')
                res = input(f'Имя {name} устраивает вас? Если хотите продолжить, выберите "Да",'
                            f'"Нет" - вернуться к выбору имени. ')
                if res.lower() == 'да':
                    print(f'Здорово! {animal_type} по имени {name} теперь ваш новый друг!')
                    animal['name'] = name
                    break
                elif res.lower() == 'нет':
                    continue
                else:
                    print('Такого ответа мы не знаем. Попробуйте еще раз.')
            break
        else:
            print('Ой, кажется такого животного в нашем питомнике нет. Может попробуете еще раз?')
    animal['hunger'] = 50
    animal['health'] = 50
    animal['happiness'] = 50
    pet_instructions()
    return animal

def pet_instructions():
    print('Отлично! Теперь давайте разберемся, как ухаживать за питомцем.')
    time.sleep(4)
    print('У питомца есть 3 характеристики: здоровье, счастье и сытость. В начале игры они заполнены наполовину. '
          'Имейте ввиду, что сытость и здоровье - жизненно важные показатели')
    print('и если они упадут, то некоторые функции будут недоступны.')
    time.sleep(7)
    print('Чтобы восполнить показатели вы можете поиграть с животным, покормить, полечить, и приласкать. '
          'Делайте это регулярно, чтобы ваш питомец чувствовал себя хорошо.')
    time.sleep(7)
    print('ВАЖНО! Внимательно выбирайте пищу для своего питомца. Некоторая еда не подходит для '
          'определенных видов животных и может сказаться на состоянии здоровья.')
    time.sleep(7)
    print('На этом обучение заканчивается! Хорошей игры! Если вам снова понадобится инструкция, введите "помощь".')

def feed(animal):
    while True:
        food = {'собака': {'сухой корм', 'мясо', 'косточка', 'мясная печенька', 'вода'},
        'кошка': {'сухой корм', 'мясо', 'рыба', 'мясная печенька', 'вода'},
        'хомяк': {'сено', 'семечки', 'сушеные фрукты', 'яблоко', 'морковь', 'вода'},
        'попугай': {'семечки', 'сушеные фрукты', 'яблоко', 'морковь', 'корм для птиц', 'вода'}}
        stopword = 'выход'
        values_combined = set().union(*food.values())
        food_value = input("Выберите, чем накормить питомца: 'сухой корм', 'мясо', 'косточка', 'мясная печенька', "
                           "'вода', 'рыба', 'сено', 'семечки', 'сушеные фрукты', 'яблоко', 'морковь', 'корм для птиц'. "
                           "Если вы закончили, введите 'выход'.")
        food_key = animal['type']
        if food_value.lower() == stopword:
            break
        if food_value.lower() != stopword and food_value.lower().replace('  ', ' ').strip() in values_combined:
            if food_key in food:
                if food_value.lower().replace('  ', ' ').strip() in food[food_key]:
                    animal['hunger']+=15
                    print('Сытость +10')
                    if animal['hunger']>100:
                        animal['hunger'] = 100
                else:
                    random_hunger = random.randint(1, 5)
                    random_health = random.randint(1, 5)
                    random_happiness = random.randint(1, 5)
                    animal['hunger']+=random_hunger
                    animal['health']-=random_health
                    animal['happiness']-=random_happiness
                    print('Кажется, эта еда не подходит:( Будьте осторожны!')
                    print(f'Сытость +{random_hunger}, здоровье -{random_health}, счастье -{random_happiness}')
                    if animal['health']<0:
                        animal['health'] = 0
                    if animal['hunger'] > 100:
                        animal['hunger'] = 100
                    if animal['happiness'] < 0:
                        animal['happiness'] = 0
        else:
            print('Может вы где-то опечатались? Попробуйте снова.')

def print_pet_state(animal):
    pet_state = f'голод - {animal['hunger']}, здоровье - {animal['health']}, счастье - {animal['happiness']}'
    print(f'Текущее состояние питомца: {pet_state}')

def play(animal):
    while True:
        games = {'собака': {'кинуть игрушку', 'попросить дать лапу'},
            'кошка': {'кинуть игрушку', 'пошуршать фантиком'},
            'хомяк': {'кинуть игрушку', 'покачать в гамаке', 'прятки в домике'},
            'попугай': {'кинуть игрушку', 'покачать на жердочке', 'позвенеть колокольчиком'}}
        stopword = 'выход'
        all_values = set().union(*games.values())
        if animal['health'] <= 5:
            print('Ой-ой, здоровье вашего питомца слишком низкое для игр!')
            break
        if animal['hunger'] <= 5:
            print('Ой-ой, Ваш питомец слишком голоден, чтобы играть!')
            break
        game_value = input("Как хотите поиграть?: 'кинуть игрушку', 'попросить дать лапу', 'пошуршать фантиком', 'позвенеть колокольчиком',"
                     "'покачать в гамаке', 'прятки в домике', 'покачать на жердочке'. Если хотите закончить - введите 'выход':  ")
        game_key = animal['type']
        if game_value.lower() == stopword:
            break
        if game_value.lower() != stopword and game_value.lower() in all_values:
            if game_key in games:
                if game_value.lower().replace('  ', ' ').strip() in games[game_key]:
                    animal['happiness']+=10
                    animal['health']-=1
                    animal['hunger']-=2
                    print('Счастье +10, здоровье -1, сытость -2')
                    if animal['happiness'] >100:
                        animal['happiness'] = 100
                    if animal['health'] < 0:
                        animal['health'] = 0
                    if animal['hunger'] < 0:
                        animal['hunger'] = 0
                else:
                    random_happiness = random.randint(1, 5)
                    animal['happiness']+=random_happiness
                    print(f'Ваш питомец не умеет так играть, но рад, что вы уделили ему время. Счастье +{random_happiness}')
                    if animal['happiness'] > 100:
                        animal['happiness'] = 100
        else:
            print('Может вы где-то опечатались? Попробуйте снова.')

def pet_pet(animal):
    while True:
        interactions = ['погладить по голове', 'похвалить', 'погдадить по спинке', 'почесать']
        stopword = 'выход'
        choice = input("Что хотите сделать?: 'погладить по голове', 'похвалить', 'погдадить по спинке', 'почесать'. Если хотите выйти - введите 'выход': ")
        if choice.lower() == stopword:
            break
        if choice.lower().replace('  ', ' ').strip() in interactions:
            random_happiness = random.randint(1, 10)
            animal['happiness']+=random_happiness
            print(f'"Я так рад, хозяин!" Счастье +{random_happiness}')
            if animal['happiness'] > 100:
                animal['happiness'] = 100
        else:
            print('Может вы где-то опечатались? Попробуйте снова.')

def cure_pet(animal):
    while True:
        actions = ['дать витаминку', 'дать таблетку', 'поставить укол']
        stopword = 'выход'
        choice = input("Что вы хотите сделать?: 'дать витаминку', 'дать таблетку', 'поставить укол'. Если хотите выйти, введите 'выход':  ")
        if choice.lower() == stopword:
            break
        if choice.lower().replace('  ', ' ').strip() in actions:
            if choice.lower().replace('  ', ' ').strip() == actions[0]:
                animal['health']+=5
                print('Здоровье +5')
                if animal['health'] > 100:
                    animal['health'] = 100
            if choice.lower().replace('  ', ' ').strip() == actions[1]:
                animal['health']+=10
                print('Здоровье +10')
                if animal['health'] > 100:
                    animal['health'] = 100
            if choice.lower().replace('  ', ' ').strip() == actions[2]:
                animal['health']+=20
                animal['happiness'] -=2
                print('Ой, вашему питомцу не понравилась такая процедура:( Здоровье +20, счастье -2')
                if animal['health'] > 100:
                    animal['health'] = 100
                if animal['happiness'] < 0:
                    animal['happiness'] = 0
        else:
            print('Может вы где-то опечатались? Попробуйте снова.')


def write_time(end_game_time):
    with open(file_name, "a", encoding='utf-8') as file:
        file.write(f"{end_game_time}")

def read_time():
    with open(file_name, "r") as file:
        lines = file.readlines()
        if len(lines) >= 1:
            last_end_time = lines[1].strip()
        else:
            last_end_time = None
        return last_end_time

def check_time(animal):
    while True:
        last_end_time = read_time()
        start_time = datetime.now()
        last_end_time = datetime.strptime(last_end_time, "%Y-%m-%d %H:%M:%S.%f")
        time_difference = start_time - last_end_time

        print(f"Загружено последнее сохранение от {last_end_time}. Время между завершением и запуском: {time_difference}.")

        if timedelta(hours=5) <= time_difference < timedelta(hours=12):
            animal['health'] = max(0, animal['health'] - 50)
            animal['hunger'] = max(0, animal['hunger'] - 50)
            animal['happiness'] = max(0, animal['happiness'] - 50)
            print(f'Животное: {animal['type']}, имя: {animal['name']}, сытость: {animal['hunger']}, '
                  f'здоровье: {animal['health']}, счастье: {animal['happiness']}')
            return animal

        elif timedelta(hours=12) <= time_difference > timedelta(hours=24):
            animal['health'] = 0
            animal['hunger'] = 0
            animal['happiness'] = 0
            print(f'Животное: {animal['type']}, имя: {animal['name']}, сытость: {animal['hunger']}, '
                  f'здоровье: {animal['health']}, счастье: {animal['happiness']}')
            revive = input('О нет! К сожалению, вас не было слишком долго! '
                           'Ваш питомец умер, но его еще можно воскресить! Хотите воскресить? '
                           '("да" - воскресить питомца, "нет" - начнется новая игра.): ')
            if revive.lower() == 'да':
                print(f"Животное: {animal['type']}, имя: {animal['name']}, сытость: {animal['hunger']}, "
                      f"здоровье: {animal['health']}, счастье: {animal['happiness']}")
                return animal
            elif revive.lower() == 'нет':
                animal = create_pet(animal)
                return animal
            else:
                print('Может вы где-то опечатались? Попробуйте снова')


        elif time_difference > timedelta(hours=24):
            print(f'Животное: {animal['type']}, имя: {animal['name']}, сытость: {animal['hunger']}, '
                  f'здоровье: {animal['health']}, счастье: {animal['happiness']}')
            print('Очень жаль! Вас не было слишком долго, и ваш питомец умер! Воскресить его уже нельзя. '
                  'Может, с новым питомцем получится?')
            animal = create_pet(animal)
            return animal


def load_pet_data(file_name):
    while True:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                pet_info = file.read().split()
                if pet_info:
                    return pet_info
                else:
                    print('Файл пуст. Создайте нового питомца.')
                    return None
        except FileNotFoundError:
            print('Ошибка! Такого файла не существует, попробуйте снова.')
            file_name = input('Введите имя файла ещё раз: ')


'''ОСНОВНОЙ КОД'''


def pet_game_main(pet_info, create_pet, check_time, feed, play, pet_pet, cure_pet, pet_instructions, print_pet_state, write_time, file_name):
    if pet_info is None:
        animal = create_pet()
    else:
        animal = {'type': pet_info[0],
            'name': pet_info[1],
            'hunger': int(pet_info[2]),
            'health': int(pet_info[3]),
            'happiness': int(pet_info[4])}
        check_time(animal)

    while True:
        action = input(
            'Что вы хотите сделать сейчас? (покормить, поиграть, приласкать, полечить, помощь, удалить игру, '
            'выход (игра будет сохранена): '
        )
        if action == 'выход':
            res = input('Хотите сохранить игру и выйти? (да, нет): ')
            if res.lower() == 'да':
                with open(file_name, 'w', encoding='utf-8') as file:
                    out = " ".join(map(str, animal.values()))
                    file.write(out + '\n')
                end_game_time = datetime.now()
                write_time(end_game_time)
                break
            if res.lower() == 'нет':
                continue
        elif action == 'помощь':
            pet_instructions()
            print_pet_state(animal)
        elif action.lower() == 'покормить':
            feed(animal)
            print_pet_state(animal)
        elif action.lower() == 'поиграть':
            play(animal)
            print_pet_state(animal)
        elif action.lower() == 'приласкать':
            pet_pet(animal)
            print_pet_state(animal)
        elif action.lower() == 'полечить':
            cure_pet(animal)
            print_pet_state(animal)
        elif action.lower() == 'удалить игру':
            result = input(
                'Вы уверены, что хотите удалить текущего питомца? Восстановить игру будет невозможно (да, нет): ')
            if result.lower() == 'да':
                with open(file_name, 'wb'):
                    pass  # Очищаем файл
                break
            else:
                continue
        else:
            print('Такой команды нет.')

file_name = input('Выберите ячейку сохранения, которую хотите загрузить '
        '(вы можете завести несколько питомцев или кто-то может завести своего на вашем устройстве) '
        '"Pet_game_1.txt", "Pet_game_2.txt", "Pet_game_3.txt": ')
pet_info = load_pet_data(file_name)
pet_game_main(pet_info, create_pet, check_time, feed, play, pet_pet, cure_pet, pet_instructions, print_pet_state, write_time, file_name)





