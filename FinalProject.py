# TODO: Функция в итоге возвращает > 30к записей, но строки повторяются. Предположу, что необходимо в каждом проходе менять год. В целом работает

import http.client
import csv
import json

TOKEN = ''
LIMIT = 200

# Парсер сайта
def simple_parser(token, next_page=None):
    '''
    Функция обрабатывает полученные через бесплатный кинопоиск API 250 строк фильмов длиной от 60 до 250 минут, бюджетом
    от 1_000_000 до 1_000_000_000, и 2010-2020 года. Функия возвращает id, название, жанрб страну, рейтинги imdb,
    рейтинг кинопоиска, количество голосов, год. Сырые данные сбрасывает в csv файл для дальнейшей обработки. Возвращаемое значение - ключ
    следующей страницы, если такая имеется.
    Бесплатный доступ позволяет в сутки до 200 обращений к сайтую
    :param url:
    :param token:
    :param dates:
    :param limit:
    :return:
    '''

    conn = http.client.HTTPSConnection('api.poiskkino.dev')
    headers = { 'X-API-KEY': token}
    # Проверка наличия следующей страницы
    if not next_page:
        pars_string = f'/v1.5/movie?year=2021&movieLength=60-250&isSeries=false&&budget.value=1000000-1000000000&year=2010-2020&limit=250'

    else:
        pars_string = f'/v1.5/movie?year=2021&movieLength=60-250&isSeries=false&&budget.value=1000000-1000000000&year=2010-2020&limit=250&next={next_page}'

    conn.request("GET", pars_string, headers=headers)
    response = conn.getresponse()
    response_bytes = response.read()
    data = response_bytes.decode('utf-8')

    res = json.loads(data)
    # Создаем файл с заголовком
    with open('row_data_kinopoisk.csv', mode='w+', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'title', 'genres', 'countries', 'rating_kp', 'rating imdb', 'votes imdb', 'year']
        csv.DictWriter(file, fieldnames=fieldnames)

    # После каждого прохода функции дополняем файл полученными строками
    with open('row_data_kinopoisk.csv', mode='a+', newline='', encoding='utf-8') as file:
        fieldnames = ['id', 'title', 'genres', 'countries', 'rating_kp', 'rating imdb', 'votes imdb', 'year']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for elem in res['docs']:
            try:
                writer.writerow({'id': elem['id'], 'title': elem['alternativeName'], 'genres': elem['genres'][0]['name'],
                            'countries': elem['countries'][0]['name'],'rating_kp': elem['rating']['kp'],
                             'rating imdb': elem['rating']['imdb'], 'votes imdb': elem['votes']['imdb'], 'year': elem['year']})
            except KeyError:
                continue

    # Проверка наличия следующей страницы.
    if not res['hasNext']:
        return
    return res['next']

# Функция для автоматического перелистывания страниц, падает на момент достижения лимита.
for _ in range(LIMIT):
    next_page = simple_parser(TOKEN)
    if next_page:
        simple_parser(TOKEN, next_page)

