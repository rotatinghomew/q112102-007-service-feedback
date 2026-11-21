# 回访可比性与流程核查：资料契约

同一服务的邀请对象以 `invite` 为标识；重填以最后一份未作废有效答卷为准。问答是 1–5 有序分数，`anchors` 仅列问卷主管认为有机会比较的题对，判断粒度是 `service`、`old_form`、`new_form` 和 `dimension`。桥接问卷以同一个服务对象的两次回答为一对，`intervening_service=1` 排除；窗口按日数计，包含两端。桥接支持量按不同受访者计。对于题对，政策给出平均配对新减旧分差上限的绝对值及 `max_opposite_share`：非零差值中少数方向占比的上限（全零时记零）；零不倒填正负。相同维度若有多个有效锚题但所支持的分差方向冲突（正负并存），不得拿平均掩盖。
`review_policy` 给出核心维度与最小可行动降幅（分数）、最低应答覆盖比例。缺答可在有效量表边界内界定；区间跨过行动门槛时标明待补证，不假设随机不答。流程事实 `delay` 或 `unfinished` 是独立于问卷的异常支持，`none` 无支持。`contact` 是居民允许再邀的用途（`bridge`、`follow`、`both`、`none`）；`review_log` 已立项事项以 `service`、`period` 为同一核查对象。桥接的作废时间用于区分前后证据。

## 输入表

- `invites.csv`：`invite`、`person`、`service`、`period`、`form`、`contact`、`status`
- `answers.csv`：`invite`、`item`、`score`、`at`
- `anchors.csv`：`service`、`old_form`、`new_form`、`dimension`、`old_item`、`new_item`
- `bridge.csv`：`id`、`person`、`service`、`old_item`、`new_item`、`old_score`、`new_score`、`days`、`intervening_service`、`void_at`
- `bridge_policy.csv`：`service`、`min_pairs`、`window_days`、`max_abs_mean_diff`、`max_opposite_share`
- `review_policy.csv`：`service`、`dimension`、`drop`、`min_response`、`contact_slots`
- `service_events.csv`：`invite`、`fact`、`at`
- `review_log.csv`：`id`、`service`、`period`、`state`、`at`、`evidence`
