from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ['+', '-', '*', '/']
        st = []
        for c in tokens:
            if c not in opr:
                st.append(int(c))
                continue
            b, a = st.pop(), st.pop()
            if c == '+':
                st.append(a+b)
            elif c == '-':
                st.append(a-b)
            elif c == '*':
                st.append(a*b)
            else:
                st.append(int(a/b))

            # print(st)
        
        return st[0]

# print(Solution().evalRPN(tokens = ["2","1","+","3","*"]))
# print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))
print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))