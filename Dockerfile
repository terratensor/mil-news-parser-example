# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y \
    wget \
    g++ \
    make \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Playwright и его зависимости
RUN pip install --upgrade pip && \
    pip install playwright==1.52.0 && \
    playwright install chromium && \
    playwright install-deps

# Создаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Команда для запуска приложения
ENTRYPOINT ["python", "example.py"]
CMD ["--url", "https://mil.ru/news/56eafbe6-bb32-49b4-ba3d-ae77e3876f84"]