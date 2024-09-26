# daily_reminder.py

def main():
    # Prompt for a Single Task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the Task Based on Priority and Time Sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Priority level not recognized."

    # Modify the reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Provide a Customized Reminder
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()
