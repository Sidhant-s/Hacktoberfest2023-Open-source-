import datetime

def is_hacktoberfest_year(year):
    # Hacktoberfest takes place in October
    october_start = datetime.date(year, 10, 1)
    october_end = datetime.date(year, 10, 31)
    
    # Check if October 1st falls on a day from Tuesday to Saturday
    if october_start.weekday() in range(1, 6):
        return october_start <= datetime.date.today() <= october_end
    else:
        return False

current_year = datetime.date.today().year

if is_hacktoberfest_year(current_year):
    print(f"{current_year} is a Hacktoberfest year!")
else:
    print(f"{current_year} is not a Hacktoberfest year.")
