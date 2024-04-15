class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length, seen, stack = len(rooms), set([0]), [0]

        while stack:
            room = stack.pop()

            for key in rooms[room]:
                if key not in seen:
                    stack.append(key)
                    seen.add(key)

        return len(seen) == length

