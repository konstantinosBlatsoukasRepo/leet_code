class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_num = str(bin(n))[2:].zfill(32)
        return int(bin_num[::-1], 2)
