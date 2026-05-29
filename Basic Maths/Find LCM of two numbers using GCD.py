## Relation between GCD and LCM
## GCD(a,b) × LCM(a,b) = a×b
## So, 
##    LCM(a,b) = (a x b) / GCD(a,b)

a = int(input("Enter a : "))
b = int(input("Enter b : "))

## Multiplication 
MUL = a * b 

## find GCD
while b != 0:
    a,b = b,a%b
GCD = a

## LCM 
LCM = MUL // GCD
print("LCM is = ",LCM)

## you can use separate variables also ( x = a , y = b )
## TC is same as GCD.
## SC is O(1) as few variables are used.