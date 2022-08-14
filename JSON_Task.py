import json, csv

data = None
filename = 'json_file.json'


def csv_file():
    with open("json_file.json", "r") as jfile:
        data = json.load(jfile)
    print(data)

    with open("new_data.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(key for key in data[0].keys())
        for item in data:
            writer.writerow(value for value in item.values())


def new_worker_add():
    new_worker = {
            "name": "Mikhail Olshevski",
            "birthday": "19.11.1996",
            "height": 185,
            "weight": 84,
            "car": True,
            "languages": ["Python"]
        }
    filename = 'json_file.json'

    with open(filename, 'r') as jfile:
        data = json.load(jfile)

    data.append(new_worker)

    with open(filename, 'w') as jfile:
        json.dump(data, jfile, indent=4)


def worker_name(search):
    with open(filename, 'r') as jfile:
        data = json.load(jfile)

    for item in data:
        if item['name'] == search:
            print(item)


def language(language):
    with open(filename, 'r') as jfile:
        data = json.load(jfile)

    for item in data:
        if language in item['languages']:
            print(item)


def year_height(year):
    with open(filename, 'r') as jfile:
        data = json.load(jfile)

    heights = []
    for item in data:
        if int(item['birthday'][-4:]) > year:
            heights.append(item['height'])
    sum = 0
    for i in range(len(heights)):
        sum += heights[i]
    print(f'Средний рост сотрудников, младше {year} года рождения - {sum / len(heights)}')

print('Выберите ваше действие:\n'
      '1. Перевести JSON файл в CSV\n'
      '2. Добавить нового работника\n'
      '3. Получить информацию о работнике\n'
      '4. Получить информацию о работниках, по выбранному языку програмированния\n'
      '5. Узнать средний рост сотрудников младше заданного года\n'
      '6. Выход из программы\n')
while True:
    choise = input('Ваш выбор - ')
    if choise == '1':
        csv_file()
    elif choise == '2':
        new_worker_add()
    elif choise == '3':
        worker_name(input('Введите имя человека - '))
    elif choise == '4':
        language(input('Введите язык программирования - '))
    elif choise == '5':
        year_height(int(input('Введите год рождения для исследования - ')))
    elif choise == '6':
        print('До свидания!')
        break
