class Solution:
    def reverseParentheses(self, s: str) -> str:
        pa = 0
        st = [""]
        temp = ""
        for i in s:
            if i == "(":
                st.append("")
            elif i == ")":
                st[-1] = st[-1][::-1]
                if len(st) > 1:
                    st[-2] = st[-2]+st[-1]
                    st.pop()
            else:
                st[-1] += i
        # print(st)
                
        return "".join(st)
                 
