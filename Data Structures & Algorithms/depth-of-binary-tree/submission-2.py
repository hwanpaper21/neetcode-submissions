# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = 0
        right = 0
        if root == None:
            return 0
        def calDepth(root, cdepth):
            depth = cdepth
            if root == None:
                print(depth)
                return depth
            else: depth += 1
            return max(calDepth(root.left, depth), calDepth(root.right, depth))

        left = calDepth(root.left, 0)
        right = calDepth(root.right, 0)

        print(left,right)
        return 1+max(left, right)