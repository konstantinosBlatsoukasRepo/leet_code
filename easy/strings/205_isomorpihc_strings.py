# better aproach with two maps
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapped = {}
        for i in range(len(s)):
            if s[i] not in mapped:
                mapped[s[i]] = t[i]
            elif s[i] in mapped and mapped[s[i]] != t[i]:
                return False

        for val in Counter(mapped.values()).values():
            if val > 1:
                return False

        for i in range(len(s)):
            s = s[:i] + t[i] + s[i + 1:]

        return s == t
