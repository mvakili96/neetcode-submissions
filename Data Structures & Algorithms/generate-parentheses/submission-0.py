class Solution:
    def generateParenthesis(self, n: int) -> List[str]:      
        result = []
        def dfs(n_open,n_close,current):
            if n_open == 0 and n_close == 0:
                result.append(current)
                return 
            elif  n_open == 0 and n_close != 0:
                for i in range(n_close):
                    current.append(")")
                result.append(current)
                return 
            
            if n_close > n_open:      
                current.append(")")
                dfs(n_open,n_close-1,current.copy())
                current.pop()
                current.append("(")
                dfs(n_open-1,n_close,current.copy())
            elif n_close == n_open:      
                current.append("(")
                dfs(n_open-1,n_close,current.copy())

        dfs(n-1,n,["("])
        out = []
        for lst in result:
            out.append("".join(lst))

        return out