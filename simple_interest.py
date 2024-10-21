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

        self.add_loan()

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


    def add_loan(self, existing_loan=None):
        # Get the loan struct
        loan = self._loan_input_prompt()

        # save it to the record
        self.loans_history.append(loan)

        # Show the interest acrual
        self.show_loan_output(loan)

    def update_loan(self):
        # Show the list of loans first
        self.show_history()
        # prompt for an index to update
        n = len(self.loans_history)
        idx = -1
        while idx < 0 or idx >= n:
            idx_str = input(
                f"Select an entry index between 0 & {n - 1} (or q to quit): "
            )
            if idx_str.lower() == "q":
                return

            try:
                idx = int(idx_str)
            except ValueError:
                print(f"'{idx_str}' is not a valid number")

        # get the existing loan struct
        loan = self.loans_history[idx]
        # prompt for updates on the values
        updated_loan = self._loan_input_prompt(loan)

        # overwrite the existing entry
        self.loans_history[idx] = updated_loan

        # show the interest acrual tabulated
        self.show_loan_output(updated_loan)

    def show_history(self):
        if len(self.loans_history) == 0:
            print("No history to show!")
            return

        tab = prettytable.PrettyTable()
        tab.field_names = ["Entry #", "Details"]
        for idx, loan in enumerate(self.loans_history):
            tab.add_row([idx, str(loan)])

        print(tab)


    def run(self):
        self.welcome()
        self.prompt()


if __name__ == "__main__":

    app = Application()
    app.run()
