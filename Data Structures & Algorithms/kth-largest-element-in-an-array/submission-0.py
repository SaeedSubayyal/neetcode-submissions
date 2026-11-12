class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        for i in range(len(nums)):
            heap.append(nums[i])


        heapq.heapify(heap)


        while len(heap) > k:

           num =  heapq.heappop(heap)

        
        return heap[0]

