from dataclasses import dataclass
from typing import Type, Optional, Any

from tortoise import Model, BaseDBAsyncClient
from tortoise.models import MODEL

from database.types.get_or_create_return import GetOrCreateReturn


class CustomModel(Model):
    class Meta:
        abstract = True

    @classmethod
    async def get_or_create(
            cls: Type[MODEL],
            defaults: Optional[dict] = None,
            using_db: Optional[BaseDBAsyncClient] = None,
            **kwargs: Any,
    ) -> GetOrCreateReturn:
        return GetOrCreateReturn(*await super().get_or_create(defaults, using_db, **kwargs))
