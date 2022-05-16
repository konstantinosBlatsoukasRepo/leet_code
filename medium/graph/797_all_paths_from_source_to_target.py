class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths = []
        # bfs paths, starting from the first node path
        queue = [[0]]
        while queue:
            path = queue.pop(0)
            last_node = path[len(path) - 1]
            if last_node == len(graph) - 1:
                paths.append(path)
            else:
                adj_nodes = graph[last_node]
                for adj_node in adj_nodes:
                    queue.append(path + [adj_node])

        return paths
