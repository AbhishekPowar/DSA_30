# https://leetcode.com/problems/pascals-triangle/solution/


def generate(numRows: int):
    pascal = []
    if numRows:
        base = [1]
        pascal.append(base)
        for i in range(numRows-1):
            nextLine = []
            nextLine.append(base[0])
            base_len = len(base)
            for idx in range(base_len-1):
                nextLine.append(base[idx]+base[idx+1])
            nextLine.append(base[-1])
            base = nextLine
            pascal.append(base)
    return pascal


if __name__ == "__main__":
    N = 5
    print(*generate(N), sep='\n')
