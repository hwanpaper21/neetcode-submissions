class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1+nums2
        temp.sort()

        if len(temp) % 2 != 0:
            idx3 = len(temp)//2
            return temp[idx3]

        else:
            idx1 = len(temp)//2
            idx2 = len(temp)//2-1
            return(temp[idx1] + temp[idx2])/2
  
        