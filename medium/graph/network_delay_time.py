

import heapq
import sys


class Solution():
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        def build_graph(times, n):
            graph = {m: [] for m in range(n)}
            for source, target, weight in times:
                graph[source - 1].append((target - 1, weight))
            return graph

        distances = [sys.maxsize for _ in range(n)]
        distances[k - 1] = 0

        graph = build_graph(times, n)
        seen = set()

        best_dist_node = [(0, k - 1)]
        heapq.heapify(best_dist_node)

        # djikstra
        while best_dist_node:
            best_dist, node_id = heapq.heappop(best_dist_node)
            seen.add(node_id)
            for candidate_target, edg_weight in graph[node_id]:
                if candidate_target not in seen:
                    new_dist = distances[node_id] + edg_weight
                    if new_dist < distances[candidate_target]:
                        distances[candidate_target] = new_dist
                        heapq.heappush(
                            best_dist_node, (new_dist, candidate_target))



        return max(distances)


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

sol = Solution()
sol.networkDelayTime(times, n, k)
