class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = [-1] * len(nums1)
        nGE = [0] * len(nums2)

        stack = deque()
        for index, value in enumerate(nums2):
            if not stack:
                stack.append((index, value))
                continue

            while stack and value > stack[-1][1]:
                idx, val = stack.pop()
                nGE[idx] = value

            stack.append((index, value))

        for idx, num in enumerate(nums1):
            next_greatest = nGE[nums2.index(num)]
            if next_greatest != 0:
                out[idx] = next_greatest

        return out
