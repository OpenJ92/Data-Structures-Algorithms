class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = self.make_vec(nums)

    def dotProduct(self, vec: 'SparseVector') -> int:
        dot = 0
        while self.vec and vec.vec:
            index, val = self.vec.popleft()
            jndex, ual = vec.vec.popleft()

            if index == jndex:
                dot += val*ual
                continue

            if index < jndex:
                vec.vec.appendleft((jndex, ual))
            if index > jndex:
                self.vec.appendleft((index, val))
        return dot

    def make_vec(self, nums):
        vec = []
        for index, val in enumerate(nums):
            if val:
                vec.append((index, val))
        return deque(vec)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
