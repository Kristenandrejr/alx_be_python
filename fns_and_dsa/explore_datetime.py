from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))  # Prompt for input
        future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format as "YYYY-MM-DD"
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid number of days.")  # Handle invalid input

# Main function to execute both parts
def main():
    display_current_datetime()  # Part 1
    calculate_future_date()     # Part 2

if __name__ == "__main__":
    main()
