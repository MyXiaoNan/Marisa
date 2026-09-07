from typing_extensions import Self
from dataclasses import field, dataclass

from marisa import models
from marisa.utils.jsondata import jsondata
from marisa.utils.manager import BuffManager, BackpackManager


@dataclass(kw_only=True)
class HeaderContext:
    name: str
    avatar: str | None = None
    stone: float
    level: str

    @classmethod
    def from_user(cls, user: models.User) -> Self:
        level_name = jsondata.get_level_name(user.level)

        return cls(name=user.user_name, stone=user.stone, level=level_name)


@dataclass(frozen=True, kw_only=True)
class BasicContext:
    """基本信息"""

    root: str = field(metadata={"title": "灵根"})
    level_up_status: str = field(metadata={"title": "突破状态"})

    metadata = {"title": "基本信息"}

    @classmethod
    def from_user(cls, user: models.User) -> Self:
        level_rate = jsondata.get_level_up_probability(user.level)
        last_level = list(jsondata._get_level_data().keys())[-1]
        if user.level == last_level:
            level_up_status = "位面至高"
        else:
            need_exp = jsondata.get_level_exp(user.level + 1) - user.exp
            if need_exp > 0:
                level_up_status = f"还需 {need_exp} 修为可突破！"
            else:
                level_up_status = f"即刻突破！突破概率：{level_rate} %"

        root = jsondata.get_root_data(user.root)
        dr_buff = next(buff for buff in root.buff if buff.type.value == "exp")

        return cls(
            root=f"{user.root}（{user.root_type} + {dr_buff.value * 100} %）",
            level_up_status=level_up_status,
        )

    def get_field_content(self, field_name: str):
        field_value = getattr(self, field_name)

        field_metadata = self.__dataclass_fields__[field_name].metadata
        content_template = field_metadata.get("content", None)

        if content_template:
            return content_template.format(field_value)
        else:
            return str(field_value)


@dataclass(frozen=True, kw_only=True)
class CombatContext:
    """战斗属性"""

    atk: float = field(metadata={"title": "攻击力"})
    dharma: str = field(metadata={"title": "法器"})
    armor: str = field(metadata={"title": "防具"})

    metadata = {"title": "战斗属性"}

    @classmethod
    def from_user(cls, user: models.User) -> Self:
        buff = BuffManager(user)
        backpack = BackpackManager(user)

        dharma = backpack.filter(
            lambda item: (
                item.type == "dharma" and bool(item.model_dump().get("is_equipped"))
            )
        )
        armor = backpack.filter(
            lambda item: (
                item.type == "armor" and bool(item.model_dump().get("is_equipped"))
            )
        )

        return cls(
            atk=buff.atk,
            dharma=dharma[0].name if dharma else "无",
            armor=armor[0].name if armor else "无",
        )

    def get_field_content(self, field_name: str):
        field_value = getattr(self, field_name)

        field_metadata = self.__dataclass_fields__[field_name].metadata
        content_template = field_metadata.get("content", None)

        if content_template:
            return content_template.format(field_value)
        else:
            return str(field_value)


@dataclass(frozen=True, kw_only=True)
class SectContext:
    """宗门信息"""

    name: str = field(metadata={"title": "所在宗门"})
    position: str = field(metadata={"title": "宗门职位"})

    metadata = {"title": "宗门信息"}

    @classmethod
    def from_user(cls, user: models.User) -> Self:
        sect_id = user.sect.sect_id
        if sect_id:
            sect_name = user.sect.info.name
            sect_position = user.sect.position
        else:
            sect_name = sect_position = "无"

        return cls(name=sect_name, position=sect_position if sect_position else "无")

    def get_field_content(self, field_name: str):
        field_value = getattr(self, field_name)

        field_metadata = self.__dataclass_fields__[field_name].metadata
        content_template = field_metadata.get("content", None)

        if content_template:
            return content_template.format(field_value)
        else:
            return str(field_value)


@dataclass(frozen=True, kw_only=True)
class RankContext:
    """排行信息"""

    register: int = field(
        metadata={"title": "注册位数", "content": "道友是踏入修真界的第 {} 人"}
    )
    exp: int = field(
        metadata={"title": "修为排行", "content": "道友的修为排在第 {} 位"}
    )
    stone: int = field(
        metadata={"title": "灵石排行", "content": "道友的灵石排在第 {} 位"}
    )

    metadata = {"title": "排行信息"}

    def get_field_content(self, field_name: str):
        field_value = getattr(self, field_name)

        field_metadata = self.__dataclass_fields__[field_name].metadata
        content_template = field_metadata.get("content", None)

        if content_template:
            return content_template.format(field_value)
        else:
            return str(field_value)


@dataclass(kw_only=True)
class UserContext:
    header: HeaderContext
    basic: BasicContext
    combat: CombatContext
    sect: SectContext
    rank: RankContext | None = None

    @classmethod
    def from_user(cls, user: models.User):
        return cls(
            header=HeaderContext.from_user(user),
            basic=BasicContext.from_user(user),
            combat=CombatContext.from_user(user),
            sect=SectContext.from_user(user),
        )

    def items(self):
        return {
            "basic": self.basic,
            "combat": self.combat,
            "sect": self.sect,
            "rank": self.rank,
        }.items()
