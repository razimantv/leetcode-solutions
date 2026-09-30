# Web crawler

[Problem link](https://leetcode.com/problems/web-crawler/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/web-crawler/


class Solution:
    def crawl(self, start: str, parser: "HtmlParser") -> list[str]:
        def host(url):
            return "/".join(url.split("/")[:3])

        h, seen, todo, ret = host(start), {start}, [start], []
        while todo:
            u = todo.pop()
            ret.append(u)
            for v in parser.getUrls(u):
                if host(v) == h and v not in seen:
                    seen.add(v)
                    todo.append(v)
        return ret
```
## Tags

* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
