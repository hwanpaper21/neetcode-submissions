# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(root):
            nonlocal best
            if root == None:
                return 0
            L = depth(root.left)
            R = depth(root.right)
            best = max(best, L+R)
            return 1+ max(L, R)

        depth(root)

        return best
            