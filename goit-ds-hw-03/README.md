# GoIT, Homework #3

## Вимоги

- Docker

## Запуск додатку

1. **Збірка Docker образу**:

   Спочатку потрібно зібрати Docker образ за допомогою наступної команди:

   ```bash
   docker build . -t trotskyi/goit-ds-hw-03

2. **Запуск контейнера**:

   Запустіть контейнер із змонтованою поточною директорією в контейнер:

   ```bash
   docker run -it --name trotskyi-container-hw-03 -v $(pwd):/app trotskyi/goit-ds-hw-03

3. **Встановлення залежностей за допомогою Poetry (при необхідності)**:

   Після того як контейнер буде запущено, встановіть усі залежності проєкту за допомогою Poetry:

   ```bash
   poetry install

4. **Запуск додатку**:

   Тепер ви можете запустити додаток із папки app:

   ```bash
   cp mongo_homework/.env.example mongo_homework/.env
   заповнити mongo_homework/.env
   python3 mongo_homework/main.py
   python3 scraper/main.py

## Примітки

- Якщо ви зіткнулися з помилками під час запуску контейнера, використовуйте команду `docker logs <container_id>`, щоб
  переглянути логи контейнера.
- Для виходу з контейнера використовуйте команду `exit`.
- Для зупинки контейнеру `docker stop trotskyi-container-hw-03`
- Для запуску контейнеру `docker start trotskyi-container-hw-03`
- Для відкриття терміналу контейнеру `docker exec -it trotskyi-container-hw-03 bash`
- Для видалення контейнеру `docker rm trotskyi-container-hw-03`
- Для видалення образу `docker rmi trotskyi/goit-ds-hw-03`
- Для списку контейнерів `docker ps -a`
- Для списку образів `docker images`
