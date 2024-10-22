from dataclasses import dataclass
from typing import Optional

import requests

from config import settings


@dataclass
class MessageDTO:
    id: int
    text: str


class MessagesApiClient:
    BASE_URL = settings.backend_url

    def get_message(self) -> Optional[MessageDTO]:
        url = self.BASE_URL + "messages/"
        response = requests.get(url=url)

        return MessageDTO(**response.json())


message_client = MessagesApiClient()
