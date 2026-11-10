# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        def listTree(root, lst):
            templst = lst
            if root == None:
                templst.append(None)
                return templst
            templst.append(root.val)
            listTree(root.left, templst)
            listTree(root.right, templst)
            return templst
        tree1 = listTree(p, tree1)
        tree2 = listTree(q, tree2)
        return tree1 == tree2
