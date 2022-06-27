# kruskal's algorithm

class UnionFind():
    def __init__(self, size):
        self.root = [0] * size
        self.rank = [0] * size

        for i in range(size):
            self.root[i] = i

    def find(self, node):
        if self.root[node] == node:
            return node
        return self.find(self.root[node])

    def union(self, node1, node2):
        group1 = self.find(node1)
        group2 = self.find(node2)

        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.root[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.root[group1] = group2
        else:
            self.root[group1] = group2
            self.rank[group2] += 1

        return True


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)
        all_edges = []

        # storing all edges
        for curr_node in range(n):
            for next_node in range(curr_node + 1, n):
                weight = abs(points[curr_node][0] - points[next_node][0]) +\
                    abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))

        # sort all edges base don the weight
        all_edges.sort()

        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0

        for weight, node1, node2 in all_edges:
            if uf.union(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break

        return mst_cost



points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
sol = Solution()
sol.minCostConnectPoints(points)