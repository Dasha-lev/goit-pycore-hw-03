import re

#Create function  normalize_phone(phone_number)
def  normalize_phone(phone_number): 
     """
     Create a row in order to store the normalize number
     """ 
     normalized_number = re.sub('[^0-9,+]', '', phone_number)
    
     #If number doesn't start with '+' we should add '+38' at the beginning of the number
     if normalized_number.startswith('380'):
        normalized_number = '+' + normalized_number

     elif normalized_number.startswith('0'):
        normalized_number = '+38' + normalized_number    
     #Return normalized number
     return normalized_number

#Example of the function usage 
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# Normalize all numbers in the list
sanitized_numbers = []
for num in raw_numbers:
    sanitized_numbers.append(normalize_phone(num))

# Print the result
print("Normalized numbers for SMS:", sanitized_numbers)
