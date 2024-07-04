from datetime import datetime, timedelta


users = [
    {"name": "Lewis Hamilton", "birthday": "1985.07.03"},
    {"name": "Lando Norris", "birthday": "1990.07.05"},
    {"name": "Max Verstappen", "birthday": "1990.07.06"},
    {"name": "George Russel", "birthday": "1990.07.07"},
    {"name": "Valterri Bott", "birthday": "1990.07.30"},
]



def get_upcoming_birthdays(users):
    
    """Function to get the list of upcoming birthdays within the next 7 days.
    If a birthday falls on a weekend, the congratulation date is moved to the next Monday."""
    
    result = []
    #Get the current date
    current_day = datetime.today().date()


    for user in users:
        # Convert birthday string to a datetime object and replace the year with the current year
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=current_day.year)
        if birthday > current_day and birthday - current_day <= timedelta(days=7):
            #If birthday falls on weekend, adjust the date
            if birthday.weekday() == 5:
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:
                birthday += timedelta(days=1)
                
            # Create a list with the user's name and the congratulation date
            birthday_user = {
                "name": user["name"],
                "congratulation_date": datetime.strftime(birthday, "%Y.%m.%d"),
                }
            #Add to the result list
            result.append(birthday_user)
    return result 

#List of upcoming birthdays
upcoming_birthdays = get_upcoming_birthdays(users)
print("Lisy of birthdays congrats this week:", upcoming_birthdays)
 