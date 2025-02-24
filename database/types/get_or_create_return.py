from dataclasses import dataclass

from tortoise import Model


@dataclass
class GetOrCreateReturn:
    data: Model
    is_new: bool
