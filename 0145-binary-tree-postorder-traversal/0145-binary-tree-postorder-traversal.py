# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        l = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    l.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        l.append(temp.val)
                else:
                    curr = temp
        return l