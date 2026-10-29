# -*- coding: utf-8 -*-
from client import GenParkQuantConcentratedLiquidityTickOptimizer

def main():
    optimizer = GenParkQuantConcentratedLiquidityTickOptimizer()
    print("=== GenPark Quant Concentrated Liquidity Tick Optimizer ===")

    # ETH/USDC pool: Current ETH = $3200, Volatility = 65%, Horizon = 10 days
    res = optimizer.compute_optimal_range(
        current_price=3200.0,
        annualized_volatility=0.65,
        horizon_days=10.0,
        confidence=0.95
    )
    print(f"Current ETH Price: ${res['current_price']} (Tick {res['current_tick']})")
    print(f"Optimal Range (95% Conf, 10d): ${res['price_lower']} - ${res['price_upper']}")
    print(f"Tick Boundaries: [{res['optimal_tick_lower']}, {res['optimal_tick_upper']}]")
    print(f"Capital Efficiency Multiplier: {res['capital_efficiency_multiplier']}x")
    print(f"Max IL at Boundary: {res['expected_il_at_upper_pct']}%")

if __name__ == "__main__":
    main()
