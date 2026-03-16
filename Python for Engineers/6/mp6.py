'''
*************************************************************************
* Name: Your name                                                 CSC 174
* Date: Today's date                                              MP 6   
*************************************************************************
* Statement: Find various vector and scalar related quantities using the
*            vn object defined in the file vn.py
* Specifications:
* Input  - a 4 dimensional vector w from the keyboard
* Invokes- a constructor to initialize a vector v
*        - an assignment operator to support x = v - w
* Output - to the monitor
*        - v's 1 norm, w's 2 norm and infinity norm, v dot w
*        - cos(theta) of hyper-angle determined by v and w
*        - 2 * v, v + w, v - w, v tensor w 
*************************************************************************
'''
import math
from vn import vn
'''
*************************************************************
* dot() method to return float dot product of vn a and vn b
* receives: vn values a & b
* returns: a1*b1 + a2*b2 + ... + an*bn
*************************************************************
'''
# code function dot below


'''
********************************************************
* normp() function to return float p-norm of vn a
* receives: vn a and integer p
* returns: (|a1|^p + |a2|^p + ... + |an|^p)^(1/p)
********************************************************
'''
def normp(a, p):
    temp = 0.0
    if p > 0:
        # after initializing reduction variable, update by visiting
        # each element in the vn argument raised to the p'th power
        for i in range(vn.VECLENGTH):
            temp += math.pow(math.fabs(a.get(i)), p)
        # return the p'th root of the sum               
        return math.pow(temp, 1.0/p)
    else:
        print("normp() received p = ", p, ", returning 0", sep="")
        return temp
    
'''
**************************************************************
* norminf() function to return float infinity norm of vn a
* receives: vn a 
* returns: max(|a1|, |a2|, ..., |an|)
**************************************************************
'''
# code function norminf below


'''
*************************************************************************
* scalarvn() function to return the vn scalar product of float k and vn a
* receives: real k and vn a
* returns: < k * a1, k * a2, ..., k * an >
************************************************************************
'''
# code function scalarvn below


'''
******************************************************************
* sumvn() function to return the vn sum of vn a and vn b
* receives: vn a and vn b
* returns: < a1 + b1, a2 + b2, ..., an + bn >
******************************************************************
'''
# code function sumvn below


'''
*********************************************************************
* diffvn() function to return the vn difference of vn a minus vn b
* receives: vn a and vn b
* returns: < a1 - b1, a2 - b2, ..., an - bn >
*********************************************************************
'''
def diffvn(a, b):
    temp = vn()
    # visit each of a and b and store the difference a minus b
    for i in range(vn.VECLENGTH):
        temp.set(i, a.get(i) - b.get(i))
    return temp

'''
**********************************************************************
* tensor() method to return the double 4x4 array of vn a tensor vn b
* receives: vn a and vn b
* returns: double 4x4 array with (i'th row, j'th column) = (ai * bj)
**********************************************************************
'''
def tensor(a, b):
    # assign a float 4x4 array
    tens = [[0.0]*vn.VECLENGTH]*vn.VECLENGTH
    # visit each array element and initialize with ai * bj
    for i in range(vn.VECLENGTH):
        for j in range(vn.VECLENGTH):
            tens[i][j] = a.get(i)*b.get(j)
    return tens

def main():
    # invoke __init__ function for vn objects
    w = vn()
    x = vn()
    v = vn(1.0, 2.0, -1.0, -2.0)

    # 1) test input function
    w.input()

    # 2) test __str__ function
    print("v and w")
    print(v)
    print(w)
    
    # 3) invocation of scalar functions: norms, dot etc.
    print(f"v norm 1 = {normp(v, 1):4.1f}\nw norm 2 = {normp(w, 2):4.1f}")
    #print(f"w norm inf = {norminf(w):4.1f}\nv dot w = {dot(v, w):4.1f")
    
    # 4) code the output statement to display the
    #cos(theta) determined by v and w below

    # 5) invocation and display of vn function scalar product
    # print("2 * v =", scalarvn(2, v))

    # 6) invocation and display of vn function sum
    #print("v + w =", sumvn(v, w))

    # 7) test assignment function and invoke function difference
    x.equals(diffvn(v, w))

    # 8) display of vn function difference
    print("v - w =", x)

    # 9) invoke tensor function and store result in 4x4 array tensorvw
    tensorvw = tensor(v, w)

    # 10) display tensor product of vn v with vn w
    print("v tensor w =")
    for i in range(vn.VECLENGTH):
        # loop over each column
        for j in range(vn.VECLENGTH):
            # loop over each row
            print(f"{tensorvw[i][j]:6.1f}", end="")
        print()
# end of main program

if __name__ == '__main__':
    main()
