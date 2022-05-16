# this can be solved using bfs or dfs, apply the algorithm at each node

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        parent = [-1 for root in range(0, len(isConnected))]

        for city in range(0, len(isConnected)):
            for other_city in range(0, len(isConnected)):
                if isConnected[city][other_city] == 1 and city != other_city:
                    self.union(parent, city, other_city)


        # total provinces are the total nodes that don't have parents (e.g. the root is -1)
        count = 0
        for i in range(0, len(parent)):
            if parent[i] == -1:
                count = count + 1


        return count


    def find_root(self, parent, city):
        if parent[city] == -1:
            return city
        return self.find_root(parent, parent[city])

    def union(self, parent, city_a, city_b):
        x_set = self.find_root(parent, city_a)
        y_set = self.find_root(parent, city_b)
        if x_set != y_set:
            parent[x_set] = y_set
