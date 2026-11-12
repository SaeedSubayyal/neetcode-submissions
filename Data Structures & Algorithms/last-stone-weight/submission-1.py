class Solution:
    def lastStoneWeight(self, stones):
        
        heap = []

        for i in range(len(stones)):
            heapq.heappush(heap,-stones[i])

        while len(heap) > 1:

            num1 = -heapq.heappop(heap)
            num2 = -heapq.heappop(heap)

            if num1 == num2:
                continue

            else:
                heapq.heappush(heap,-(num1-num2))

        if heap:
            return -heap[0]

        return 0
