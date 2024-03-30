import json
import os
from glob import glob

from models.news import NewsModel


class NewsService:
    """
    Сервис для работы с новостями.
    """

    def get_news(self) -> dict[str, list[NewsModel]]:
        """
        Получение списка новостей
        :return:
        """

        result = {}
        for filename in glob("fixtures/news/*"):
            with open(filename, encoding="utf-8") as file:
                # Получить код из названия файла
                alpha2code = os.path.basename(filename).split(".")[0]
                if data := json.load(file):
                    result[alpha2code] = [
                        NewsModel(
                            author=news.get("author"),
                            title=news.get("title"),
                            description=news.get("description"),
                            url=news.get("url"),
                            published_at=news.get("published_at"),
                        )
                        for news in data.get("articles", [])
                    ]

        return result