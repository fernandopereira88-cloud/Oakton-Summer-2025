'''
*************************************************************************
* Name: FERNANDO CHIAVERINI ALBANO PEREIRA                        CSC 174
* Date: 07/02/2025                                                MP 3   
*************************************************************************
* Statement: Approximate the integral of 1/(1+x^2) from a to b
* Specifications:
* Input - a and b, the limits of integration and n, the number of panels
* Output - message indicating function used (trapezoid or simpson)
*        - approximation to the integral
*        - relative error
*************************************************************************
'''
import math

def main():
    # all variables must be declared
    #n = 1
    Sapprox = 0
    
    # 1) prompt and read right hand limit of integration
    a = float(input("Enter the right hand value:"))
    # 2) prompt and read left hand limit of integration
    b = float(input("Enter the left hand value:"))

    # Extra Credit - Checking whether a > b and adjusting
    if a > b:
        temp = b
        b = a
        a = temp
        
    # 3) calculate known result for error analysis
    Stheory = math.atan(b)-math.atan(a)
    
    # 4) prompt and read the number of panels
    n = int(input("Enter the number of panels: "))
    
    # Extra Credit - Enforcing that number of panels provided is a positive number
    while  n <= 0:
        n = int(input("Enter a POSITIVE number for the number of panels: "))
    

    # 5) determine panel width
    deltax = (b - a)/n
    
    # 6) test parity
    if n % 2 == 0:
        # 7) display method
        print("Using Simpson's method")

        # 8) initialize reduction to 0
        SsimpEven = 0
        SsimpOdd = 0
        
        #  9) odd interior points
        # 10) increase odd sum by y
        for i in range (1,n,2):
            SsimpOdd += 1.0/(1.0+math.pow(a+i*deltax,2.0))

        # 11) even interior points
        # 12) increase even sum by y        
        for i in range (2,n-1,2):
            SsimpEven += 1.0/(1.0+math.pow(a+i*deltax,2.0))            

        # 13) calculate sum for Simpson
        Sapprox = (deltax/3)*((1/(1+a**2))+(1/(1+b**2)+4*SsimpOdd+2*SsimpEven))
        
    else:        
        # 14) display method
        print("Using Trapezoid")

        # 15) initialize reduction at endpoints
        Sapprox = ((1/(1+a**2)+(1/(1+b**2))))/2
                        
        # 16) loop over all interior points
        # 17) increase sum by y                        
        for i in range(1,n):
            Sapprox +=  (1.0/(1.0+(a+i*deltax)*(a+i*deltax)))                    

        # 18) factor in deltax
        Sapprox = Sapprox*deltax
                        
        # 19) display result and error analysis
    epsilon = abs(Stheory - Sapprox)/Stheory
                    
    print(f'Integral from {a} to {b}')
    print(f'Approximation: {Sapprox:,.6f}')
    print(f'Theory: {Stheory:,.6f}')
    print(f'Relative Error: {epsilon:,.6e}')

# end main function
if __name__ == '__main__':
    main()
    
