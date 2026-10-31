---
name: genpark-quant-concentrated-liquidity-tick-optimizer-skill
description: Quant concentrated liquidity tick optimizer for Uniswap v3/v4 pools balancing fee APY against impermanent loss given asset volatility.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'compute_optimal_range', 'description': 'Compute optimal tick and price range for concentrated LP positions.'}
  - {'name': 'price_to_tick', 'description': 'Convert discrete asset price to exact Uniswap tick index.'}
---

# Genpark Quant Concentrated Liquidity Tick Optimizer Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Quant Concentrated Liquidity Tick Optimizer Skill**.
Your primary directive is to execute: Quant concentrated liquidity tick optimizer for Uniswap v3/v4 pools balancing fee APY against impermanent loss given asset volatility.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'compute_optimal_range', 'description': 'Compute optimal tick and price range for concentrated LP positions.'}`
- `{'name': 'price_to_tick', 'description': 'Convert discrete asset price to exact Uniswap tick index.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'compute_optimal_range', 'description': 'Compute optimal tick and price range for concentrated LP positions.'}`
- `{'name': 'price_to_tick', 'description': 'Convert discrete asset price to exact Uniswap tick index.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
