# Друге завдання

import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <= 1000 and quantity <= max - min:
        numbers = random.sample(range(min, max + 1), quantity)
        return sorted(numbers)
    
    else:
        numbers = []
        return numbers


lottery_numbers = get_numbers_ticket(10, 15, 5)
print("Ваші лотерейні числа:", lottery_numbers)

