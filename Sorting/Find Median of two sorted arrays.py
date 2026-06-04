def find_median(arr1,arr2):
    merged = arr1 + arr2 ## combining both arrays
    merged.sort() ## sorting combined array
    
    n = len(merged)

    if n % 2 == 1: ## array of odd length
        return merged[n//2]
    else: ## array of even length
        return (merged[n//2 - 1] + merged[n//2]) / 2

arr1 = [1,2,3]
arr2 = [2,4,5]
print(find_median(arr1,arr2))
