#!/usr/bin/env python3
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

@dataclass
class LoanData:
    start_date: datetime
    end_date: datetime
    loan_amount: float
    loan_currency_str: str
    base_interest_rate: float
    margin: float

    @property
    def total_interest_rate(self):
        return self.base_interest_rate + self.margin

class Application:

    def __init__(self):
        self.loans_history: List[LoanData] = []

    def run(self):
        self.welcome()
        self.prompt()


if __name__ == "__main__":

    app = Application()
    app.run()
