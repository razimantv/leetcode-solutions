# Find duplicate file in system

[Problem link](https://leetcode.com/problems/find-duplicate-file-in-system)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-duplicate-file-in-system

class Solution {
 public:
  vector<vector<string>> findDuplicate(vector<string>& paths) {
    unordered_map<string, vector<string>> dup;

    for (const string& s : paths) {
      istringstream iss(s);
      string dir, file;
      iss >> dir;

      while (iss >> file) {
        int L = file.size();
        for (int i = 0;; ++i) {
          if (file[i] == '(') {
            string filename = file.substr(0, i),
                   content = file.substr(i + 1, L - i - 2);
            dup[content].push_back(dir + "/" + filename);
            break;
          }
        }
      }
    }

    vector<vector<string>> ret;
    for (const auto& [c, n] : dup) {
      if (n.size() > 1) ret.push_back(n);
    }
    return ret;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Hashmap](/Collections/hashmap.md#hashmap)
