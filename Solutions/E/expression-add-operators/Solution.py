# https://leetcode.com/problems/expression-add-operators

class Solution:
  def addOperators(self, num, target):
    ret = []
    self.target = target
    for i in range(1,len(num)+1):
        if i == 1 or (i > 1 and num[0] != "0"): self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), ret)
    return ret

  def dfs(self, num, temp, cur, last, ret):
    if not num:
        if cur == self.target: ret.append(temp)
        return
    for i in range(1, len(num)+1):
        val = num[:i]
        if i == 1 or (i > 1 and num[0] != "0"):
            self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), ret)
            self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), ret)
            self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), ret)
