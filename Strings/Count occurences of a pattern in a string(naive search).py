text = "banana"
pattern = "ana"
k = len(pattern)
count = 0

for i in range(len(text) - k + 1):
    if text[i:i+k] == pattern: ## if text.startswith(pattern,i) -> if text starts with pattern at index i
        count += 1
print(count) 

## TC = O((n-k+1) X k) -> O(n X k)
## SC = O(1)

# Why Is It Called "Naive Search"?
# Because at every position:

# Check pattern
# Move by 1
# Check again
# Move by 1

# No optimization.
# That's why advanced algorithms like KMP and Rabin-Karp exist.