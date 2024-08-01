# Shortest string that contains three strings

[Problem link](https://leetcode.com/problems/shortest-string-that-contains-three-strings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
 public:
  int add(string &a, string &b) {
    int A = a.size(), B = b.size();
    if (A <= B and b.find(a) != string::npos) return 0;
    for (int L = min(A, B); L; --L) {
      bool flag{true};
      for (int i = 0, j = A - L; i < L; ++i, ++j) {
        if (b[i] != a[j]) {
          flag = false;
          break;
        }
      }
      if (flag) return A - L;
    }
    return A;
  }

  string work(string &a, string &b, string &c) {
    int l1 = add(a, b);
    reverse(b.begin(), b.end());
    reverse(c.begin(), c.end());
    int l2 = add(c, b);
    reverse(b.begin(), b.end());
    reverse(c.begin(), c.end());
    return a.substr(0, l1) + b + c.substr(c.size() - l2);
  }

  string minimumString(string a, string b, string c) {
    vector<string> all{a, b, c};
    sort(all.begin(), all.end());
    string ret = a + b + c;
    do {
      auto cur = work(all[0], all[1], all[2]);
      if (cur.size() < ret.size() or (cur.size() == ret.size() and cur < ret))
        ret = cur;
    } while (next_permutation(all.begin(), all.end()));
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Prefix/Suffix](/Collections/string.md#prefix-suffix)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
