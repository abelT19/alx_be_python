# explore_datetime.py
# Objective: Familiarize yourself with Python’s datetime module

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date, days_to_add):
    # Save the future date by adding timedelta
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)
    return future_date

# Main program
if __name__ == "__main__":
    # Display current date and time
    current_date = display_current_datetime()

    # Ask the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input! Please enter an integer.")
