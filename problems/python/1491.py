class Solution:
    def average(self, salaries: List[int]) -> float:
        length     = len(salaries) - 2
        min_salary = min(salaries)
        max_salary = max(salaries)

        sum = 0
        exclude = set([min_salary, max_salary])
        for salary in salaries:
            if salary in exclude:
                continue
            sum += salary

        return sum / length
