class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        source_pointer = 0
        total_found = 0

        for i in range(len(t)):
            if s[source_pointer] == t[i]:
                total_found += 1
                source_pointer += 1

                if total_found == len(s):
                    return True

        return False