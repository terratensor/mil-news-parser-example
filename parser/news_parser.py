from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import json

class MilNewsParser:
    def __init__(self, headless=True):
        self.headless = headless

    def parse_news(self, url):
        """Основной метод для парсинга новости"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            context = browser.new_context(ignore_https_errors=True)
            page = context.new_page()
            
            try:
                page.goto(url, wait_until="networkidle", timeout=60000)
                
                # Ожидание загрузки ключевых элементов
                page.wait_for_selector('[class*="ComponentDateFullYear"]', timeout=10000)
                page.wait_for_selector('[class*="ComponentTitleText"]', timeout=10000)
                page.wait_for_selector('[class*="NewsOneContent"]', timeout=10000)
                
                html = page.content()
                soup = BeautifulSoup(html, "lxml")
                
                return {
                    "title": self._extract_by_partial_class(soup, "ComponentTitleText"),
                    "date": self._extract_by_partial_class(soup, "ComponentDateFullYear"),
                    "author": self._extract_author(soup),
                    "content": self._extract_news_content(soup),
                    "url": url
                }
            except Exception as e:
                print(f"Ошибка при парсинге: {e}")
                return None
            finally:
                context.close()
                browser.close()

    def _extract_by_partial_class(self, soup, class_part):
        element = soup.find(class_=lambda x: x and class_part in x)
        return self._clean_text(element.get_text()) if element else ""

    def _extract_author(self, soup):
        author_tag = soup.find('a', href=lambda x: x and "structuremorf" in x)
        return self._clean_text(author_tag.get_text()) if author_tag else ""

    def _extract_news_content(self, soup):
        news_block = soup.find('div', class_=lambda x: x and "NewsOneContent" in x)
        if not news_block:
            return ""

        content_div = news_block.find('div', class_='content')
        if not content_div:
            return ""

        paragraphs = []
        
        # Обрабатываем все элементы внутри content_div
        for element in content_div.children:
            if element.name == 'p':
                # Обработка параграфов
                text = self._clean_paragraph(element.get_text())
                if text and not any(exclude in text for exclude in [
                    "браузеры с поддержкой российских сертификатов",
                    "Вернуться на старую версию сайта"
                ]):
                    paragraphs.append(text)
            
            elif element.name in ['ul', 'ol']:
                # Обработка списков
                list_items = []
                for li in element.find_all('li', recursive=False):
                    li_text = self._clean_paragraph(li.get_text())
                    if li_text:
                        list_items.append(f"• {li_text}")
                
                if list_items:
                    paragraphs.append("\n".join(list_items))
            
            elif element.name == 'div' and element.get('class') == ['content']:
                # Обработка вложенного контента
                nested_content = self._extract_news_content(element.parent)
                if nested_content:
                    paragraphs.append(nested_content)

        return "\n\n".join(paragraphs)

    def _clean_text(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def _clean_paragraph(self, text):
        text = re.sub(r'[\n\r\t]+', ' ', text)
        text = re.sub(r'[ ]+', ' ', text)
        text = re.sub(r',([^\s])', r', \1', text)
        return text.strip()