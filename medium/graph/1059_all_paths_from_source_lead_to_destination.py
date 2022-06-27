# cycle detection in digraph

class Solution():
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        GRAY = 1
        BLACK = 2

        def build_digraph(n, edges):
            graph = [[] for i in range(n)]
            for edge in edges:
                graph[edge[0]].append(edge[1])
            return graph

        def leadsToDest(graph, node, dest, states):
            if states[node] != None:
                return states[node] == BLACK

            if len(graph[node]) == 0:
                return node == dest

            states[node] = GRAY

            for next_node in graph[node]:
                if not leadsToDest(graph, next_node, dest, states):
                    return False

            states[node] = BLACK
            return True

        states = [None for i in range(n)]
        digraph = build_digraph(n, edges)

        return leadsToDest(digraph, source, destination, states)
