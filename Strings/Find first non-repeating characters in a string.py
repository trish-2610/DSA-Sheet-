## Input : "aabbcd"
## Count : 
## a -> 2
## b -> 2
## c -> 1 ( first non repeating character (whose count is 1))
## d -> 1

s = "aabbcd"
freq = {}

for char in s:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] += 1
print(freq)

# for k,v in freq.items():
#     if v == 1:
#        print(k)
#        break

for char in s:
    if freq[char] == 1:
        print(char)
        break
