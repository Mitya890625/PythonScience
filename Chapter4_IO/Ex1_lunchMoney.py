total_amount_of_money = float(input("How much money (in dollars) in your launch account"))
current_day = float(input("What day of the month is today?"))
number_of_days = float(input("How many days in this month?"))
daily_allowance = total_amount_of_money / (number_of_days - current_day)
print("You can spend ${0:0.3f} each day for the rest of the month".format(daily_allowance))