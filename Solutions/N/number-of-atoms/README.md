# Number of atoms

[Problem link](https://leetcode.com/problems/number-of-atoms/description/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-atoms/description/
class Solution {
 public:
  map<string, int> work(string& formula, int& pos) {
    map<string, int> ret;
    while (formula[pos]) {
      map<string, int> cur;
      string elem;
      if (formula[pos] == ')') {
        ++pos;
        break;
      }

      while (islower(formula[pos]) or (elem.empty() and isupper(formula[pos])))
        elem += formula[pos++];

      if (elem.empty())
        cur = work(formula, ++pos);
      else
        cur[elem] = 1;

      int cnt = 0;
      while (isdigit(formula[pos])) cnt = cnt * 10 + formula[pos++] - '0';
      if (!cnt) cnt = 1;

      for (auto [k, v] : cur) ret[k] += v * cnt;
    }
    return ret;
  }

  string countOfAtoms(string formula) {
    int pos = 0;
    auto m = work(formula, pos);
    string ret;
    for (auto [k, v] : m) {
      ret += k;
      if (v > 1) ret += to_string(v);
    }
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing) > [Recursive](/Collections/string.md#recursive)
* [Hashmap](/Collections/hashmap.md#hashmap)
