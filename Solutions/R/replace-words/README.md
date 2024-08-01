# Replace words

[Problem link](https://leetcode.com/problems/replace-words/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class Node:
            def __init__(self):
                self.children = defaultdict(Node)
                self. end = False

        trie = Node()

        def insert(word):
            node = trie
            for c in word:
                node = node. children[c]
            node.end = True

        def get(word):
            node = trie
            for i, c in enumerate(word):
                if c not in node. children:
                    return word
                node = node. children[c]
                if node. end:
                    return word[:i + 1]
            return word

        for word in dictionary:
            insert(word)
        return ' '. join(map(get, sentence. split(' ')))
```
## Tags

* [Trie](/Collections/trie.md#trie)
