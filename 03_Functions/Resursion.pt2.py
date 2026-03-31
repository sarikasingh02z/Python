#Write a recursive function max_depth(nested_list) that returns the maximum nesting depth of a nested list.
def max_depth(nested_list):
    if not isinstance(nested_list, list):
        return 0
    
    if not nested_list:
        return 1
    
    max_child_depth = 0
    for item in nested_list:
        depth = max_depth(item)
        if depth > max_child_depth:
            max_child_depth = depth
    
    return 1 + max_child_depth

print(max_depth([1, 2, 3]))             
print(max_depth([1, [2, 3], 4]))         
print(max_depth([1, [2, [3, 4], 5], 6])) 
print(max_depth([[[[1]]]])) 

#Write a recursive function combinations(nums, k) that returns all combinations of length k from the list nums.
def combinations(nums, k):
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()  # Backtrack
    
    result = []
    backtrack(0, [])
    return result

print(combinations([1, 2, 3, 4], 2))

#Write a recursive function permutations(nums) that returns all possible permutations of a list of numbers.
def permutations(nums):
    if len(nums) <= 1:
        return [nums]
    
    result = []
    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i] + nums[i+1:]
        for perm in permutations(remaining):
            result.append([current] + perm)
    return result

print(permutations([1, 2, 3]))

#Write a recursive function binary_search(arr, target, left, right) that returns the index of target in a sorted list, or -1 if not found.
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(arr, 7, 0, len(arr) - 1))   
print(binary_search(arr, 10, 0, len(arr) - 1)) 

#Write a recursive function hanoi(n, source, target, auxiliary) that prints the steps to move n disks from source to target using auxiliary. Each step should say "Move disk from X to Y".
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk from {source} to {target}")
        return
    
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
