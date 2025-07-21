# 开发指南

## 预备知识

Marish 是基于 NoneBot 框架，因此我们假定你已经拥有了一定的 NoneBot 和 Python 开发基础。
如果你对自己的基础不自信，可以参考下面的文档：

- [NoneBot 官方文档](https://nonebot.dev)
- [NoneBot 社区文档](https://x.none.bot)
- [现代 Python 教程](https://docs.python.org/zh-cn)

## 关于 Alconna

> [!NOTE]
Alconna 其实是 [plugin-alconna](https://github.com/nonebot/plugin-alconna) 的一个依赖，因由同一作者编写，
且支持完整的 Alconna 特性，我们习惯性的二者都称为 `Alconna`

[plugin-alconna](https://github.com/nonebot/plugin-alconna) 是一个强大的 NoneBot 命令匹配拓展插件，
支持富文本/多媒体解析，跨平台消息收发。
Marisa 的所有指令都是用其构造的，因此我们推荐你使用 Alconna 来进行插件开发。
如果你对 Alconna 不熟悉，可以查看[仓库内教程](https://github.com/nonebot/plugin-alconna/blob/master/docs.md)

## 关于 ORM

Marisa 使用 NoneBot 官方提供的插件 [plugin-orm](https://github.com/nonebot/plugin-orm) 进行数据库操作，
但数据库绝大部分内容已经完备，开发者只需掌握最基本的增删改查即可

~~但还是建议阅读一下 [文档](https://nonebot.dev/docs/2.4.0/best-practice/database/)，以了解最基本的使用方式~~
