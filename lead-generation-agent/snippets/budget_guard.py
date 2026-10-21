"""Simplified example written for this showcase (not the production code).

A monthly budget guard: warn at 80 percent of the budget, stop at 100 percent.
"""
from dataclasses import dataclass


@dataclass
class BudgetGuard:
    monthly_budget_usd: float
    spent_usd: float = 0.0

    def record(self, usd: float) -> None:
        self.spent_usd += usd

    def status(self) -> str:
        if self.spent_usd >= self.monthly_budget_usd:
            return "STOP"
        if self.spent_usd >= 0.8 * self.monthly_budget_usd:
            return "WARN"
        return "OK"


if __name__ == "__main__":
    guard = BudgetGuard(monthly_budget_usd=40.0)
    guard.record(33.0)
    print(guard.status())   # WARN
