# Takeaway: similar procedure as the conversion from decimal to binary
# Perfrom succesive division with the base (here the base is 26 instaed of 2)

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        while columnNumber > 26:
            result += chr(ord('A') + (columnNumber - 1) % 26)
            columnNumber = int((columnNumber - 1) / 26)

        result += chr(ord('A') + (columnNumber - 1) % 26)
        return result[::-1]
