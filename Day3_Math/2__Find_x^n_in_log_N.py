# https://leetcode.com/problems/powx-n/submissions/

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

def myPow(x,n):
    def find(x,n):
        if n == 0:
            return 1
        if n == 1:
            return x
        else:
            val = find(x,n//2)

            if n%2==0:
                return val*val
            else:
                return val*val*x

    def handle(x,n):
        if n<0:
            n*=-1
            return 1/find(x,n)
        else:
            return find(x,n)
    return handle(x,n)

ans = myPow(2,32)