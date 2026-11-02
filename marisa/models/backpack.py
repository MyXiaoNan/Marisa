from nonebot_plugin_orm import Model
from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column


class Backpack(Model):
    """背包"""

    __tablename__ = "backpack"

    id: Mapped[str] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    """用户 ID"""
    item_id: Mapped[int]
    """物品 ID"""
    item_name: Mapped[str]
    """物品名称"""
    is_bundle: Mapped[bool]
    """是否为绑物"""
    is_equipped: Mapped[bool] = mapped_column(default=False)
    """是否装备"""
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    """创建时间"""
    update_time: Mapped[DateTime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    """更新时间"""
