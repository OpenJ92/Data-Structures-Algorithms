class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(n)]

        for _, destination in edges:
            indegree[destination] += 1
        
        output = []
        for node, degree in enumerate(indegree):
            if not degree:
                output.append(node)
        return output
