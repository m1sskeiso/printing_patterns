# Function to print the pattern
def print_pattern(rows):
    for i in range(1, rows + 1):
# Print each number i, repeated i times
         print(" ".join(str(i) * i))
# Specify the number of rows
num_rows = 9

# Call the function to print the pattern
print_pattern(num_rows)

