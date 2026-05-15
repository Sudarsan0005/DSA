'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
'''
Optimal Approach (Hash Map)

Instead of checking every pair (slow), we use a hash map for fast lookup.

Idea
- Loop through the array
- For each number x, compute target - x
- Check if that value already exists in the map
- If yes → return indices
- If not → store x in map'''

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]] =i
print(Solution().twoSum(nums= [2,7,11,15],target=9))
print(Solution().twoSum(nums= [3,3],target=6))