movie_budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())
dresses_price = number_of_statists * one_dress_price
movie_decor = movie_budget * 0.10

if number_of_statists > 150:
    dresses_price *= 90

needed_money = movie_decor + dresses_price
difference = abs(needed_money - movie_budget)
if needed_money > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} lv more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} lv left")
