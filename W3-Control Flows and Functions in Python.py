def calculate_discount(price, discount_perc):
    discounted_price = price - (price * discount_perc/100)
    if discount_perc >= 20:
        print(discounted_price)
    else: print(price)

calculate_discount(75, 25)