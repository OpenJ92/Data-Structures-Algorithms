# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(nums):
            if not nums:
                return None

            index = nums.index(max(nums))

            left  = construct(nums[:index])
            right = construct(nums[index+1:])

            return TreeNode(val=nums[index],left=left,right=right)

        return construct(nums)
