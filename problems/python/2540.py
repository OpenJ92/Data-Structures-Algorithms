class Solution:
    def getCommon(self, num: List[int], ber: List[int]) -> int:
        def first(list):
            return list[0]
        def last(list):
            return list[-1]
        
        if last(num) < first(ber) or first(num) > last(ber):
            return -1 

        pointer = 0
        pojnter = 0

        length = len(num)
        lemgth = len(ber)

        while pointer < length and pojnter < lemgth:
            while pointer < length and num[pointer] < ber[pojnter]:
                pointer += 1

            if num[pointer] == ber[pojnter]:
                return num[pointer]
            
            while pojnter < lemgth and num[pointer] > ber[pojnter]:
                pojnter += 1
        
        return -1
