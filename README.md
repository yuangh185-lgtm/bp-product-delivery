# bp-product-delivery

面向制造业产品交付场景的 Codex Skill，覆盖 MES、APS、PLM、PDM、IPS、ERP、OA 等系统。

它将需求、会议纪要、截图、旧版 PRD、原型、字段清单和业务规则，组织为一致、可追溯、可开发、可测试的产品交付物。

## 能力范围

- 需求提取、冲突与遗漏检查
- PRD、业务流程、泳道图、状态机和决策树
- 高保真交互原型与交互说明
- ER 模型、数据字典和 Oracle DDL
- OpenAPI / Swagger 接口契约
- 测试用例、验收标准和发布门禁
- 跨交付物一致性检查与追溯矩阵
- 完整制造业产品交付包

## 目录结构

- `SKILL.md`：Skill 主入口和编排规则
- `agents/`：Skill 展示与调用配置
- `references/`：需求、PRD、原型、数据、测试和制造业领域参考
- `assets/`：PRD、Oracle SQL、OpenAPI、测试和追溯模板
- `scripts/`：完整交付包校验脚本

## 使用方式

将本仓库作为 Skill 安装，或把仓库内容放入 Codex Skills 目录。安装后可直接提出制造业产品交付任务，例如：

> 根据这份 APS 需求和页面截图，输出需求基线、PRD、规则决策树、Oracle 表结构、OpenAPI 接口、测试用例和验收清单，并检查跨文档一致性。

Skill 会根据任务选择最小工作模式：分析、生产、审查、更新或完整交付，并维护 `REQ → RULE/FLOW/UI → DATA/API → TC → AC` 的追溯关系。

## 校验完整交付包

```bash
python3 scripts/validate_delivery.py <delivery-directory> --profile full
```

## 说明

当前版本面向 MES、APS、PLM、PDM、IPS、ERP、OA 等制造业产品交付场景。公开仓库不等于自动授予开源许可；如需对外分发或商业使用，请由仓库所有者补充合适的 LICENSE。
