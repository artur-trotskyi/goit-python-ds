FROM python:3.12.8-slim

# оголошення змінної середовища
ENV APP_HOME=/app

# встановлення робочої директорії
WORKDIR $APP_HOME

# копіювання всіх файлів
COPY . .
COPY pyproject.toml /app
COPY poetry.lock /app

# встановлення poetry
RUN pip3 install poetry

# налаштування poetry
RUN poetry config virtualenvs.create false

# інсталяція залежностей
RUN poetry install --only main --no-root

# якщо потрібно, щоб python-програма запускалася автоматично,
# але також залишатися у терміналі після завершення виконання
CMD ["bash", "-c", "python main.py && exec bash"]


# docker build . -t trotskyi/python3.12.8-slim
# docker run -it --name examplesql-container3.12.8-slim -v $(pwd):/app trotskyi/python3.12.8-slim

# poetry install
# poetry add faker
# python3 fill_data.py


######################################################################################
# якщо вийшов із контейнера, то він може бути не запущений, треба перевірити
# docker ps -a

# якщо контейнер не працює, то треба його запустити
# docker start examplesql-container3.12.8-slim

# зайти в термінал контейнеру
# docker exec -it examplesql-container3.12.8-slim bash

# зупинити контейнер
# docker stop examplesql-container3.12.8-slim

# видалення контейнеру
# docker ps -a or docker ps
# docker rm examplesql-container3.12.8-slim
# docker ps -a or docker ps

# видалення образу
# docker rmi trotskyi/python3.12.8-slim
# docker images