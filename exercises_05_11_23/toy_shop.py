needed_money = float(input())
puzzels = int(input())
talking_dolls = int(input())
toy_bears = int(input())
minions = int(input())
trucks = int(input())


total_price = puzzels * 2.6 \
              + talking_dolls * 3 \
              + toy_bears * 4.10  \
              + minions * 8.20  \
              + trucks * 2

total_number_of_toys = puzzels + \
                       + talking_dolls \
                       + toy_bears \
                       + minions \
                       + trucks
if total_number_of_toys >= 50:
    total_price *= 0.75
total_price *= 0.90
difference = abs(total_price - needed_money)
if total_price >= needed_money:
    print(f"Yes! {difference: .2f} lv left!")
else:
    print(f"Not enough money! {difference: .2f} lv needed ! ")
