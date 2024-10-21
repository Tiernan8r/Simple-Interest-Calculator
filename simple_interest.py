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

    # If given a loan object, also used to update that entry...
    def _loan_input_prompt(self, existing_loan=None):

        # If given an existing loan struct, create strings to notify user of existing values that can be re-accepted
        existing_loan_amount_str = ""
        existing_currency_str = ""
        existing_base_interest_str = ""
        existing_margin_str = ""
        existing_start_str = ""
        existing_end_str = ""

        if existing_loan is not None:
            existing_loan_amount_str = (
                f" (existing = {existing_loan.loan_amount}; leave blank to accept)"
            )
            existing_currency_str = f" (existing = {existing_loan.loan_currency_str}; leave blank to accept)"
            existing_base_interest_str = f" (existing = {existing_loan.base_interest_rate}%; leave blank to accept)"
            existing_margin_str = (
                f" (existing = {existing_loan.margin}%; leave blank to accept)"
            )
            existing_start_str = f" (existing = {datetime.strftime(existing_loan.start_date, "%d-%m-%Y")}; leave blank to accept)"
            existing_end_str = f" (existing = {datetime.strftime(existing_loan.end_date, "%d-%m-%Y")}; leave blank to accept)"

        # =======================
        # Do the actual prompting
        # =======================

        # Loan Amount with type check
        while True:
            loan_amount_str = input(
                f"Enter the loan amount{existing_loan_amount_str}: "
            )
            # User can give empty input to not overwrite current value
            if not loan_amount_str and existing_loan is not None:
                loan_amount = existing_loan.loan_amount
                break

            try:
                loan_amount = float(loan_amount_str)
                break
            except ValueError:
                print(f"'{loan_amount_str}' could not be parsed as a float, try again!")

        # Currency
        curr_str = input(f"Input the currency{existing_currency_str}: ")
        if not curr_str and existing_loan is not None:
            currency = existing_loan.loan_currency_str
        else:
            currency = curr_str

        # Base interest rate with type check
        while True:
            base_interest_rate_str = input(
                f"Input the base interest rate{existing_base_interest_str} (as a percentage): "
            )

            # User can give empty input to not overwrite current value
            if not base_interest_rate_str and existing_loan is not None:
                base_interest_rate = existing_loan.base_interest_rate
                break

            try:
                base_interest_rate = int(base_interest_rate_str)
                break
            except ValueError:
                print(
                    f"'{base_interest_rate_str}' could not be parsed as an integer, try again!"
                )

        # Margin with type check
        while True:
            margin_str = input(
                f"Input the margin{existing_margin_str} (as a percentage): "
            )

            # User can give empty input to not overwrite current value
            if not margin_str and existing_loan is not None:
                margin = existing_loan.margin
                break

            try:
                margin = int(margin_str)
                break
            except ValueError:
                print(f"'{margin_str}' could not be parsed as an integer, try again!")

        # Start date with type check
        while True:
            start_date_str = input(
                f"Input the start date{existing_start_str} (dd-MM-YYYY): "
            )

            # User can give empty input to not overwrite current value
            if not start_date_str and existing_loan is not None:
                start_date = existing_loan.start_date
                break
            try:
                start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
                break
            except ValueError:
                print(f"'{start_date_str}' could not be parsed to a date, try again!")

        # End date with type check
        while True:
            end_date_str = input(f"Input the end date{existing_end_str} (dd-MM-YYYY): ")

            # User can give empty input to not overwrite current value
            if not end_date_str and existing_loan is not None:
                end_date = existing_loan.end_date
                break

            try:
                end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
                break
            except ValueError:
                print(f"'{end_date_str}' could not be parsed to a date, try again!")
        # I've assumed start date is before end date implicitly...

        loan = LoanData(
            start_date, end_date, loan_amount, currency, base_interest_rate, margin
        )

        return loan

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

    # Show tabulateddaily acrued interest between start & end date
    def show_loan_output(self, loan: LoanData):
        delta_days = (loan.end_date - loan.start_date).days

        daily_interest_no_margin = (
            loan.loan_amount * (loan.base_interest_rate / 100) / 365
        )
        daily_interest = loan.loan_amount * (loan.total_interest_rate / 100) / 365

        tab = prettytable.PrettyTable()
        tab.field_names = [
            "Acrual Date",
            "# Days Elapsed",
            "Daily Interest (No Margin)",
            "Daily Interest",
            "Total Interest",
        ]

        for day_num in range(delta_days):
            curr_date = loan.start_date + timedelta(days=day_num)

            total_interest = daily_interest * (day_num + 1)

            tab.add_row(
                [
                    datetime.strftime(curr_date, "%d/%m/%Y"),
                    day_num,
                    f"{loan.loan_currency_str}{daily_interest_no_margin:.2f}",
                    f"{loan.loan_currency_str}{daily_interest:.2f}",
                    f"{loan.loan_currency_str}{total_interest:.2f}",
                ]
            )

        print(tab)

    def run(self):
        self.welcome()
        self.prompt()


if __name__ == "__main__":

    app = Application()
    app.run()
