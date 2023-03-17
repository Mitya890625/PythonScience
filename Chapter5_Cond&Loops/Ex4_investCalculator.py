def annual(inv, i_r, n_y):
    for i in range(n_y):
        bonus = inv * i_r
        inv = inv + bonus
    print(f'{inv:.2f}')
def monthly(inv, i_r, n_y):
    for i in range(n_y*12):
        bonus = inv * (i_r/12)
        inv = inv + bonus
    print(f'{inv:.2f}')    
def daily(inv, i_r, n_y):
    for i in range(n_y*365):
        bonus = inv * (i_r/365)
        inv = inv + bonus
    print(f'{inv:.2f}') 
invest = input("Enter amount of money to invest: ")
invest = int(invest.replace('$', ''))
interest_rate = input("Choose interest rate: ")
interest_rate = int(interest_rate.replace('%', ''))/100
number_of_years = int(input("Enter period of time of the investment (in years): "))

annual(invest, interest_rate, number_of_years)
monthly(invest, interest_rate, number_of_years)
daily(invest, interest_rate, number_of_years)