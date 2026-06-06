"""
AI Observability - AI可观测性工具
支持链路追踪、指标收集、日志分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIObservabilityTools:
    """
    AI可观测性工具
    支持：追踪、指标、日志
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_observability_stack(self, services: List[str]) -> Dict:
        """设计可观测性栈"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        services_text = ", ".join(services)

        prompt = f"""请为{services_text}设计可观测性栈：

请返回JSON格式：
{{
    "tracing": "链路追踪方案",
    "metrics": "指标收集方案",
    "logging": "日志收集方案",
    "correlation": "关联方案",
    "tools": ["推荐工具"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"observability": content}

    def generate_opentelemetry_config(self, service: str) -> str:
        """生成OpenTelemetry配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{service}生成OpenTelemetry配置：

要求：
1. Tracing配置
2. Metrics配置
3. Logging配置
4. Exporter配置"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_dashboards(self, service: str, metrics: List[str]) -> Dict:
        """生成仪表板"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = ", ".join(metrics)

        prompt = f"""请为{service}生成仪表板：

指标：{metrics_text}

请返回JSON格式：
{{
    "dashboards": [
        {{"name": "仪表板名", "panels": [{{"title": "标题", "type": "类型", "query": "查询"}}]}}
    ],
    "alerts": ["告警规则"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"dashboards": content}

    def analyze_trace(self, trace_data: Dict) -> Dict:
        """分析链路追踪"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        trace_text = json.dumps(trace_data, ensure_ascii=False)

        prompt = f"""请分析以下链路追踪数据：

{trace_text}

请返回JSON格式：
{{
    "summary": "总结",
    "bottlenecks": ["瓶颈"],
    "errors": ["错误"],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"trace_analysis": content}

    def design_sli_slo(self, service: str, critical_paths: List[str]) -> Dict:
        """设计SLI/SLO"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        paths_text = ", ".join(critical_paths)

        prompt = f"""请为{service}设计SLI/SLO：

关键路径：{paths_text}

请返回JSON格式：
{{
    "slis": [
        {{"name": "SLI名", "description": "描述", "measurement": "测量方式"}}
    ],
    "slos": [
        {{"name": "SLO名", "target": "目标", "window": "时间窗口"}}
    ],
    "error_budget": "错误预算策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"sli_slo": content}

    def generate_alerting_rules(self, service: str, slos: List[Dict]) -> str:
        """生成告警规则"""
        if not self.client:
            return "LLM客户端未配置"

        slos_text = json.dumps(slos, ensure_ascii=False)

        prompt = f"""请为{service}生成告警规则：

SLO：{slos_text}

要求：
1. 多级告警
2. 静默规则
3. 升级策略"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIObservabilityTools:
    """创建可观测性工具"""
    return AIObservabilityTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Observability Tools")
    print()

    # 测试
    stack = tools.design_observability_stack(["用户服务", "订单服务"])
    print(json.dumps(stack, ensure_ascii=False, indent=2))
