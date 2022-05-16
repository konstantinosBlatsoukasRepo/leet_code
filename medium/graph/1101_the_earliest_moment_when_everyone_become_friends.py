class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """

        logs = [(log[0], log[1], log[2]) for log in logs]
        logs = sorted(logs, key=lambda tup: tup[0])

        root = [-1 for i in range(n)]

        for (time, a, b) in logs:
            result = self.union(root, time, a, b, n)
            if result[0]:
                return result[1]

        return -1

    def find(self, root, a):
        if root[a] == -1:
            return a
        return self.find(root, root[a])

    def union(self, root, time, a, b, n):
        root_a = self.find(root, a)
        root_b = self.find(root, b)
        if root_a != root_b:
            root[root_b] = root_a

        if len([i for i in root if i == -1]) == 1:
            return [True, time]
        return [False, -1]
