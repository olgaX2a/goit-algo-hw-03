import random

def get_numbers_ticket(min, max, quantity):
    empty_list = list()
    # check arguments
    if min < 1 or max > 1000 or max <= min or quantity < 1: 
        return empty_list

    # generate list of possible numbers
    possible_numbers = list(range(min, max + 1, 1))

    # check if quantity not more than possible numbers
    quantity_limit = len(possible_numbers)
    if quantity > quantity_limit:
        return empty_list

    winning_numbers = random.sample(possible_numbers, quantity)
    winning_numbers.sort()

    return winning_numbers
