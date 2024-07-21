import random

def get_numbers_ticket(min, max, quantity):
    # check arguments
    if min < 1: 
        raise ValueError('Minimal limit should be equal or more than 1') 
    if max > 1000:
        raise ValueError('Maximum limit should be equal or less than 1000')
    if max <= min:
        raise ValueError(f'Maximum limit should more than {min}')
    if quantity < 1:
        raise ValueError('Minimal limit should be equal or more than 1') 
    
    # generate list of possible numbers
    possible_numbers = list(range(min, max + 1, 1))

    # check if quantity not more than possible numbers
    quantity_limit = len(possible_numbers)
    if quantity > quantity_limit:
        raise ValueError(f'Quantity can`t be more than {quantity_limit}') 

    winning_numbers = random.sample(possible_numbers, quantity)
    winning_numbers.sort()

    return winning_numbers
