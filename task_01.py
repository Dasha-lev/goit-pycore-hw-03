
from datetime import datetime

#Create function get_days_from_today(date)
def get_days_from_today(date):
    #Revert  data string to date in the format 'YYYY-MM-DD' to object datetime
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    #Get current date
    current_date = datetime.now().date()
    #Calculate the difference between current date and given date
    difference = current_date - given_date
    return difference.days
#Result
result = get_days_from_today("2021-10-09")
print(result)






