from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
from selenium.webdriver.chrome.service import Service
import time
import csv

def writecena():
    driver = webdriver.Chrome()

    # URL страницы
    url = 'https://www.divan.ru/category/promo-dostavim-bystro-moscow?types%5B%5D=1'

    # Открытие страницы
    driver.get(url)

    # Ждем некоторое время, чтобы страница полностью загрузилась
    time.sleep(5)

    # Парсинг цен
    prices = driver.find_elements(By.CLASS_NAME, "ui-LD-ZU")
    print("Bcero:", len(prices))
    # Открытие CSV файла для записи
    with open('divan_prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])  # Записываем заголовок столбца

        # Записываем цены в CSV файл
        for price in prices:
            writer.writerow([price.text])

    # Закрытие драйвера
    driver.quit()


def clean_price(price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(price.replace('руб.', '').replace(' ', ''))


def create_new_csv():
    # Чтение данных из исходного CSV файла и их обработка
    input_file = ('divan_prices.csv')
    output_file = 'divan_cleaned_prices.csv'
    with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                      encoding='utf-8') as outfile:
         reader = csv.reader(infile)
         writer = csv.writer(outfile)

         # Читаем заголовок и записываем его в новый файл
         header = next(reader)
         writer.writerow(header)

         # Обрабатываем и записываем данные строк
         for row in reader:
             clean_row = [clean_price(row[0])]
             writer.writerow(clean_row)

    print(f"Обработанные данные сохранены в файл {output_file}")

def create_hist():
    # Загрузка данных из CSV-файла
    file_path = 'divan_cleaned_prices.csv'
    data = pd.read_csv(file_path)

    # Предположим, что столбец с ценами называется 'price'
    prices = data['Price']

    # Построение гистограммы
    plt.hist(prices, bins=10, edgecolor='black')

    # Мы можем изменить количество bin-ов по своему усмотрению

    # Добавление заголовка и меток осей
    plt.title('Гистограмма цен Ha DuBaHbI')
    plt.xlabel('Цена')
    plt.ylabel('Частота')

    # Показать гистограмму
    plt.show()
