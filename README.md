# LOL 比赛认知库

> 用可复查的职业比赛证据，持续修正我对版本、英雄与阵容的理解。

这个仓库不是“预测必胜公式”，也不是按单日胜率排英雄。它把每天看比赛得到的判断写成带日期、版本、赛区、样本和反证的认知记录，最终为比赛预测系统提供可回测的候选特征。

## 三条主线

1. **每日英雄层级**：LCK、LPL 分开，覆盖上路、打野、中路、AD、辅助。
2. **每日阵容复盘**：从 BP 到胜负，分析伤害如何真正交付。
3. **逆风阵容案例库**：先收录候选案例；跨队伍、跨对手复现后才升级为 validated。

## 当前入口

- [当前版本认知总榜](tier-lists/current.md)
- [当前阵容原型分级](composition-tiers/current.md)
- [LCK 五位置逐路检验](tier-lists/roles/2026-08-13-LCK.md)
- [LPL 五位置逐路检验](tier-lists/roles/2026-08-13-LPL.md)
- [2026-08-13 每日复盘](daily/2026/08/2026-08-13.md)
- [逆风阵容案例库](comeback-comps/README.md)
- [评级与阵容分析方法](docs/methodology.md)
- [术语表](docs/glossary.md)
- [认知台账](knowledge-ledger/claims.csv)

## 我如何定义 T0

T0 不是“胜率最高”，而是当前赛区和版本下，能够显著改变 BP、较容易兑现且缺陷较难被稳定惩罚的英雄。评价至少检查：

- BP 优先级与对手是否愿意付出 ban 位；
- 盲选安全性与对线下限；
- 阵容适配范围；
- 逆风仍能提供的功能；
- 领先后的资源转化；
- 选手熟练度与赛区执行差异。

因此仓库会同时标记 `T0`、`T0.5`、`T1`、`Counter T0`、`逆风锚点`、`comfort`、`trap`，并允许某个位置暂时没有证据足够的 T0。

阵容也使用同一套语言，但评的是完整交付链而不是五个英雄的名气：当前将“多点强开 + 第二轮输出”列为基础 T0；“完整反开保排”在对上冲阵时是 Counter T0；“前后排持续 + 反开锚点”和“边线牵制 + 跨图接应”通常为 T0.5，再按 LCK/LPL 修正。

## 每日更新流程

```bash
# 1. 从模板新增当天复盘和分赛区层级快照
# 2. 更新 knowledge-ledger/claims.csv
python3 scripts/build_index.py
python3 scripts/validate.py
```

推荐顺序：先冻结赛程、patch 和 BP 数据，再写判断；先记录事实，再写推断；最后补最强反证和下一次验证条件。

## 证据边界

- 一队联赛与次级联赛分开；LCK 与 LPL 分开。
- Fearless/全局 BP 下，已使用英雄不会记为后续 ban，不能只用 ban 数代表优先级。
- 单局翻盘只是一条案例，不是“经典阵容”。
- 小样本只用于生成候选结论，不冒充因果或稳定预测增量。
- 任何准备进入预测模型的认知，都必须再做时间切分、样本外验证与市场消融。

## 声明

本仓库是个人赛事研究笔记，与 Riot Games、LCK、LPL 或参赛俱乐部无关。英雄联盟及相关名称归各自权利人所有。

<!-- generated-index:start -->
## 自动索引

### 阵容原型分级
- [当前阵容原型分级｜2026-08-13](composition-tiers/current.md)

### 每日复盘
- [每日比赛认知｜2026-08-13](daily/2026/08/2026-08-13.md)

### 五位置逐路检验
- [LPL 五位置逐路检验｜2026-08-13](tier-lists/roles/2026-08-13-LPL.md)
- [LCK 五位置逐路检验｜2026-08-13](tier-lists/roles/2026-08-13-LCK.md)

### 层级历史
- [LPL 英雄层级快照｜2026-08-13](tier-lists/history/2026-08-13-LPL.md)
- [LCK 英雄层级快照｜2026-08-13](tier-lists/history/2026-08-13-LCK.md)

### 逆风阵容候选
- [候选翻盘阵容｜WBG vs NIP G2](comeback-comps/candidates/2026-08-13-WBG-vs-NIP-G2.md)
- [候选翻盘阵容｜GEN vs HLE G1](comeback-comps/candidates/2026-08-13-GEN-vs-HLE-G1.md)
- [候选翻盘阵容｜BFXY vs KRXC G2](comeback-comps/candidates/2026-08-11-BFXY-vs-KRXC-G2.md)
<!-- generated-index:end -->
