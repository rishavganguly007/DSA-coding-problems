# code: https://www.naukri.com/code360/problems/missing-number_6680467


def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    val = sum(a)
    total = (N * (N + 1)) // 2                                                               
    return abs(total - val)
