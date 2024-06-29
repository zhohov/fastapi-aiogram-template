import requests
from typing import Optional
from dataclasses import dataclass

from config import settings


@dataclass
class MessageDTO:
    id: int
    text: str


class MessagesApiClient:
    BASE_URL = settings.backend_url

    def get_message(self) -> Optional[MessageDTO]:
        url = self.BASE_URL + "message_router/"
        response = requests.get(url=url)

        return MessageDTO(**response.json())
    

message_client = MessagesApiClient()
