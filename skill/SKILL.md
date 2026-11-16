---
name: asr-repo
version: 1.0.0
description: asr_serve
trigger_conditions:
  - 需要理解、修改或排障 asr 的代码
  - 在 asr 里定位入口、数据表、对外契约或构建方式
---

# asr 仓库技能

> 由仓库实际内容生成的骨架（README/目录/模型定义/契约/构建脚本逐项取证）。新增判断与坑位请直接在下面对应小节补充。

## 定位

**asr_serve**

a local deploy ASR models web server

- 远端：`https://github.com/yumoqing/asr.git`
- 默认分支：`main`（共 2 个提交）
- 最近提交：2026-11-03 `a4b3be4` chore: 忽略构建/测试临时文件
- 规模：15 个文件；Python 5，JSON 1

## 目录结构

- `app/` — 应用级初始化 / 菜单与页面装配（6 个文件）
- `conf/` — 配置（`config.json`；密码为 AES 密文）（1 个文件）
- `files/` — 静态文件（1 个文件）
- `i18n/` — 多语言（`msg.txt` 逐行 `key: value` + `i18n.json`）（1 个文件）
- `logs/` — 1 个文件
- `plugins/` — 1 个文件
- `wwwroot/` — 前端页面与 `.dspy` 契约（服务端渲染入口）（1 个文件）
- 根文件：`.gitignore`、`README.md`、`requirements.txt`

## 构建与运行

- `requirements.txt`：1 项（openai-whisper）

## 建议阅读顺序

1. `README.md`
2. `wwwroot/`

