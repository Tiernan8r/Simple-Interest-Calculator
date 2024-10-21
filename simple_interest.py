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

    # More legible ASCII table
    def as_table(self) -> str:
        tab = prettytable.PrettyTable()
        tab.field_names = []
        tab.add_rows(
            [
                ["Loan Currency", self.loan_currency_str],
                ["Loan Amount", self.loan_amount],
                ["Total Interest Rate (%)", self.total_interest_rate],
                ["Base Interest Rate (%)", self.base_interest_rate],
                ["Margin (%)", self.margin],
            ]
        )

        return tab.get_string()


class Application:

    def __init__(self):
        self.loans_history: List[LoanData] = []

    def welcome(self):
        art.tprint("Simple Loan Interest")

    def prompt(self):

        inp = ""

        while inp != "q":

            print()
            print("To add a loan: a")
            print("To update an entry: u")
            print("To list history: l")
            print("Quit: q")
            inp = input("a/u/l/q: ").strip().lower()

            if inp == "q":
                continue
            elif inp == "a":
                self.add_loan()
            elif inp == "u":
                self.update_loan()
            elif inp == "l":
                self.show_history()
            else:
                print(f"Unrecognised input '{inp}'\n")

    def run(self):
        self.welcome()
        self.prompt()


if __name__ == "__main__":

    app = Application()
    app.run()
