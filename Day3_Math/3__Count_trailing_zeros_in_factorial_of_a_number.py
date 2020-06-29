#3__Count_trailing_zeros_in_factorial_of_a_number

N=625
def trailingZeroes(n: int) -> int:
    count = 0
    i = 5 
    while n >= i:
        print(n//i)
        count += n//i
        n = n//i
    return count
if __name__ == "__main__":
    zeros  =trailingZeroes(N)
# dp = [(0,0) for _ in range(N+1)]
# last = (1,0)
# # dp[0:6]=[(1,0),(1,0),(2,0),(6,0),(4,0),(2,1)]
# for i in range(1,N+1):
#     # lsn,zeros = dp[i-1]
#     lsn,zeros = last

#     nlsn = str(lsn*i)
#     # print(nlsn)
#     nlsn_len = len(nlsn)
#     count=0
#     ch = int(nlsn[-1])

#     for j in range(nlsn_len-1,-1,-1):
#         if nlsn[j] !='0':
#             count = nlsn_len-j-1
#             end = j+1
#             break
    
#     zeros+=count    
#     nlsn = int(nlsn[:end])
#     # dp[i] = (nlsn,zeros)
#     last = (nlsn,zeros)
# print(last) 