class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        queue = deque()
        for num in nums:
            queue.append(deque([num]))

        def valid(queue):
            return len(queue) > 1

        def merge(lst1, lst2):
            nlst = deque()
            while lst1 and lst2:
                one = lst1.popleft()
                two = lst2.popleft()

                if one < two:
                    nlst.append(one)
                    lst2.appendleft(two)
                else:
                    nlst.append(two)
                    lst1.appendleft(one)

            if lst1:
                nlst += lst1
            if lst2:
                nlst += lst2

            return nlst

        while valid(queue):
            lst1 = queue.popleft()
            lst2 = queue.popleft()
            lstn = merge(lst1, lst2)
            queue.append(lstn)

        result, *_ = queue
        return result
