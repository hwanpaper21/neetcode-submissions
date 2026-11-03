class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pt1 = 0
        pt2 = 0
        temp = []
        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] < nums2[pt2]:
                temp.append(nums1[pt1])
                pt1 += 1
            else:
                temp.append(nums2[pt2])
                pt2 += 1
        if pt1 != len(nums1):
            temp += nums1[pt1:]
        else:
            temp += nums2[pt2:]

        if len(temp) % 2 != 0:
            idx2 = len(temp)//2
            return temp[idx2]

        else:
            idx1 = len(temp)//2
            return(temp[idx1] + temp[idx1-1])/2
  
        