# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        heap = []
        queue = deque([root])
        level = 1
        while queue:
            level_length = len(queue)
            level_values = []
            for _ in range(level_length):
                node = queue.popleft()
                level_values.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            heappush(heap, (-sum(level_values), level))
            level += 1

        kth, level = heappop(heap)

        return level
