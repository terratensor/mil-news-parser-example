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
python example.py
```

Или используйте в своем коде:
```python
from parser.news_parser import MilNewsParser

parser = MilNewsParser()
news_data = parser.parse_news("https://mil.ru/news/...")