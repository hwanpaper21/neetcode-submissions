class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        ans = 0
        while left<right:
            if heights[left] > heights[right]:
                area = abs(right-left)*heights[right]
            else:
                area = abs(right-left)*heights[left]
            
            print(area,ans)
            if area > ans:
                ans = area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans