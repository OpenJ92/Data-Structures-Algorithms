## https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        stack = deque([root])
        while stack:
          node = stack.pop()
          if node.left:
              graph[node].add(node.left)
              graph[node.left].add(node)
              stack.append(node.left)
          if node.right:
              graph[node].add(node.right)
              graph[node.right].add(node)
              stack.append(node.right)

        values = []
        queue = deque([(target, 0)])
        seen = set([target])
        while queue:
          node, depth = queue.popleft()
          if depth == k:
            values.append(node.val)
          neighbors = graph[node]
          for neighbor in neighbors:
            if neighbor not in seen:
              queue.append([neighbor, depth + 1])
              seen.add(neighbor)

        return values
