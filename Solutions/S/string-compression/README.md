# String compression

[Problem link](https://leetcode.com/problems/string-compression)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/string-compression

class Solution {
 public:
  int compress(vector<char>& chars) {
    int outpos = 1;
    for (int inpos = 1, count = 1, N = chars.size();; ++inpos) {
      if (inpos < N and chars[inpos] == chars[inpos - 1])
        ++count;
      else {
        if (count > 1) {
          string s = to_string(count);
          for (int i = 0; s[i]; chars[outpos++] = s[i++])
            ;
        }
        if (inpos == N) break;
        chars[outpos++] = chars[inpos];
        count = 1;
      }
    }
    return outpos;
  }
};
```