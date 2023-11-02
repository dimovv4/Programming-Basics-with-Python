number_of_pens = int(input())
number_of_markers = int(input())
litres_of_detergent = int(input())
discount_percent = int(input())
price_of_pens = 5.80
price_of_markers = 7.20
price_per_liter_of_detergent = 1.20
needed_sum = number_of_pens * price_of_pens \
             + number_of_markers * price_of_markers \
             + litres_of_detergent * price_per_liter_of_detergent
needed_sum = needed_sum - needed_sum * discount_percent / 100
print(needed_sum)
