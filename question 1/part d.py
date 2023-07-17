from datetime import datetime, timedelta

# Define the starting date
start_date = datetime(2022, 9, 17)

# Calculate the date before 74 days and 5 hours
new_date = start_date - timedelta(days=74, hours=5)

# Print the result
print("Date before 74 days and 5 hours:", new_date)