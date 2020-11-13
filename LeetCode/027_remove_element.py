''' Leetcode 027: Remove Element
# Question  : Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Link      : https://leetcode.com/problems/remove-element/
# Runtime   : 28 ms   - 88%
# Memory    : 14.1 MB - 63%
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [0,1,2,2,3,0,4,2]
        #                |
        #  0,1 3 0 4 2
        #  0,0 1 2 2 2 2 3 -> 7 - 3 = 4
        if not nums:
            return 0
        else:
            nRemoved = 0
            for i, num in enumerate(nums):
                nums[i-nRemoved] = nums[i]
                if num == val:
                    nRemoved += 1
            return len(nums) - nRemoved