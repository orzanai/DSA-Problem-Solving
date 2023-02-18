"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

def twoSum(self, nums: List[int], target: int) -> List[int]:
    emp_d = {}
    for idx, num in enumerate(nums):
        if idx not in emp_d.keys():
            emp_d[idx] = num
        if target - num in emp_d.values() and nums.index(target - num) != idx:
            return [idx, nums.index(target - num)]