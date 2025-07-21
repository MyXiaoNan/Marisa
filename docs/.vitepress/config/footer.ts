import type { FooterData } from '@theojs/lumen'

export const footer: FooterData = {
  author: { name: 'Komorebi', link: 'https://github.com/KomoriDev' },
  group: [
    {
      title: '框架',
      icon: 'fa-solid fa-lightbulb',
      links: [
        { name: 'NoneBot', link: 'https://nonebot.dev' },
        { name: 'Alconna', link: 'https://github.com/nonebot/plugin-alconna' },
      ]
    },
    {
      title: '工具',
      icon: 'fa-solid fa-puzzle-piece',
      links: [
        { name: '可视化管理工具', link: '#' },
      ]
    },
    {
      title: '社区',
      icon: 'fa-solid fa-expand',
      links: [
        { name: '官方 企鹅 社区', link: 'https://qm.qq.com/q/D4HghuhbVe' },
        { name: '赞助', link: 'https://afdian.com/@komoridev' },
        // { name: '官方 Telegram 社区', href: '#' },
      ]
    }
  ]
}
