quantity_of_nylon = int(input())
quantity_of_paint = int(input())
quantity_of_thinner = int(input())
hours = int(input())
nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40            #Имаме +2, защото Румен иска да се подсигури и дава 2 кв.м. найлон.
materials = nylon_price * (quantity_of_nylon + 2)\
            + paint_price * (quantity_of_paint * 1.1)\
            + thinner_price * quantity_of_thinner \
            + bags_price
workers_payment = materials * 0.3 * hours #30/100
total_sum = workers_payment + materials
print(total_sum)

