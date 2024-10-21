# Simple Interest Calculator

Simple python cli program to calculate the simple interest on a set of loans

The program can be run simply via:

```console
$ ./simple_interest.py
```

It requires the installation of dependencies listed in `requirements.txt` first (used simply for aesthetic purposes)
```console
$ pip install -r requirements.txt
```

# Running

The program allows you to add/update/list simple loans

On first run you will be prompted to input some loan data

Once input, the daily interest acrual of that loan in the given loan period will be shown in a table.
Once that is done, a new loan can be added, existing loan details can be edited, or an overview of all loans can be printed.

To quit, simply input "q" when prompted for input in the overview

# Example:

```console
 ____   _                    _         _                            ___         _                           _   
/ ___| (_) _ __ ___   _ __  | |  ___  | |      ___    __ _  _ __   |_ _| _ __  | |_   ___  _ __   ___  ___ | |_ 
\___ \ | || '_ ` _ \ | '_ \ | | / _ \ | |     / _ \  / _` || '_ \   | | | '_ \ | __| / _ \| '__| / _ \/ __|| __|
 ___) || || | | | | || |_) || ||  __/ | |___ | (_) || (_| || | | |  | | | | | || |_ |  __/| |   |  __/\__ \| |_ 
|____/ |_||_| |_| |_|| .__/ |_| \___| |_____| \___/  \__,_||_| |_| |___||_| |_| \__| \___||_|    \___||___/ \__|
                     |_|                                                                                        

Enter the loan amount: 1000 
Input the currency: £
Input the base interest rate (as a percentage): 5
Input the margin (as a percentage): 1
Input the start date (dd-MM-YYYY): 21-20-2024
'21-20-2024' could not be parsed to a date, try again!
Input the start date (dd-MM-YYYY): 21-10-2024
Input the end date (dd-MM-YYYY): 21-11-2024
+-------------+----------------+----------------------------+----------------+----------------+
| Acrual Date | # Days Elapsed | Daily Interest (No Margin) | Daily Interest | Total Interest |
+-------------+----------------+----------------------------+----------------+----------------+
|  21/10/2024 |       0        |           £0.14            |     £0.16      |     £0.16      |
|  22/10/2024 |       1        |           £0.14            |     £0.16      |     £0.33      |
|  23/10/2024 |       2        |           £0.14            |     £0.16      |     £0.49      |
|  24/10/2024 |       3        |           £0.14            |     £0.16      |     £0.66      |
|  25/10/2024 |       4        |           £0.14            |     £0.16      |     £0.82      |
|  26/10/2024 |       5        |           £0.14            |     £0.16      |     £0.99      |
|  27/10/2024 |       6        |           £0.14            |     £0.16      |     £1.15      |
|  28/10/2024 |       7        |           £0.14            |     £0.16      |     £1.32      |
|  29/10/2024 |       8        |           £0.14            |     £0.16      |     £1.48      |
|  30/10/2024 |       9        |           £0.14            |     £0.16      |     £1.64      |
|  31/10/2024 |       10       |           £0.14            |     £0.16      |     £1.81      |
|  01/11/2024 |       11       |           £0.14            |     £0.16      |     £1.97      |
|  02/11/2024 |       12       |           £0.14            |     £0.16      |     £2.14      |
|  03/11/2024 |       13       |           £0.14            |     £0.16      |     £2.30      |
|  04/11/2024 |       14       |           £0.14            |     £0.16      |     £2.47      |
|  05/11/2024 |       15       |           £0.14            |     £0.16      |     £2.63      |
|  06/11/2024 |       16       |           £0.14            |     £0.16      |     £2.79      |
|  07/11/2024 |       17       |           £0.14            |     £0.16      |     £2.96      |
|  08/11/2024 |       18       |           £0.14            |     £0.16      |     £3.12      |
|  09/11/2024 |       19       |           £0.14            |     £0.16      |     £3.29      |
|  10/11/2024 |       20       |           £0.14            |     £0.16      |     £3.45      |
|  11/11/2024 |       21       |           £0.14            |     £0.16      |     £3.62      |
|  12/11/2024 |       22       |           £0.14            |     £0.16      |     £3.78      |
|  13/11/2024 |       23       |           £0.14            |     £0.16      |     £3.95      |
|  14/11/2024 |       24       |           £0.14            |     £0.16      |     £4.11      |
|  15/11/2024 |       25       |           £0.14            |     £0.16      |     £4.27      |
|  16/11/2024 |       26       |           £0.14            |     £0.16      |     £4.44      |
|  17/11/2024 |       27       |           £0.14            |     £0.16      |     £4.60      |
|  18/11/2024 |       28       |           £0.14            |     £0.16      |     £4.77      |
|  19/11/2024 |       29       |           £0.14            |     £0.16      |     £4.93      |
|  20/11/2024 |       30       |           £0.14            |     £0.16      |     £5.10      |
+-------------+----------------+----------------------------+----------------+----------------+

To add a loan: a
To update an entry: u
To list history: l
Quit: q
a/u/l/q: a
Enter the loan amount: 100
Input the currency: €
Input the base interest rate (as a percentage): 1
Input the margin (as a percentage): 0
Input the start date (dd-MM-YYYY): 01-01-1987
Input the end date (dd-MM-YYYY): 10-01-1987
+-------------+----------------+----------------------------+----------------+----------------+
| Acrual Date | # Days Elapsed | Daily Interest (No Margin) | Daily Interest | Total Interest |
+-------------+----------------+----------------------------+----------------+----------------+
|  01/01/1987 |       0        |           €0.00            |     €0.00      |     €0.00      |
|  02/01/1987 |       1        |           €0.00            |     €0.00      |     €0.01      |
|  03/01/1987 |       2        |           €0.00            |     €0.00      |     €0.01      |
|  04/01/1987 |       3        |           €0.00            |     €0.00      |     €0.01      |
|  05/01/1987 |       4        |           €0.00            |     €0.00      |     €0.01      |
|  06/01/1987 |       5        |           €0.00            |     €0.00      |     €0.02      |
|  07/01/1987 |       6        |           €0.00            |     €0.00      |     €0.02      |
|  08/01/1987 |       7        |           €0.00            |     €0.00      |     €0.02      |
|  09/01/1987 |       8        |           €0.00            |     €0.00      |     €0.02      |
+-------------+----------------+----------------------------+----------------+----------------+

To add a loan: a
To update an entry: u
To list history: l
Quit: q
a/u/l/q: q
```