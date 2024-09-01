# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (
            ord(coordinate1[0]) + ord(coordinate1[1])
            + ord(coordinate2[0]) + ord(coordinate2[1])
        ) & 1 == 0
