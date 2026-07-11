# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.maxsum = float('-inf')#very very important part
        self.dfs(root)
        return self.maxsum
    def dfs(self, root):
        if root == None: 
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        self.maxsum = max(self.maxsum , left + right + root.val)
        return max(left, right) + root.val        