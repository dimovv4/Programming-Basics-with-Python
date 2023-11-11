score = int(input())

bonus_score = 0

if score <= 100:
    bonus_score += 5

elif score > 1000:
    bonus_score += (score * 10) / 100
elif score >= 100 and score <= 1000:
    bonus_score += (score * 20) / 100

if score % 2 == 0:
    bonus_score += 1
if score % 10 == 5:
    bonus_score = bonus_score + 2

all_score = score + bonus_score
print(bonus_score)
print(all_score)
