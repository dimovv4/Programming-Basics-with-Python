chicken_orders = int(input())
fish_orders = int(input())
vegetarian_orders = int(input())
chicken_price = 10.35
fish_price = 12.40
vegetarian_price = 8.15
delivery = 2.50
total_bill = chicken_orders * chicken_price \
         + fish_orders * fish_price \
         + vegetarian_orders * vegetarian_price
desert = total_bill * 0.2
total_sum = total_bill + desert + delivery
print(total_sum)
