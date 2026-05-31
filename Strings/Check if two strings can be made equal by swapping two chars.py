s1 = "bank"
s2 = "kanb"

mismatch_count = 0
mis_lst =[]
# i = j = 0
# while i < len(s1) and j < len(s2):
#     if s1[i] != s2[j]:
#         mismatch_count += 1
#         mis_lst.append(i)
#     i += 1
#     j += 1

## using for loop 
for i in range(0,len(s1)):
    if s1[i] != s2[i]:
        mismatch_count += 1
        mis_lst.append(i)
print(mis_lst)
print(mismatch_count)

if mismatch_count == 0:
    print("Both strings are same")
elif mismatch_count == 2:
    i,j = mis_lst
    if s1[i] == s2[j] and s1[j] == s2[i]:
        print("Both strings can be made equal")
    else:
        print("Not possible")
else:
    print("Not possible")

## TC = O(n)
## SC = O(n)

## we can make space complexity more optimized O(1) by breaking loop when 
## mismatch count becomes 2 (because after mismatch count > 2 
## the solution becomes impossible.)