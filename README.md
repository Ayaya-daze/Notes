# Notes

Ayaya's public notes — 物理、数学、统计课程笔记。

## 目录

| 目录 | 内容 |
|------|------|
| `Physics/Feynman III/` | 费曼物理 III (Week 1-15) |
| `Physics/Solid State Physics/` | 固体物理 (能带结构) |
| `Physics/Topics in Statistical Mechanics/` | 统计力学专题 (Lec 01-10) |
| `Math/Group Theory/` | 群论 (Chapter 1-2) |
| `Math/Stochastic Process/` | 随机过程 (DTMC, Martingale, Poisson, CTMC) |
| `others/Statistics in Astrophysics/` | 天体物理统计学 (Lec 1-13) |

## 发布

```bash
cd /Users/ayaya/Documents/server/server-pull/notes-content
git add .
git commit -m "Update notes"
git push
```

git push 到服务器后，post-receive hook 自动执行 Quartz 构建。

## 附件

- `attachments/tikz/` — TikZ 图表（PNG + 部分 .tex 源文件）
- `attachments/imagegen/` — Python 生成的图表
- `attachments/` — 其他图片资源

TikZ 图片在暗色主题下自动加暖白底背景。

## 主题

前端主题部署详见运维手册 `tmp-notes-refactor2/` 目录和 runbook 中的 Notes 主题发布章节。
