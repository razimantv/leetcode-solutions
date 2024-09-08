# https://leetcode.com/problems/convert-date-to-binary/

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(f'{int(x):b}' for x in date.split('-'))
