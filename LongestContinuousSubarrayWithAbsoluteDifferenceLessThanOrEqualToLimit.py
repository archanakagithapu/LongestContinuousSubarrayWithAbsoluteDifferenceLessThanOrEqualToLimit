'''

def longestSubarray(nums, limit):
    from collections import deque
    max_deque = deque()
    min_deque = deque()
    left = 0
    longest = 0
    for right, num in enumerate(nums):
        while max_deque and num > nums[max_deque[-1]]:
            max_deque.pop()
        while min_deque and num < nums[min_deque[-1]]:
            min_deque.pop()
        max_deque.append(right)
        min_deque.append(right)
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            if max_deque[0] < min_deque[0]:
                left = max(max_deque.popleft() + 1, left)
            else:
                left = max(min_deque.popleft() + 1, left)
        longest = max(longest, right - left + 1)
    return longest

nums = []
limit = int(input("Enter the limit: "))
n = int(input("Enter the number of elements: "))
for i in range(n):
    nums.append(int(input("Enter element {}: ".format(i+1))))
print(longestSubarray(nums, limit))
'''

nums = []
limit = int(input("Enter the limit: "))
n = int(input("Enter the number of elements: "))
for i in range(n):
    nums.append(int(input("Enter element {}: ".format(i+1))))
left = 0
longest = 0
max_val = min_val = nums[0]
for right in range(len(nums)):
    max_val = max(max_val, nums[right])
    min_val = min(min_val, nums[right])
    while max_val - min_val > limit:
        if nums[left] == max_val:
            max_val = max(nums[left + 1:right + 1])
        elif nums[left] == min_val:
            min_val = min(nums[left + 1:right + 1])
        left += 1
        max_val = max(nums[left:right + 1])
        min_val = min(nums[left:right + 1])
    longest = max(longest, right - left + 1)
print(longest)
