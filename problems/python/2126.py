class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort(reverse=True)
        if mass < asteroids[-1]:
            return False

        while asteroids:
            asteroid = asteroids.pop()
            if asteroid > mass:
                return False
            mass += asteroid
        return True
