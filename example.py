from parser.news_parser import MilNewsParser
import json

def main():
    # Инициализация парсера
    parser = MilNewsParser(headless=True)
    
    # URL новости для парсинга
    news_url = "https://mil.ru/news/e0e4b7d0-ef73-42a7-945c-da4369542ee0"
    
    # Парсинг новости
    news_data = parser.parse_news(news_url)
    
    if news_data:
        # Вывод результата
        print(f"Заголовок: {news_data['title']}")
        print(f"Дата: {news_data['date']}")
        print(f"Автор: {news_data['author']}")
        print("\nСодержание:")
        print(news_data['content'])
        
        # Сохранение в JSON
        with open("parsed_news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)
        print("\nРезультат сохранен в parsed_news.json")
    else:
        print("Не удалось получить данные")

if __name__ == "__main__":
    main()