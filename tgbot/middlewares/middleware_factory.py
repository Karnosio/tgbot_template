from aiogram import BaseMiddleware
from aiogram.types import Message

from typing import Callable, Dict, Any, Awaitable


class MiddlewareFactory(BaseMiddleware):
    def __init__(self, obj: Any, name: str) -> None:
        self.obj = obj
        self.name = name

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        data[self.name] = self.obj

        return await handler(event, data)
