class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        # index, value
        for i, val in enumerate(nums):

            diff = target - nums[i]

            if diff in seen:
                return [seen[diff],i]
            
            seen[val] = i
            

