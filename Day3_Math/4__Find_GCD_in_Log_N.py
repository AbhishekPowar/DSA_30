# https://practice.geeksforgeeks.org/problems/lcm-and-gcd/0
#4__Find_GCD_in_Log_N

# Normal O(min(m,n))
def hcfFunc(m,n):
    for i in range(min(m,n),0,-1):
        if m%i == 0 and n%i ==0:
            return i

# Euclids method
def gcdEuclid(m,n):
    if m == 0:
        return n
    if n == 0:
        return m
    if m == n:
        return m
    if m>n:
        return gcd(m-n,n)
    return gcd(m,n-m)

# Improved Euclid
def gcdFunc(m,n):
    def gcd(m,n):
        print(m,n)
        if n == 0:
            return m
        return gcd(n,m%n)
    if n==1:
        return m
    if m==1:
        return n
    else:
        return gcd(m,n)
    # if m==0:
    #     return n
    # return gcd(m%n,n)

def lcmfunc(m,n):
    return (m*n)//(gcdFunc(m,n))

# gfg solution you dont need to calculate gcd twice
if __name__ == "__main__":
    m = 98623541
    n = 93043031
    hcf = gcdFunc(m,n)
    # ans2 = gcd(m,n)
    lcm = lcmfunc(m,n)
    print(lcm,hcf)
     