class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split("/")
        for s in temp:
            if not s:
                continue
            if s == "..":
                if stack:
                    stack.pop()
            elif s != ".":
                stack.append(s)
        return "/" + "/".join(stack)