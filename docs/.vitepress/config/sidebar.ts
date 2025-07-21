const tutorial = [
  {
    text: "开始",
    items: [
      { text: '介绍', link: '/tutorial/intro.md' },
      { text: '安装', link: '/tutorial/install.md' },
    ]
  }
]

const guide = [
  {
    text: "",
    items: [
      { text: '总览', link: '/guide/' },
    ]
  },
  {
    text: "相关",
    items: [
      { text: '术语', link: '/guide/glossary.md' },
    ]
  }
]

const about = [
  {
    text: "关于",
    items: [
      { text: '参与讨论', link: '/about/contact.md' },
    ]
  },
  {
    text: "更新",
    items: [
      { text: '更新日志', link: 'https://github.com/MyXiaoNan/Marisa/releases' },
      { text: '从低版本迁移', link: '/about/upgrade.md' },
    ]
  },
  {
    text: "贡献",
    items: [
      { text: '项目结构', link: '/about/structure.md' },
      { text: '贡献指南', link: 'https://github.com/MyXiaoNan/Marisa/blob/master/.github/CONTRIBUTING.md' },
    ]
  }
]


export default {
  "/tutorial/": tutorial,
  "/guide/": guide,
  "/about/": about
}
