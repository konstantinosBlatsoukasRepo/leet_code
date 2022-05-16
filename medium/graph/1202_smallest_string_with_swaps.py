class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """

        # initialize roots
        root = [i for i in range(len(s))]
        rank = [1 for i in range(len(s))]

        # connect the swap pairs
        for a, b in pairs:
            self.union(root, rank, a, b)

        # group vertexes per root
        rootToComponent = {}
        for vertex in range(len(s)):
            vertex_root = self.find(root, vertex)
            if vertex_root in rootToComponent:
                rootToComponent[vertex_root].append(vertex)
            else:
                rootToComponent[vertex_root] = [vertex]

        result = list(s)
        for component_key in rootToComponent:
            indices = rootToComponent[component_key]
            chars = [s[ind] for ind in indices]
            chars.sort()

            for index in range(len(indices)):
                result[indices[index]] = chars[index]

        return "".join(result)

    def find(self, root, a):
        while root[a] != a:
            a = root[a]
        return a

    def union(self, root, rank, a, b):
        root_a = self.find(root, a)
        root_b = self.find(root, b)

        if root_a != root_b:
            if rank[root_a] >= rank[root_b]:
                root[root_b] = root_a
                rank[root_a] += rank[root_b]
            else:
                root[root_a] = root_b
                rank[root_b] += rank[root_a]
