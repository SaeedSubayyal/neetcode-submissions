class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i in range(len(nums)):

            if nums[i] in hashmap:
                diff = target - nums[i]
                if diff in hashmap and hashmap[diff] != i:
                    return [hashmap[diff], i]
            
            else:
                hashmap[nums[i]] = 0
                hashmap[nums[i]] = i

                diff = target - nums[i]

                if diff in hashmap and hashmap[diff] != i:
                    return [hashmap[diff],i]

