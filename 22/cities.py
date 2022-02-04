#!../venv/bin/python3
import csv
from datetime import datetime
import os
from random import randint


def create_log_file():
    today = datetime.today()
    time_stamp = today.strftime("%d-%m-%Y-%H:%M")
    if not os.path.exists('log/'):
        os.mkdir("log")
    log_file_name = "log/" + time_stamp + ".log"
    return log_file_name

def read_database(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        result_list = list()
        reader = csv.reader(file)
        for string in reader:
            result_list.append("".join(string))
    return result_list

def get_city_list(first_letter, cities_container):
    if not isinstance(first_letter, str):
        raise TypeError
    if len(first_letter) != 1:
        raise ValueError
    first_letter=first_letter.upper()
    if "А" < first_letter > "Я":
        raise ValueError("Буква вне допустимого диапазона А-Я")
    selected = [city for city in cities_container if len(city) > 0 and city[0] == first_letter]
    return selected

def get_valid_city(first_letter, cities_container):
    # Список городов начинающихся с заданной буквы
    city_list = get_city_list(first_letter, cities_container)
    # Список городов на которые возможно сделать ход
    possible_city_list = [city for city in city_list if len(get_city_list(city[-1], cities_container)) > 0]
    if possible_city_list:
        return possible_city_list[0]
    else:
        return None

def find_city(city, cities_container):
    city = (city.lower()).replace("-", " ")
    city_list = city.split()
    for current_city in cities_container:
        current_city_lower = current_city.lower()
        current_city_lower = current_city_lower.replace('-', ' ')
        current_city_list = current_city_lower.split()
        if len(city_list) == len(current_city_list) and current_city_list == city_list:
            return current_city
    return None

def get_random_city(city_container):

    random_letter = chr(randint(ord('А'), ord('Я')))

    city = get_valid_city(random_letter, city_container)
    while not city:
        city = get_valid_city(random_letter, city_container)
        print(city)
    return city

cities_filename = "cities_database.csv"

while not os.path.exists(cities_filename):
    print("Файл базы данных городов не найден")
    print("Введите путь до файла с базой городов *.csv")
    cities_filename = input()

cities_set = set(read_database(cities_filename))
mentioned_cities = set()

log_file = open(create_log_file(), mode='w', encoding="utf-8")
log_writer = csv.writer(log_file)


print("Игра в города")
score_counter = 0
k_counter =0
error_counter = 0

bot_city = get_random_city(cities_set)
mentioned_cities.add(bot_city)
print(bot_city)
log_writer.writerow(['bot-', bot_city])


print("Вам на ", bot_city[-1].upper())
while error_counter < 5:
    user_city = input()
    user_city_checked = find_city(user_city, cities_set)
    if user_city_checked:
        if user_city_checked not in mentioned_cities:
            mentioned_cities.add(user_city_checked)
            score_counter+=1
            log_writer.writerow(['user-', user_city])
            if user_city_checked[0].lower() == bot_city[-1].lower():
                for letter in user_city_checked[::-1]: # Перебор букв с конца пока не встретим ту на которую есть города
                    bot_city = get_valid_city(letter, cities_set - mentioned_cities)
                    if bot_city:
                        print(bot_city)
                        mentioned_cities.add(bot_city)
                        log_writer.writerow(['bot-', bot_city])
                        print("Вам на ", bot_city[-1].upper())
                        if bot_city[-1].lower()=="к":
                            k_counter +=1
                        break
                    elif get_city_list(letter, cities_set - mentioned_cities):
                        print('Все города на букву', letter,' уже назывались')
                    elif get_city_list(letter, cities_set):
                        print('Городов на букву', letter, ' в базе данных нет')
            else:
                print("Город должен начинаться с буквы ", bot_city[-1].upper())
                error_counter += 1
        else:
            print("Такой город уже назывался")
            error_counter += 1
    else:
        print("Такого города нет в базе данных")
        error_counter += 1

print("Игра завершена")
print("Ваш результат", score_counter, "очков")
print("Вы назвали ", k_counter, "городов на К")


log_file.close()
print("Результаты сохранены в файл")