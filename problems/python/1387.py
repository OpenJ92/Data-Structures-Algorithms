class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = defaultdict(int)
        memo[1] = 0
        def get_power(num):
            if num in memo:
                return memo[num]

            if num % 2 == 0:
                next_num = num // 2
            else:
                next_num = 3 * num + 1

            memo[num] = 1 + get_power(next_num)
            return memo[num]

        powers = []
        while lo <= hi:
            powers.append(((get_power(lo), lo), lo))
            lo += 1
        heapify(powers)

        while powers and k:
            _, num = heappop(powers)
            k -= 1

        return num

