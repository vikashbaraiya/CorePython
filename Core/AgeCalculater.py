import datetime
from datetime import date,timedelta

bir_year =int(input('Please Enter your Birth year = '))
bir_month =int(input("Please Enter your Birth month = "))
bir_day = int(input("Please enter your Birth day = "))
current_date = date.today()
birth_date = datetime.date(bir_year,bir_month,bir_day,)
age = (current_date.year-birth_date.year ) - ((current_date.month , current_date.day) > (birth_date.month,birth_date.day))
print(age,"year")