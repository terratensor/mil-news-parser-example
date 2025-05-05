# Парсер новостей Минобороны России

Этот проект позволяет парсить новости с официального сайта Министерства обороны РФ (mil.ru).

## Особенности
- Получение заголовка, даты, автора и содержания новости
- Автоматическая очистка текста от лишних пробелов и форматирования
- Сохранение результатов в JSON

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/mil-news-parser.git
cd mil-news-parser
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
# ИЛИ
venv\Scripts\activate # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Установите Playwright браузер:
```bash
playwright install chromium
```

## Использование

1. Активируйте виртуальное окружение (если еще не активировано):
```bash
source venv/bin/activate # Linux/MacOS
# ИЛИ
venv\Scripts\activate # Windows
```

2. Запустите пример:
```bash
python example.py --url "https://mil.ru/news/e0e4b7d0-ef73-42a7-945c-da4369542ee0"
# или
NEWS_URL="https://mil.ru/news/e0e4b7d0-ef73-42a7-945c-da4369542ee0" python example.py
```


## Инструкция по сборке:

### 1. Соберите образ:

```bash
docker build -t mil-news-parser .
```

### 2. Если нужно очистить кеш:

```bash
docker build --no-cache -t mil-news-parser .
```

### 3. Запустите контейнер:

Через аргумент

```bash
docker run --rm mil-news-parser --url "https://mil.ru/news/e0e4b7d0-ef73-42a7-945c-da4369542ee0"
```

### 4. Для локального запуска без Docker:

```bash
python example.py --url "https://mil.ru/news/e0e4b7d0-ef73-42a7-945c-da4369542ee0"
```

или

```bash
NEWS_URL="https://mil.ru/news/e0e4b7d0-ef73-42a7-945c-da4369542ee0" python example.py
```