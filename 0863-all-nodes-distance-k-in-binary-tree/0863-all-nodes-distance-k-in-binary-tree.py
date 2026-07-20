# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def parent(self, root, pmap):
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                pmap[node.left] = node
                q.append(node.left)
            if node.right:
                pmap[node.right] = node
                q.append(node.right)
                
    def distanceK(self, root, target, k):
        if root is None:
            return []
        pmap = {}
        self.parent(root, pmap)
        return self.bfs(target, pmap, k)

    def bfs(self, target, pmap, k):
        q = deque()
        vis = set()
        q.append(target)
        vis.add(target)
        level = 0
        while q:
            size = len(q)
            if level == k:
                break
            for _ in range(size):
                node = q.popleft()
                if node.left and node.left not in vis:
                    vis.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in vis:
                    vis.add(node.right)
                    q.append(node.right)
                if node in pmap and pmap[node] not in vis:
                    vis.add(pmap[node])
                    q.append(pmap[node])
            level += 1
        return [x.val for x in q]