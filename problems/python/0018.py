## TLE
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        valid_selections  = set()

        def dfs(index, sum, current_selection):
            nonlocal valid_selections
            if index > len(nums):
                return

            if len(current_selection) == 4:
                if sum == target:
                    valid_selection = current_selection[:]
                    valid_selection.sort()
                    valid_selections.add(tuple(valid_selection))
                    return

            for jndex in range(index, len(nums)):
                sum += nums[jndex]
                current_selection.append(nums[jndex])
                dfs(jndex+1, sum, current_selection)
                current_selection.pop()
                sum -= nums[jndex]
            dfs(index+1, sum, current_selection)
            return

        dfs(0, 0, [])
        return valid_selections
