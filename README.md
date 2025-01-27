# GoIT, Python DataScience

## Вимоги

- Docker

## Запуск додатку

1. **Збірка Docker образу**:

   Спочатку потрібно зібрати Docker образ за допомогою наступної команди:

   ```bash
   docker build . -t trotskyi/goit-ds

2. **Запуск контейнера**:

   Запустіть контейнер із змонтованою поточною директорією в контейнер:

   ```bash
   docker run -it --name trotskyi-goit-ds-container -v $(pwd):/app trotskyi/goit-ds

3. **Встановлення залежностей за допомогою Poetry (при необхідності)**:

   Після того як контейнер буде запущено, встановіть усі залежності проєкту за допомогою Poetry:

   ```bash
   poetry install

4. **Запуск додатку (при необхідності)**:

   Тепер ви можете запустити додаток:

   ```bash
   python3 main.py

## Примітки

- Якщо ви зіткнулися з помилками під час запуску контейнера, використовуйте команду `docker logs <container_id>`, щоб
  переглянути логи контейнера.
- Для виходу з контейнера використовуйте команду `exit`.
- Для зупинки контейнеру `docker stop trotskyi-goit-ds-container`
- Для запуску контейнеру `docker start trotskyi-goit-ds-container`
- Зайти в термінал контейнеру `docker exec -it trotskyi-goit-ds-container bash`
- Для видалення контейнеру `docker rm trotskyi-goit-ds-container`
- Для видалення образу `docker rmi trotskyi/goit-ds`
- Показати всі контейнери `docker ps -a`
- Показати всі образи `docker images`
