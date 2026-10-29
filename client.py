# -*- coding: utf-8 -*-
"""
GenPark Quant Concentrated Liquidity Tick Optimizer
Standard Library only: math, typing.
Computes optimal tick boundaries for Uniswap v3/v4 pools balancing fee APY
against impermanent loss given asset volatility, time horizon, and confidence level.
"""

import math
from typing import Dict, Any

class GenParkQuantConcentratedLiquidityTickOptimizer:
    TICK_BASE = 1.0001

    def price_to_tick(self, price: float) -> int:
        if price <= 0: raise ValueError("Price must be > 0")
        return int(round(math.log(price) / math.log(self.TICK_BASE)))

    def tick_to_price(self, tick: int) -> float:
        return self.TICK_BASE ** tick

    def compute_optimal_range(self, current_price: float, annualized_volatility: float,
                              horizon_days: float = 14.0, confidence: float = 0.95,
                              fee_tier: float = 0.003) -> Dict[str, Any]:
        """
        Calculates optimal [P_lower, P_upper] and tick boundaries given volatility.
        """
        if current_price <= 0 or annualized_volatility <= 0:
            raise ValueError("Price and volatility must be positive")

        t_years = horizon_days / 365.25

        # Normal critical value approximation (e.g., 0.95 -> 1.96, 0.90 -> 1.645)
        z = 1.96 if confidence >= 0.95 else (1.645 if confidence >= 0.90 else 1.28)

        sigma_t = annualized_volatility * math.sqrt(t_years)
        p_lower = current_price * math.exp(-z * sigma_t)
        p_upper = current_price * math.exp(z * sigma_t)

        tick_current = self.price_to_tick(current_price)
        tick_lower = self.price_to_tick(p_lower)
        tick_upper = self.price_to_tick(p_upper)

        # Capital efficiency multiplier vs full range: 1 / (1 - sqrt(p_lower / p_upper))
        ratio = math.sqrt(p_lower / p_upper)
        multiplier = round(1.0 / max(0.01, (1.0 - ratio)), 2)

        # Impermanent loss at boundaries
        k_upper = p_upper / current_price
        il_upper_pct = round(((2.0 * math.sqrt(k_upper) / (1.0 + k_upper)) - 1.0) * 100, 2)

        k_lower = p_lower / current_price
        il_lower_pct = round(((2.0 * math.sqrt(k_lower) / (1.0 + k_lower)) - 1.0) * 100, 2)

        return {
            "current_price": current_price,
            "current_tick": tick_current,
            "optimal_tick_lower": tick_lower,
            "optimal_tick_upper": tick_upper,
            "price_lower": round(p_lower, 4),
            "price_upper": round(p_upper, 4),
            "capital_efficiency_multiplier": multiplier,
            "horizon_days": horizon_days,
            "confidence_level": confidence,
            "expected_il_at_upper_pct": il_upper_pct,
            "expected_il_at_lower_pct": il_lower_pct,
            "fee_tier": fee_tier
        }
