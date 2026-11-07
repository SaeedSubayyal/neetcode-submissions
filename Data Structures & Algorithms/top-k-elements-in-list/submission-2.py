class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        #  freq: [], freq: []
        
        buckets = []
        for _ in range(len(nums)+1):
            buckets.append([])

        for num in count:
            freq = count[num]
            buckets[freq].append(num)

        result = []
        freq = len(nums)

        while freq > 0:
            for num in buckets[freq]:
                result.append(num)
            
            if len(result) == k:
                return result

            freq -= 1

        return result
