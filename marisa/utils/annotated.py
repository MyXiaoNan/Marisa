from typing import Annotated

from sqlalchemy import select
from nonebot.params import Depends
from sqlalchemy.orm import selectinload
from nonebot_plugin_orm import SQLDepends

from .depends import get_user_id
from ..models import User as _User

UserInfo = Annotated[
    _User,
    SQLDepends(
        select(_User)
        .options(
            selectinload(_User.sect),
            selectinload(_User.backpack),
            selectinload(_User.status),
        )
        .where(_User.id == Depends(get_user_id))
    ),
]
