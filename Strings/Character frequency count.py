s = "madam ji"
freq = {}
for char in s:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] += 1
print(freq)

## TC = O(n)
## SC = O(n)

## Using counter 
from collections import Counter 
freq = Counter(s)
print(freq)

## Another way using get()
s = "madam"
freq = {}
for char in s:
    freq[char] = freq.get(char,0) + 1
print(freq)

## get() -> returns frequency if element exists else return 0 if not exists 
