https://piptrends.com/compare/pipenv-vs-poetry

# PIPENV

cd app-pipenv 

### Перевіряємо версію pipenv
pipenv --version

### Перевіряємо версію Python
python3 --version
### Перевіряємо версію pip
pip --version

### Встановлюємо необхідний пакет для створення віртуальних середовищ (якщо він ще не встановлений)
sudo apt install python3-venv

### Встановлюємо pipenv
sudo apt install pipenv

### Перевіряємо версію pipenv після встановлення
pipenv --version

### Встановлюємо необхідні пакети із Pipfile у віртуальне середовище
pipenv install

### Встановлення додаткового пакету (наприклад, requests) в середовище pipenv
pipenv install requests

### Запускаємо скрипт за допомогою pipenv
### Ця команда запускає Python-скрипт в межах середовища pipenv
pipenv run python main.py

### Входимо в середовище pipenv
### Термінал перейде у віртуальне середовище, де ви зможете виконувати команди Python
pipenv shell

### Запускаємо файл main.py безпосередньо в середовищі pipenv
python ./main.py

### Вихід з середовища pipenv
### Після завершення роботи в середовищі, виходимо назад в основне середовище
exit


# POETRY

cd app-poetry

### Встановлюємо poetry
sudo apt install python3-poetry

### Ініціалізація нового проекту Poetry
poetry init

### Додавання пакету (наприклад, requests) в проект Poetry
poetry add requests

### Видалення пакету з проекту
poetry remove requests

### Запуск скрипта за допомогою poetry
poetry run python main.py

### Вхід в середовище poetry
poetry shell

### Додавання пакету для тестування (наприклад, pytest)
poetry add pytest

### Видалення пакету з середовища
poetry remove pytest

### Додавання пакету до групи (наприклад, для тестів)
poetry add pytest -G test

### Встановлення всіх залежностей
poetry install

### Встановлення лише основних залежностей
poetry install --only main

### Отримання інформації про середовище poetry
poetry env info

### Запуск main.py в середовищі Poetry
python ./main.py

### Вихід з середовища poetry
exit