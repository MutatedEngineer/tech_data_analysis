import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Константы
TOKEN = token
RANDOM_SEED = 42
GENRE = ''
DATES = ['2020', '2025']
URL = "api.poiskkino.dev"
LIMIT = 250 # Допускается в диапазоне от 1 до 250

# Парсер сайта
def simple_parser(url, token, dates, limit):
    conn = http.client.HTTPSConnection(url)
    headers = { 'X-API-KEY': token}

    conn.request("GET", f"/v1.5/movie?year={dates[0]}&year={dates[-1]}&limit={LIMIT}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    with open('out_data.txt', 'a', encoding="utf-8", newline='\n') as f:
        f.write(data.decode("utf-8"))

df = simple_parser(URL, TOKEN, DATES, LIMIT)

# Графики для кучи

plt.plot()
plt.show()

# Базовая модель
