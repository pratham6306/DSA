# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    dia = 0
    def diameterOfBinaryTree(self, root):
        
        self.height(root)
        return self.dia
    def height(self, root):
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        self.dia = max(self.dia, left + right)
        return 1 + max(left, right)    