class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left <= right:
            mid = (right+left)//2
            total = 0
            for i in piles:
                total += (int(i)+mid-1)//mid
            
            if total > h:
                left = mid + 1
            else:
                right = mid - 1
        return left