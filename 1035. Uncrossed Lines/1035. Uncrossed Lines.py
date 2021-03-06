
class Solution:
    def maxUncrossedLines(self, A, B):
        m, n = len(A), len(B)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1]==B[j-1]:
                    T[i][j] = T[i-1][j-1] + 1
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        
        return T[-1][-1]
        