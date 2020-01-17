# -*- encoding: utf-8 -*-
'''
@File    :   bisection.py
@Time    :   2019/12/06 11:04:53
@Author  :   Simon 
@Version :   1.0
@Desc    :   二等分
'''

# here put the import lib
import math

def bisection(
    function, a, b
): # find where the function become 0 in [a, b] using bisection
    
    start = a
    end = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif(
        function(a) * function(b) > 0
    ): # if none of these are root and they are both positive or negative,
       # then his algorithm can't find the root
        print("couldn't find root in [a, b]")
        return
    else:
        mid = start + (end - start) / 2.0
        while abs(start - mid) > 10 ** -7: # until we achieve precise equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid



def f(x):
    return math.pow(x, 2) - 2 * x - 5

if __name__ == "__main__":
    print(bisection(f, 1, 1000))