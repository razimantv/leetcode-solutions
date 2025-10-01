# Remove k digits

[Problem link](https://leetcode.com/problems/remove-k-digits)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-k-digits

class Solution {
 public:
  string removeKdigits(string num, int k) {
    string ret = "";
    int N = num.size(), req = N - k;
    for (int next = 0; req > 0 and next < num.size(); --req) {
      int bestpos = next;
      char best = num[next];
      for (int i = next + 1; i + req <= N; ++i) {
        if (num[i] < best) {
          best = num[i];
          bestpos = i;
        }
      }

      if (best > '0' or ret != "") ret += best;
      next = bestpos + 1;
    }

    if (ret == "") ret = "0";
    return ret;
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and k and stack[-1] > c:
                stack.pop()
                k -= 1
            stack. append(c)
        while k:
            stack.pop()
            k -= 1

        for i, c in enumerate(stack):
            if c > '0':
                return ''. join(stack[i:])
        return '0'
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
