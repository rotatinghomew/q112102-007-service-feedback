# 数据说明

服务对象、回访邀请、反馈响应和办理核查的合成资料。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `services.csv`

字段：`service_id`、`resident_ref`、`service_code`、`completed_at`、`grid_ref`。当前演练样本 4 条。

## `invitations.csv`

字段：`invite_id`、`service_id`、`sent_at`、`delivery_state`、`survey_version`。当前演练样本 4 条。

## `responses.csv`

字段：`response_id`、`invite_id`、`received_at`、`score`、`state`、`supersedes`。当前演练样本 4 条。

## `reviews.csv`

字段：`review_id`、`service_id`、`reviewed_at`、`finding`、`source_ref`。当前演练样本 2 条。
