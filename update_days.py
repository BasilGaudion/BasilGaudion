from datetime import datetime

# Get the current date
now = datetime.now()

# Calculate the number of days until the end of the year
days_left = 365 - int(now.strftime("%j"))

# Read the README file
with open("README.md", "r") as file:
    lines = file.readlines()

# Update the line that contains the number of days left
for i, line in enumerate(lines):
    if "Days left until the end of the year:" in line:
        lines[i] = f"Days left until the end of the year: {days_left}\n"

# Write the updated lines back to the README
with open("README.md", "w") as file:
    file.writelines(lines)
