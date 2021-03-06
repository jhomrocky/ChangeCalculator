"""
This is a calculator for determining how many coins a cashier would need to return to their customer.
Not everyone's the best at math! So this can be helpful.
"""

from decimal import Decimal


def change_calc():

    customer_total = input("What was the customer's total? ")
    customer_amount_given = input("How much did the customer give you? ")
    customer_total = Decimal(customer_total)
    customer_amount_given = Decimal(customer_amount_given)

    # find the difference (total change to be provided)
    change_total = Decimal(customer_amount_given - customer_total)
    # tell user the amount they owe the customer
    print("You owe the customer: $" + str(change_total))

    # these are given +1 each time one of their values is subtracted from the change_total until the subtraction
    # goes below 0 then stops and moves on, giving an integer count of how many coins to return to the customer
    # also need to be reset for each iteration
    dollars_returned = 0
    quarters_returned = 0
    dimes_returned = 0
    nickels_returned = 0
    pennies_returned = 0
    # first check how many dollars to return
    while change_total >= 0:
        if change_total - Decimal(1.0) >= 0:
            dollars_returned += 1
            change_total -= 1.0
        else:
            if change_total - Decimal(0.25) >= 0:
                quarters_returned += 1
                change_total -= Decimal(0.25)
            else:
                if change_total - Decimal(0.1) >= 0:
                    dimes_returned += 1
                    change_total -= Decimal(0.1)
                else:
                    if change_total - Decimal(0.05) >= 0:
                        nickels_returned += 1
                        change_total -= Decimal(0.05)
                    else:
                        if change_total - Decimal(0.01) > 0:
                            pennies_returned += 1
                            change_total -= Decimal(0.01)
                        else:
                            pennies_returned += 1
                            break

    print("You should give them %d dollars, %d quarters, %d dimes, %d nickels and"
          " %d pennies." % (dollars_returned, quarters_returned, dimes_returned, nickels_returned,
                            pennies_returned))
    user_restart = input("Do you want to do another? Y for Yes, or N for No")
    user_restart = user_restart.lower()
    if user_restart == 'y':
        change_calc()


change_calc()
