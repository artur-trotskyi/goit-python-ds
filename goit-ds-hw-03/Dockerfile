FROM python:3.12.8-slim

# Declare environment variable
ENV APP_HOME=/app

# Set the working directory
WORKDIR $APP_HOME

# Copy all files
COPY . .
COPY pyproject.toml /app
COPY poetry.lock /app

# Install Poetry
RUN pip3 install poetry

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --only main --no-root

# Set the default command to run the application and keep the terminal open
CMD ["bash", "-c", "python main.py && exec bash"]
