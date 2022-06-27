# BIDIRECTIONAL!!!!!!!!
# the mistake that was doing: building only the one direction in gra[h construction

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        def build_graph(n, edges):
            graph = [[] for i in range(n)]
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
            return graph

        def path_exists(source, destination):
            seen = set()
            queue = [source]
            while queue:
                node = queue.pop(0)

                seen.add(node)
                if node == destination:
                    return True

                for adj_node in graph[node]:
                    if adj_node not in seen:
                        queue.append(adj_node)

            return False

        graph = build_graph(n, edges)
        return path_exists(source, destination)
