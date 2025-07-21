from sqlalchemy import select
from nonebot_plugin_orm import get_session

from ..models import User, UserCD


async def calc_closing(user_id: str):
    """
    计算闭关获得的收益

    参数：
        user_id: 用户ID
    """
    session = get_session()
    async with session.begin():
        stmt = select(User).where(User.user_id == user_id)
        user = (await session.execute(stmt)).scalar()
        user_cd_info = await session.get(UserCD, user_id)

    if user is None or user_cd_info is None:
        return
