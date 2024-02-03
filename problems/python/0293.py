class Solution:
    def generatePossibleNextMoves(self, current_state: str) -> List[str]:
        next_states = []
        for index in range(0, len(current_state)-1):
            if current_state[index:index+2] != '++':
                continue
            candidate = current_state[:index] + '--' + current_state[index+2:]
            next_states.append(candidate)
        return next_states
