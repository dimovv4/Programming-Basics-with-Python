tax = int(input())
sneakers_price = tax * 0.60 # sneakers_price = tax - annual * 40 / 100
basketball_kit = sneakers_price * 0.80
basketball_price = basketball_kit / 4
basketball_accessories = basketball_price / 5
total_sum = tax + sneakers_price \
            + basketball_kit + basketball_price \
            + basketball_accessories
print(total_sum)
