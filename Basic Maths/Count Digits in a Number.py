n = int(input("Enter number : "))

count = 0 
while n > 0:
    n = n // 10  ## removes last digit 
    count += 1

print("Digits count = ",count)

# Time Complexity
# Suppose number has d digits.
# Loop runs d times.
# Time Complexity : O(d)
# 10. Space Complexity
# O(1)
# Only one variable used.

## Edge case 
# if n == 0:
#     count = 1