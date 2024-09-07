# Stream of characters

[Problem link](https://leetcode.com/problems/stream-of-characters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/stream-of-characters

class StreamChecker {
  struct TrieNode {
    unordered_map<char, TrieNode *> next;
    bool end;
    TrieNode() : end(false) {}
  };

 public:
  TrieNode *head;
  vector<char> stream;
  StreamChecker(vector<string> &words) {
    head = new TrieNode;
    for (auto w : words) {
      TrieNode *cur = head;
      for (int i = w.size() - 1; i >= 0; --i) {
        char c = w[i];
        if (!cur->next.count(c)) cur->next[c] = new TrieNode;
        cur = cur->next[c];
      }
      cur->end = true;
    }
  }

  bool query(char letter) {
    stream.push_back(letter);
    TrieNode *cur = head;
    for (int i = stream.size() - 1; i >= 0; --i) {
      char c = stream[i];
      if (!cur->next.count(c)) return false;
      cur = cur->next[c];
      if (cur->end) return true;
    }
    return false;
  }
};

```