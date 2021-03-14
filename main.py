import random
from bs4 import BeautifulSoup
import requests
import os


print('Сколько имён пользователей необходимо сгенерировать?:')
how_many_users_need = int(input())
directory = str(os.getcwd())

if how_many_users_need == 0:
    print('Невозможно создать 0(Ноль) пользователей, попробуйте  ещё раз')
else:

    url = 'https://statusname.ru/catalog/wevro3206/imya-v-rossii/?arrFilterNames_pf%5BATR_NAMES_GEN%5D=&arrFilter' \
          'Names_pf%5BATR_NAMES_ORIGIN%5D%5B%5D=74&arrFilterNames_pf%5BCONT_LEVEL%5D=null&arrFilterNames_pf%5BATR' \
          '_NAMES_TIP%5D=&arrFilterNames_pf%5BATR_NAMES_CHARS_COUNT%5D%5BLEFT%5D=&arrFilterNames_pf%5BATR_NAMES' \
          '_CHARS_COUNT%5D%5BRIGHT%5D=&arrFilterNames_pf%5BATR_NAMES_WORDS_COUNT%5D%5BLEFT%5D=&arrFilterNames' \
          '_pf%5BATR_NAMES_WORDS_COUNT%5D%5BRIGHT%5D=&set_filter=Применить&set_filter=Y'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.408', 'accept': '*/*'}
    users = []
    names = {'Мужские имена': [], 'Женские имена': []}
    surnames = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков',
                'Фёдоров', 'Морозов', 'Волков', 'Алексеев', 'Лебедев', 'Семенов', 'Егоров', 'Павлов', 'Козлов',
                'Степанов', 'Николаев', 'Орлов', 'Андреев', 'Макаров', 'Никитин', 'Захаров']
    reqsturl = requests.get(url, headers=headers).text
    bs = BeautifulSoup(reqsturl, 'html.parser')
    parses = bs.find_all('div', class_='names-item-name')
    for pars in parses:
        say_my_name = pars.find('a').get_text(strip=True)
        if say_my_name[-1] == 'а' or say_my_name[-1] == 'я':
            names['Женские имена'].append(say_my_name)
        else:
            names['Мужские имена'].append(say_my_name)
    for i in range(how_many_users_need):
        gender = random.choice(list(names.keys()))
        if gender == 'Женские имена':
            users.append(random.choice(names[gender]) + ' ' + random.choice(surnames) + 'а')
        else:
            users.append(random.choice(names[gender]) + ' ' + random.choice(surnames))
    with open(directory + '\\' + 'Генератор имён ' + '.txt', 'w', encoding='utf-8') as file:
        for user in users:
            file.write("'" + user + "'," + '\n')

