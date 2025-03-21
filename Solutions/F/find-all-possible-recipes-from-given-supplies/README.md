# Find all possible recipes from given supplies

[Problem link](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]],
        supplies: list[str]
    ) -> list[str]:
        supplies = set(supplies)
        recipes = {
            recipe: ingredient
            for recipe, ingredient in zip(recipes, ingredients)
        }
        seen = set()

        @cache
        def poss(recipe):
            seen.add(recipe)
            for ingredient in recipes[recipe]:
                if ingredient in supplies:
                    continue
                elif (
                    ingredient in seen or ingredient not in recipes
                    or not poss(ingredient)
                ):
                    break
            else:
                seen.remove(recipe)
                return True
            return False

        return [recipe for recipe in recipes if poss(recipe)]
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
