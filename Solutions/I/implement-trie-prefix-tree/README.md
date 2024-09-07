# Implement trie prefix tree

[Problem link](https://leetcode.com/problems/implement-trie-prefix-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/implement-trie-prefix-tree

class Trie {
 public:
  map<char, Trie*> T;

  /** Initialize your data structure here. */
  Trie() {}

  /** Inserts a word into the trie. */
  void insert(string word) {
    Trie* Tp = this;
    for (char c : word) {
      if (!Tp->T.count(c)) Tp->T[c] = new Trie();
      Tp = Tp->T[c];
    }
    Tp->T['$'] = NULL;
  }

  /** Returns if the word is in the trie. */
  bool search(string word) {
    Trie* Tp = this;
    for (char c : word) {
      if (!Tp->T.count(c)) return false;
      Tp = Tp->T[c];
    }
    return Tp->T.count('$');
  }

  /** Returns if there is any word in the trie that starts with the given
   * prefix. */
  bool startsWith(string prefix) {
    Trie* Tp = this;
    for (char c : prefix) {
      if (!Tp->T.count(c)) return false;
      Tp = Tp->T[c];
    }
    return true;
  }
};

```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Trie](/Collections/trie.md#trie)
