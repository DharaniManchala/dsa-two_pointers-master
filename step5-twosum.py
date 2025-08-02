def two_sum(nums,target):
    """
    Find two numbers in nums that add up to target.
    
    :param nums: List of integers
    :param target: Integer target sum
    :return: Tuple of the two numbers that add up to target, or None if no such pair exists
    """
    left=0
    right=len(nums)-1
    while left <right:
        total=nums[left]+nums[right]
        if total==target:
            return [left,right]
        elif total <target:
            left+=1
        else:
            right-=1
    return []
# # Example usage
nums = [2, 3, 4, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 3]
# timecomplexity:O(n)
# spacecomplexity:O(1)







    
    