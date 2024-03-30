from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NewsModel(BaseModel):
    """
    Модель данных о новостях.
    """

    author: str = Field(title="Автор")
    title: str = Field(title="Название")
    description: Optional[str] = Field(title="Описание")
    url: str = Field(title="Ссылка")
    published_at: Optional[datetime] = Field(title="Опубликовано")