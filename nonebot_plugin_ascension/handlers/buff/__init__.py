from nonebot.internal.adapter import Event
from nonebot_plugin_orm import async_scoped_session
from nonebot_plugin_alconna import Button, Command, UniMessage, FallbackStrategy

from ...utils.annotated import UserInfo
from ...models import UserCD, UserStatus

in_closing = Command("闭关").build(use_cmd_start=True)
out_closing = Command("出关").build(use_cmd_start=True)


@in_closing.handle()
async def _(event: Event, user: UserInfo, session: async_scoped_session):
    if user is None:
        await (
            UniMessage.text("修仙界没有你的足迹，输入 『 /我要修仙 』 加入修仙世界吧！")
            .keyboard(Button("input", "我要修仙", text="/我要修仙"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    usercd_info = await session.get(UserCD, user.user_id)

    if not usercd_info:
        session.add(UserCD(user_id=event.get_user_id(), status=UserStatus.MEDITATING))
        await session.commit()
    elif usercd_info.status == UserStatus.NONE:
        usercd_info.status = UserStatus.MEDITATING
        await session.commit()
    else:
        match usercd_info.status:
            case UserStatus.MEDITATING:
                await UniMessage.text("道友正在闭关呢，小心走火入魔！").finish(
                    at_sender=True
                )
            case UserStatus.WORKING:
                await UniMessage.text("道友正在做悬赏令呢，分身乏术！").finish(
                    at_sender=True
                )
            case UserStatus.EXPLORING:
                await UniMessage.text("道友正在探索秘境，分身乏术！").finish(
                    at_sender=True
                )
    await (
        UniMessage.text("进入闭关状态，如需出关，发送『 /出关 』")
        .keyboard(Button("input", "出关", text="/出关"))
        .finish(at_sender=True, fallback=FallbackStrategy.ignore)
    )


@out_closing.handle()
async def _(event: Event, user: UserInfo, session: async_scoped_session):
    usercd_info = await session.get(UserCD, event.get_user_id())

    if not usercd_info:
        await (
            UniMessage.text("道友现在什么都没干呢~")
            .keyboard(Button("input", "闭关", text="/闭关"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    elif usercd_info.status == UserStatus.MEDITATING:
        # TODO
        ...
    else:
        match usercd_info.status:
            case UserStatus.WORKING:
                await UniMessage.text("道友正在做悬赏令呢，分身乏术！").finish(
                    at_sender=True
                )
            case UserStatus.EXPLORING:
                await UniMessage.text("道友正在探索秘境，分身乏术！").finish(
                    at_sender=True
                )
