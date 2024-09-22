# https://leetcode.com/problems/report-spam-message/

class Solution:
    def reportSpam(self, message: List[str], banned: List[str]) -> bool:
        banned, bad = set(banned), 0
        for word in message:
            if word in banned:
                if bad:
                    return True
                bad = 1
        return False
