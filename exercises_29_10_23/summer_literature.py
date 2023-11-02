pages_in_book = int(input())
pages_in_a_hour = int(input())
days_to_read = int(input())

hours_to_read = pages_in_book / pages_in_a_hour
hours_to_read2 = hours_to_read / days_to_read
print(int(hours_to_read2))
