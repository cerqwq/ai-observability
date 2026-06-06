# 👁️ AI Observability

AI可观测性工具，支持链路追踪、指标收集、日志分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 可观测性栈设计
- ⚙️ OpenTelemetry配置
- 📊 仪表板生成
- 🔍 链路追踪分析
- 📏 SLI/SLO设计
- 🔔 告警规则生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_observability import create_tools

tools = create_tools()

# 可观测性栈
stack = tools.design_observability_stack(["用户服务", "订单服务"])

# OpenTelemetry配置
otel = tools.generate_opentelemetry_config("用户服务")

# 仪表板
dashboards = tools.generate_dashboards("API服务", ["延迟", "错误率"])

# 链路追踪分析
trace = tools.analyze_trace(trace_data)

# SLI/SLO
sli_slo = tools.design_sli_slo("API服务", ["请求延迟", "错误率"])

# 告警规则
alerts = tools.generate_alerting_rules("API服务", slos)
```

## 📁 项目结构

```
ai-observability/
├── tools.py       # 可观测性工具核心
└── README.md
```

## 📄 许可证

MIT License
