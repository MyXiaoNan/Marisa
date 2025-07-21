// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import type { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'

import { HomeFooter } from '@theojs/lumen'
import { Announcement } from '@theojs/lumen'

import './style.css'
import './custom_sidebar.css'
import { footer as Footer_Data } from '../config/footer'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(HomeFooter, { Footer_Data }),
      'home-hero-info-before': () => h(Announcement) 
    })
  },
  enhanceApp({ app, router, siteData }) {
    // ...
  }
} satisfies Theme
