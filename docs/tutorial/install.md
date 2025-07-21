# 安装

<div class="tip custom-block" style="padding-top: 8px">

只是想了解功能吗？跳至 [插件](./) 部分.

</div>

## 环境准备

> [!IMPORTANT]
请确保你的 Python 版本 >= 3.10

为了让 Marisa 稳定运行，我们使用了包管理器 [PDM](https://github.com/pdm-project/pdm)

```bash
# 安装 pipx
pip install pipx
# 安装 PDM 包管理器
pipx install pdm
# 安装项目依赖
pdm install
```

## 本体准备

### 使用 nb-cli 安装 <Badge type="warning" text="WIP" />

```bash
nb marisa install
```

### 使用 git 下载

在任意你喜欢的目录下键入：

::: code-group

```bash [HTTPS]
git clone https://github.com/MyXiaoNan/Marisa.git
```

```bash [SSH]
git clone git@github.com:MyXiaoNan/Marisa.git
```

```bash [Github CLI]
gh repo clone MyXiaoNan/Marisa
```

:::

### 其它方法

[![Download](/download.svg)](https://github.com/MyXiaoNan/Marisa/archive/refs/heads/master.zip)
