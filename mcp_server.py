# -*- coding: utf-8 -*-
import sys, json
from client import GenParkQuantConcentratedLiquidityTickOptimizer

optimizer = GenParkQuantConcentratedLiquidityTickOptimizer()

def run_tool(name, args):
    if name == "compute_optimal_range":
        price = float(args.get("current_price", 3000.0))
        vol = float(args.get("annualized_volatility", 0.65))
        days = float(args.get("horizon_days", 14.0))
        conf = float(args.get("confidence", 0.95))
        fee = float(args.get("fee_tier", 0.003))
        return optimizer.compute_optimal_range(price, vol, days, conf, fee)
    elif name == "price_to_tick":
        price = float(args.get("price", 1.0))
        return {"tick": optimizer.price_to_tick(price)}
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark Concentrated Liquidity Optimizer Self-Test...")
        res = optimizer.compute_optimal_range(3000.0, 0.50, 7.0)
        assert res["optimal_tick_lower"] < res["current_tick"] < res["optimal_tick_upper"]
        assert res["capital_efficiency_multiplier"] > 1.0
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
