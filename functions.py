import json
import os
from pathlib import Path
import pickle
import csv


def text_to_json(name = 'res.txt'):
    with open (name, 'r', encoding='utf-8') as f, \
    open ('res.json', 'w', encoding='utf-8') as f2:
        res_list = []        
        for line in f:
            res_list.append(line.capitalize())
        json.dump(res_list, f2, indent=4)


def access_users(name = 'db.json')
    db = {}
    if os.path.exists(name) and os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as f:
            db = json.load(f)
    with open(name, 'w', encoding='utf-8') as f:
        while True:
            while True:
                try:
                    user_level = int(input('Введите уровень от 1 до 7 или любую букву для выхода: '))
                except:
                    json.dump(f, db)
                    exit()
                else:
                    break
            if not 1 <=user_level<= 7: 
                continue
            if user_level not in db:
                db[user_level] = {}
            while True:
                try:
                    user_id = int(input('Введите идентификатор: '))
                except:
                    print('Вы ввели не число!')
                else:
                    flag = False
                    for level in db:
                        for ident in db[level]:
                            if ident == user_id:
                                print('Идентификатор должен быть уникальным!')
                                flag = True
                                break
                    if flag:
                        continue   
                    else:
                        break            
            while True:
                user_name = input('Введите имя: ')
                if user_name:
                    break
                else:
                    print('Имя не должно быть пустым!')
            db[user_level][user_id] = user_name

def json_to_csv(name='db.json', res_file='db.csv'):
    with open(name, 'r', encoding='utf-8') as f_json:
        db = json.load(f_json)
    with open(res_file, 'r', encoding='utf-8') as f:
        for k, v in db.items():
            for k2, v2 in v.items():
                print(f"{k},{k2},{v2}", file=f)


def csv2json(from_file: Path, to_file: Path) -> None:
    json_list = []
    with open(from_file, 'r', newline='', encoding='utf-8') as f:
        csv_write = csv.reader(f, dialect='excel')
        for i, line in enumerate(csv_write):
            json_dict = {}
            if i == 0:
                continue
            else:
                level, id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f"{int(id):010}"
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f"{json_dict['name']}{json_dict['id']}")
                json_list.append(json_dict)

    with open(to_file, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


def json_to_pickle(directory='.'):
    for file in os.listdir(directory):
        file_name, file_extension = os.path.splitext(file)
        print(file_extension)
        if file_extension == '.json':
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
            with open(os.path.join(directory, file_name + '.pickle'), 'wb') as f:
                pickle.dump(data, f)


def pickle2csv(file: Path) -> None:
    with (
        open(file, 'rb') as f_read,
        open(f'{file.stem}2.csv', 'w', newline='', encoding='utf-8') as f_write,
    ):
        data = pickle.load(f_read)

        keys = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=keys, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)

        csv_write.writeheader()
        csv_write.writerows(data)


def csv2pickles(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)

    print(pickle.dumps(pickle_list))
