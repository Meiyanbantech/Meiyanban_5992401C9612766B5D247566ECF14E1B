def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Get user input for the year
year = int(input("Enter a year: "))

# Check if it's a leap year using the function
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
