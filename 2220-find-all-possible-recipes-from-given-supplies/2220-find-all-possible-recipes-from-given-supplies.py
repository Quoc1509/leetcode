class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        mp = defaultdict(list)
        for i in range(len(recipes)):
            mp[recipes[i]].extend(ingredients[i])
        visit = set()
        def dfs(node):
            if node in supplies:
                return True
            if len(mp[node]) == 0 or node in visit:
                return False
            visit.add(node)
            for n in mp[node]:
                if not dfs(n):
                    return False
            supplies.add(node)
            return True
        ans = []
        for food in recipes:
            if dfs(food):
                ans.append(food)
        return ans