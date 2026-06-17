# 1
# 12
# 123
# 1234
# 12345

n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end="")
    print()

## OR
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
