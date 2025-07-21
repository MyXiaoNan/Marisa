import { defineConfig } from 'vitepress'
import nav from './nav'
import sidebar from './sidebar'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Marisa",
  description: "Marisa Docs",
  themeConfig: {
    siteTitle: 'Marisa <code class="VPBadge tip">alpha</code>',

    nav: nav,
    sidebar: sidebar,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ],

    editLink: {
      pattern: 'https://github.com/MyXiaoNan/Marisa/edit/master/docs/:path',
      text: '编辑此页面'
    },

    lastUpdated: { text: '上次更新' },
    outline: { label: '目录', level: [2, 3] },
    docFooter: { prev: '上一页', next: '下一页'},

    sidebarMenuLabel: '目录',
    returnToTopLabel: '回到顶部 ▲',

    darkModeSwitchLabel: '黑暗模式',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到黑暗模式',

    externalLinkIcon: false
  }
})
