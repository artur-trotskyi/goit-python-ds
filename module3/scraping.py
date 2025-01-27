import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

################################## Пошук на сторінці за тегом, за класом, за ID ##################################

"""
HTML-документ зберігає багато інформації, але, завдяки Beautiful Soup, простіше знаходити потрібні дані. 
Часом для цього потрібно лише один рядок коду. Спробуємо знайти всі теги span з класом text. 
Це, в свою чергу, поверне всі теги. Коли потрібно знайти кілька однакових тегів, варто використати функцію find_all().

Розмітка, що повертається, — це не зовсім те, що потрібно. 
Для отримання лише даних - цитат у цьому випадку, можна використовувати властивість .text.
"""

for quote in quotes:
    print(quote.text)

"""
Для пошуку та виведення всіх авторів працюємо за тим самим принципом — спершу потрібно вручну вивчити сторінку. 
Можна звернути увагу на те, що кожен автор взятий в тег <small> з класом author.
Далі використовуємо функцію find_all() та зберігаємо результат у змінній authors.
"""

quotes = soup.find_all('small', class_='author')

for quote in quotes:
    print(quote.text)

"""
Додамо код отримання всіх тегів для кожної цитати. Спочатку потрібно отримати кожен зовнішній блок кожної колекції тегів. 
Якщо цей перший крок не виконати, теги можна буде отримати, але асоціювати їх із конкретною цитатою — ні.
Коли блок отримано, можна опускатись нижче за допомогою функції find_all для отриманої підмножини. 
А далі буде потрібно додати внутрішній цикл для завершення процесу.
"""
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tagsforquote = tags[i].find_all('a', class_='tag')
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    break
