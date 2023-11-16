# https://leetcode.com/problems/find-unique-binary-string/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('0' if s[i] == '1' else '1' for i, s in enumerate(nums))
