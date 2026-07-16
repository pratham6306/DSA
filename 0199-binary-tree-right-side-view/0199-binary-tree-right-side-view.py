# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        # Final 2D result list
        ans = []

        # Return empty if tree is empty
        if not root:
            return ans

        # Create queue for BFS
        q = deque()
        q.append(root)

        # Loop until queue is empty
        while q:
            # Get number of nodes at current level
            size = len(q)

            # List to hold current level values
            level = []

            # Process all nodes at this level
            for _ in range(size):
                # Pop node from queue
                node = q.popleft()

                # Store its value
                level.append(node.val)

                # Add left child if exists
                if node.left:
                    q.append(node.left)

                # Add right child if exists
                if node.right:
                    q.append(node.right)

            # Append this level to answer
            ans.append(level)

        return ans
    def rightSideView(self, root):
        level = self.levelOrder(root)
        return [x[-1] for x in level]
        
        