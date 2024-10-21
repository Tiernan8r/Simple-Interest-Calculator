#!/usr/bin/env python3
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple

import art
import prettytable


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

    def _str_start_time(self) -> str:
        return datetime.strftime(self.start_date, "%d/%m/%Y")

    def _str_end_time(self) -> str:
        return datetime.strftime(self.end_date, "%d/%m/%Y")

    # As a oneliner
    def __str__(self) -> str:

        return f"{self.loan_currency_str}{self.loan_amount:.2f} \
            @ {self.total_interest_rate}% ({self.base_interest_rate}% + {self.margin}%) \
                from {self._str_start_time()} to {self._str_end_time()}"

class Application:

    def __init__(self):
        self.loans_history: List[LoanData] = []

    def run(self):
        self.welcome()
        self.prompt()


if __name__ == "__main__":

    app = Application()
    app.run()
