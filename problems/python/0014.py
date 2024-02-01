class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def first(array):
            return array[0]
        def rest(array):
            return array[1:]

        def tails(arrays):
            output = []
            narrays = []
            for index in range(len(arrays)):
                item = first(arrays[index])
                output.append(item)
                arrays[index] = rest(arrays[index])
            return output

        output = []
        while all(strs):
            tail = tails(strs)
            if len(set(tail))!=1:
                break
            output.append(first(tail))


        return ''.join(output)
