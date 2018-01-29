"""
This is a calculator for determining how many coins a cashier would need to return to their customer.
Not everyone's the best at math! So this can be helpful.
"""


def change_calc():
    customer_total = input("What was the customer's total? ")
    customer_amount_given = input("How much did the customer give you? ")
    customer_total = float(customer_total)
    customer_amount_given = float(customer_amount_given)

    # find the difference (total change to be provided)
    change_total = customer_amount_given - customer_total
    change_total = float(change_total)

    # these are given +1 each time one of their values is subtracted from the change_total until the subtraction
    # goes below 0 then stops and moves on
    dollars_returned = 0
    quarters_returned = 0
    dimes_returned = 0
    nickels_returned = 0
    pennies_returned = 0

    # first check how many dollars to return
    while change_total > 0:
        if change_total - 1 > 0:
            # adds one dollar to "amount to give back". process repeated for other currencies.
            # if subtracting would drop under 0, continue to next currency
            dollars_returned += 1
            change_total -= 1
    # now to check quarters, nickels, and dimes
        if change_total - .25 > 0:
            quarters_returned += 1
            change_total -= .25

        if change_total - .1 > 0:
            dimes_returned += 1
            change_total -= .1

        if change_total - .1 > 0:
            nickels_returned += 1
            change_total -= .05

        if change_total - .01 > 0:
            pennies_returned += 1
            change_total -= .01

    print("You owe the customer $%f. You should give them %d dollars, %d quarters, %d dimes, %d nickels and"
          " %d pennies." % (change_total, dollars_returned, quarters_returned, dimes_returned, nickels_returned,
                            pennies_returned))


change_calc()
