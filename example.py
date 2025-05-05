import json
import os
import argparse
from parser.news_parser import MilNewsParser

def parse_news(url):
    """Функция для парсинга одной новости"""
    parser = MilNewsParser(headless=True)
    news_data = parser.parse_news(url)
    
    if news_data:
        print(f"Заголовок: {news_data['title']}")
        print(f"Дата: {news_data['date']}")
        print(f"Автор: {news_data['author']}")
        print("\nСодержание:")
        print(news_data['content'])
        
        # Сохранение в JSON
        with open("parsed_news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)
        print("\nРезультат сохранен в parsed_news.json")
        return True
    return False

def main():
    # Настройка парсера аргументов
    arg_parser = argparse.ArgumentParser(description='Парсер новостей Минобороны России')
    arg_parser.add_argument('--url', type=str, help='URL новости для парсинга')
    args = arg_parser.parse_args()

    # Получаем URL из аргументов или переменной окружения
    news_url = args.url or os.getenv('NEWS_URL')
    
    if not news_url:
        print("Ошибка: Не указан URL новости. Используйте --url или переменную окружения NEWS_URL")
        print("Пример использования:")
        print("  python example.py --url https://mil.ru/news/...")
        print("  или")
        print("  NEWS_URL=https://mil.ru/news/... python example.py")
        return

    if not parse_news(news_url):
        print("Не удалось получить данные")

if __name__ == "__main__":
    main()