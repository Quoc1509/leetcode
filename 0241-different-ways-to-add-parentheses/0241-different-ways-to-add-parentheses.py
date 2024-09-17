class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # operating = []
        # num = ""
        # for i in expression:
            
        #     if not i.isdigit():
        #         operating.append(num)
        #         operating.append(i)
        #         num = ""
        #     else:
        #         num += i
        # operating.append(num)

        def compute(l, r, o):
            temp = []
            for i in range(len(l)):
                for j in range(len(r)):
                    if o == '-':
                        temp.append(l[i]-r[j])
                    elif o == '+':
                        temp.append(l[i]+r[j])
                    elif o == '*':
                        temp.append(l[i]*r[j])
            return temp

        @cache
        def dvd(e):
            if len(e) < 3: return [int(e)]
            
            res = []
            for i in range(len(e)):
                
                if not e[i].isdigit():
                    left = dvd(e[:i])
                    right = dvd(e[i+1:])
                    temp = compute(left, right, e[i])
                    res.extend(temp)
            return res
        return dvd(expression)
        