'''
*************************************************************************
* Name: FERNANDO CHIAVERINI ALBANO PEREIRA                        CSC 174
* Date: 2025-06-16                                                MP 1   
*************************************************************************
* Statement: Interpolate y = N*e^(k*x) between (x1, y1) and (x2, y2)
* Specifications:
* Input - x1, y1, x2, y2, the given points
*       - xinterp, the x value to be interpolated
* Output - exponential interpolating equation y = N*e^(k*x)
*        - y value corresponding to xinterp
*************************************************************************
'''
import math
def main():
    # 1) prompt for and input x1
    x1 = float(input("Enter x1:"))

    # 2) prompt for and input y1
    y1 = float(input("Enter y1:"))

    # 3) prompt for and input x2
    x2 = float(input("Enter x2:"))

    # 4) prompt for and input y2
    y2 = float(input("Enter y2:"))

    # 5) calculate k
    k = (math.log(y2) - math.log(y1))/(x2-x1)


    # 6) calculate N0
    n0 = math.exp(math.log(y1) - (k*x1))

    # 7) display the exponential model
    #print(f"Exponential model : y = {n0:.3f}*exp({k:.3f} * x)\n")
    #print(f"Exponential model : y = {n0:.3f}*e^({k:.3f} * x)\n")
    print(f"Exponential model : y = {n0:.3f}*e**({k:.3f} * x)\n")

    # // 8) prompt for and input xinterp
    xinterp = float(input("Enter x value for interpolation:"))


    # // 9) display the interpolated y value
    yinterp = n0*math.exp(k*xinterp)
    print(f'{yinterp:0.3f}')
    
main()
