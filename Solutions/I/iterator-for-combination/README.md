# Iterator for combination

[Problem link](https://leetcode.com/problems/iterator-for-combination)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/iterator-for-combination

class CombinationIterator {
 public:
  vector<int> perm;
  bool can;
  string word;
  CombinationIterator(string characters, int k) {
    word = characters;
    perm = vector<int>(word.size(), 0);
    fill(perm.begin(), perm.begin() + k, 1);
    can = true;
  }

  string next() {
    string ret = "";
    for (int i = 0; i < perm.size(); ++i)
      if (perm[i]) ret += word[i];
    can = prev_permutation(perm.begin(), perm.end());
    return ret;
  }

  bool hasNext() { return can; }
};

```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
