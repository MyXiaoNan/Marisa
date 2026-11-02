from pathlib import Path
from typing import overload
from collections.abc import Callable

import ujson as json
from nonebot.log import logger
from pydantic import TypeAdapter

from marisa.configs import DATA_DIR
from marisa.schemas.item import Item, ItemType
from marisa.exception import ItemNotFoundError


class ItemManager:
    def __init__(self) -> None:
        self.file_path: Path = DATA_DIR / "items.json"
        self.items: list[Item] = self.load()

    def load(self) -> list[Item]:
        with open(self.file_path, encoding="UTF-8") as f:
            json_data = json.load(f)

        items = TypeAdapter(list[Item]).validate_python(json_data["items"])

        for item_type in ItemType.__args__:
            loaded_count = len(list(filter(lambda item: item.type == item_type, items)))
            logger.debug(f"Loaded {loaded_count} {item_type} items successfully.")

        logger.info(f"Loaded {len(items)} items successfully.")
        return items

    def save(self) -> None:
        json_data = {"items": [item.model_dump() for item in self.items]}
        with open(self.file_path, "w", encoding="UTF-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

    def add(self, item: Item) -> None:
        if not self.items:
            max_id = 0
        else:
            max_id = max([item.id for item in self.items if item.id is not None])

        item.id = max_id + 1
        self.items.append(item)
        self.save()

    def get(self, item_id: int) -> Item:
        for item in self.items:
            if item.id == item_id:
                return item
        raise ItemNotFoundError(item_id)

    @overload
    def filter(self, target: str) -> list[Item] | None: ...

    @overload
    def filter(self, target: Callable[[Item], bool]) -> list[Item] | None: ...

    def filter(self, target: str | Callable[[Item], bool]) -> list[Item] | None:
        if isinstance(target, str):
            filtered_items = filter(
                lambda item: target.lower() in item.name.lower(), self.items
            )
        elif callable(target):
            filtered_items = filter(target, self.items)
        return list(filtered_items)


item_manager = ItemManager()
