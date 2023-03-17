def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)
 
# Driver Code
def day_of_week():
    day = dayofweek(17, 5, 2023)
    if day == 1:print("Monday")
    elif day == 2:print("Tuesday")
    elif day == 3:print("Wednesday")
    elif day == 4:print("Thursday")
    elif day == 5:print("Friday")
    elif day == 6:print("Saturday")
    elif day == 0:print("Sunday")
    
day_of_week()