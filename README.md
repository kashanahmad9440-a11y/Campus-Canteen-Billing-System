# Campus Canteen Billing System

A beginner-friendly Python console application that calculates customer bills for a fictional campus canteen.

## Features

- Displays four menu items with their prices.
- Accepts multiple orders.
- Calculates the price of each order.
- Tracks the total quantity of items.
- Applies a 10% discount when the subtotal is PKR 1,000 or more.
- Displays the subtotal, discount, and final bill.
- Handles invalid menu choices and non-positive quantities.

## Menu

| Choice | Item | Price |
|---|---|---:|
| 1 | Tea | PKR 80 |
| 2 | Sandwich | PKR 250 |
| 3 | Juice | PKR 150 |
| 4 | Coffee | PKR 180 |
| 0 | Checkout | — |

## Discount Rule

Customers receive a 10% discount when the subtotal is PKR 1,000 or more.

## Requirements

- Python 3
- No additional packages required

## How to Run

1. Open this folder in VS Code.
2. Open the terminal.
3. Run:

   ```bash
   py billing.py
   ```

   If `py` is unavailable, try `python billing.py`.

4. Select a menu item and enter a whole-number quantity.
5. Enter `0` to finish ordering and display the final bill.

## Python Concepts Used

- Variables
- `print()` and `input()`
- Integer conversion using `int()`
- Arithmetic operators
- `if`, `elif`, and `else`
- `while` loops
- `break` and `continue`
- f-strings

## Project Structure

```text
canteen-billing/
├── billing.py
└── README.md
```

## Project Information

Created as a beginner Python practice project for learning programming fundamentals.
