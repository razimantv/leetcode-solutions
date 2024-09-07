# Design add and search words data structure

[Problem link](https://leetcode.com/problems/design-add-and-search-words-data-structure)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-add-and-search-words-data-structure

struct trienode {
  unordered_map<char, trienode*> next;
  trienode() {}
};

class WordDictionary {
 public:
  trienode head;
  /** Initialize your data structure here. */
  WordDictionary() {}

  /** Adds a word into the data structure. */
  void addWord(string word) {
    trienode* cur = &head;
    for (char c : word) {
      if (!cur->next.count(c)) cur->next[c] = new trienode();
      cur = cur->next[c];
    }
    cur->next['$'] = NULL;
  }

  /** Returns if the word is in the data structure. A word could contain the dot
   * character '.' to represent any one letter. */
  bool search(string word, int pos = 0, trienode* cur = NULL) {
    if (cur == NULL) cur = &head;
    if (pos == word.size()) return cur->next.count('$');
    if (word[pos] != '.')
      return (cur->next.count(word[pos]) and
              (search(word, pos + 1, cur->next[word[pos]])));
    for (auto p : cur->next)
      if (p.first != '$' and search(word, pos + 1, p.second)) return true;
    return false;
  }
};

```
## Tags

* [Trie](/Collections/trie.md#trie)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
