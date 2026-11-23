# 巡游导向试点资料

该项目收集文化活动试点运行数据，供运营人员检查不同场次的路线安排。`data/observations.json` 是可直接阅读的合成资料，包含场次分配、导向牌状态、路段、匿名行程和观察中断。`group_id` 标识预先分配的场次组，`event_id` 标识一条业务记录。路线容量按场次时段记录，行程中的入口字段不表示该游客只看见对应入口的牌。

`data/trial-rounds.json` 补充三轮分场次分配及逐行程观测。分配以场次入口为单位，重复扫描以同一 `traveler` 关联，`parent_allocation` 是已确认的原分配。共享窄口的人数上限按时窗记录。已签延伸安排与待议申请使用相同编号体系。

要求 Python 3.11 或更新版本。运行基线检查可使用 `python3 -m unittest discover -s tests`。`src/records.py` 提供基础 JSON 资料读取能力。
