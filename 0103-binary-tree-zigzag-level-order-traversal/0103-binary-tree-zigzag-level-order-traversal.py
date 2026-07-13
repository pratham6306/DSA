# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        ans = []
        if not root:
            return ans
        q = deque([root])
        dirn = True
        while q:
            size = len(q)
            l = [0]*size
            for i in range(size):
                node = q.popleft()
                index = i if dirn else size - 1 - i
                l[index] = node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            dirn = not dirn
            ans.append(l)
        return ans
            
        