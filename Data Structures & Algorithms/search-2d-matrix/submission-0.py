class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = 0
        for i in matrix:

            left = 0
            right = len(i) - 1

            while right >= left:
                mid = (right + left) // 2
                if target == i[mid]:
                    return True
                elif target < i[mid]:
                    right = mid -1
                else:
                    left = mid + 1
        return False
