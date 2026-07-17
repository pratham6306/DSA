# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mirror(self, l, rt):
        if l is None or rt is None:
            return l == rt
        return (l.val == rt.val and self.mirror(l.left, rt.right) and self.mirror(l.right, rt.left))

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None: return True
        return self.mirror(root.left, root.right)
        