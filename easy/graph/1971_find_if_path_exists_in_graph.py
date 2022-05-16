class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        def build_graph(edges):
            graph = {}
            for node_one, node_two in edges:
                if node_one not in graph:
                    graph[node_one] = [node_two]
                elif node_two not in graph[node_one]:
                    graph[node_one].append(node_two)

                if node_two not in graph:
                    graph[node_two] = [node_one]
                elif node_one not in graph[node_two]:
                    graph[node_two].append(node_one)
            return graph

        def path_exists(source, destination):
            seen = set()
            stack = [source]
            while stack:
                node = stack.pop()

                if node == destination:
                    return True

                if node not in seen:
                    seen.add(node)
                    for adj_node in graph[node]:
                        stack.append(adj_node)

            return False

        graph = build_graph(edges)
        return path_exists(source, destination)
