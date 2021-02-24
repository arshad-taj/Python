import math

price = 1000000  # price of house
down_payment = None
is_buyer_good = input()
#bool(is_buyer_good)
if is_buyer_good == "True":
    down_payment = price * 10 // 100
else:
    down_payment = price * 20 // 100

print(f"The down payment is {down_payment}")

s ="asrrh"

