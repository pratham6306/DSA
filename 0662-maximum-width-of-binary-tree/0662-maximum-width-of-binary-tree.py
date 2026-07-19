# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):

        # If root is None, return 0
        if not root:
            return 0

        # Initialize max width
        max_width = 0

        # Queue for BFS traversal
        # Stores node and its index
        q = deque()
        q.append((root, 0))

        # Continue BFS
        while q:

            # Size of current level
            size = len(q)

            # Minimum index at this level
            min_index = q[0][1]

            # Initialize first and last
            first = 0
            last = 0

            # Process all nodes at this level
            for i in range(size):

                # Get node and relative index
                node, idx = q.popleft()
                curr_index = idx - min_index

                # Set first index
                if i == 0:
                    first = curr_index

                # Set last index
                if i == size - 1:
                    last = curr_index

                # Append left child if exists
                if node.left:
                    q.append((node.left, 
                              2 * curr_index + 1))

                # Append right child if exists
                if node.right:
                    q.append((node.right, 
                              2 * curr_index + 2))

            # Update max width
            max_width = max(max_width, 
                            last - first + 1)

        # Return the answer
        return max_width