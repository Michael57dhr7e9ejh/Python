# Calculate minute endurance on generator
print("This program calculates litres used.")

# Get the minutes used from the user
minutes_used = input("Enter minutes used:")
# Convert text entered to a
# floating point number
# The user can enter 10 here as I have converted text to a number, but the work 10 creates an error
minutes_used = float(minutes_used)

# Get litres used from the user
litres_used = input("Enter litres used:")
# Convert text entered to a
# floating point number
litres_used = float(litres_used)

# Calculate and print the answer
ltrs = minutes_used / litres_used
print("Minutes left on generator:", ltrs)