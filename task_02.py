import random

#Create get_numbers_ticket(min, max, quantity) to generate random for lotteries
def get_numbers_ticket(min: int, max: int, quantity: int):
    #Chek function params
    if min < 1 or max > 1000 or quantity > (max - min+1):
        return []
    #Create and generate unique set of numbers
    numbers = []
    while len(numbers) < quantity:
        number = random.randint(min, max)
        #Check if the number is adsence in the list and add it to the list
        if number not in numbers:
           numbers.append(number)

    #Sort the list with numbers
    numbers.sort()
    return numbers 
#Get the result
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
