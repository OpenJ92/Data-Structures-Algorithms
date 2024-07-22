class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for index in range(len(heights)):
            heights[index] = (-heights[index], index)

        heights.sort()
        for index in range(len(heights)):
            (_, jndex) = heights[index]
            heights[index] = names[jndex]

        return heights

