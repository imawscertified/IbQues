class Solution:

    def grt(self, A, prev=True):
        stack, ans = list(), [0] * len(A)
        
        if prev:
            it = range(len(A))            
        else:
            it = range(len(A)-1, -1, -1)

        for i in it:
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(i)
        return ans

    def maxSpecialProduct(self, A):
        left = self.grt(A)
        right = self.grt(A, prev=False)
        maxx = -float('inf')

        for l, r in zip(left, right):
            maxx = max(l * r, maxx)

        return maxx % 1000000007


