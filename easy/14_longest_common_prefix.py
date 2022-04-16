class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest_word_len = min([len(word) for word in strs])
        result = ''
        for i in range(shortest_word_len):
            test = strs[0][i]

            if (all([test == str[i] for str in strs])):
                result += strs[0][i]
            else:
                return result
        return result


sol = Solution()

assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
