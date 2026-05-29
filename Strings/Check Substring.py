s = "Python is good"
sub = "good"
is_substring = sub in s 
print("Yes" if is_substring else "No")

# Time Complexity
# Suppose:
# main string length = n
# substring length = m
# Worst-case searching:
# O(n⋅m)
# But Python uses optimized internal searching algorithms, so practically very fast.

# Space Complexity
# No extra major space used.
# O(1)