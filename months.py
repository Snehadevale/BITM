'''def days_in_month(month):
    month_days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    # Check if the input month is valid
    if month in month_days:
        return month_days[month]
    else:
        return None

# Get user input for month
month_input = input("Enter a month: ")

# Get the number of days in the input month
days = days_in_month(month_input)

if days is not None:
    print(f"Number of days in {month_input}: {days}")
else:
    print("Invalid month input")'''



def days_in_month(month):
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    try:
        index = month_names.index(month.capitalize())
        return days_in_months[index]
    except ValueError:
        return None

# Get user input for month
month_input = input("Enter a month: ")

# Get the number of days in the input month
days = days_in_month(month_input)

if days is not None:
    print(f"Number of days in {month_input}: {days}")
else:
    print("Invalid month input")

