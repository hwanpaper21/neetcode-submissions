# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def height(root, level):
            depth = level
            if root == None:
                return depth
            depth += 1
            return max(height(root.left,depth), height(root.right, depth))
        left = height(root.left, 1)
        right = height(root.right, 1)


        if abs(left-right) > 1:
            return False
        return (
            self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

