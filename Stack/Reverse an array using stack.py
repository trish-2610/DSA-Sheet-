def reverse_array_using_stack(arr) -> list:
    stack = []
    for i in range(len(arr)):
        stack.append(arr[i])
    reversed_stack = []
    while stack:
        reversed_stack.append(stack.pop())
    return reversed_stack

print(reverse_array_using_stack([1,2,3,4,5]))
## commit
