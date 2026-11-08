class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:

            width = right - left
            h = min(heights[right], heights[left])

            area = width * h
            maxArea = max(area,maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1 

        return maxArea


