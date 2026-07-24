# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.lst1 = []
        self.lst2 = []
        def dfs1(node):
            if node == None:
                self.lst1.append('null')
                return
            
            self.lst1.append(node.val)
            dfs1(node.left)
            dfs1(node.right)
        def dfs2(node):
            if node == None:
                self.lst2.append('null')
                return
            
            self.lst2.append(node.val)
            dfs2(node.left)
            dfs2(node.right)
        dfs1(p)
        dfs2(q)
        print(self.lst1, self.lst2)
        return self.lst1 == self.lst2

