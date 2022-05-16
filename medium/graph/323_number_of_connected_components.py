class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        root = [-1 for i in range(n)]

        for edge in edges:
            self.union(root, edge[0], edge[1], count)

        return len([i for i in root if i == -1])

    def find(self, root, a):
        if root[a] == -1:
            return a
        return self.find(root, root[a])

    def union(self, root, a, b, count):
        root_a = self.find(root, a)
        root_b = self.find(root, b)

        if root_a != root_b:
            root[root_b] = root_a
