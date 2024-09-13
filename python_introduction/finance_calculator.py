# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))  # User input for income
# Prompt the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))  # User input for expenses
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05
# Projected savings after one year, incorporating the interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)
# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
