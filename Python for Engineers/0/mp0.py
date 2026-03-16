"""
Name: FERNANDO
Date: TODAY
CSC 174 MP0
Statement: Approximate f'(x) using forward and central differences
Specifications:
Input - x, deltax
Output - forward and central approximations to d(sin(x)/dx
- relative errors for each are displayed
"""
import math
 #math library for sine and cosine functions
 #prompt and read the user's x value
x = float(input("Enter any value for x: "))
import math

def main():
 #prompt and read the user's deltax value
 deltax = float(input("Enter a positive value for deltax: "))

 #calculate the y values and y'
 ynm1 = math.sin(x - deltax)
 yn = math.sin(x)
 ynp1 = math.sin(x + deltax)
 yprime = math.cos(x)

 #calculate the derivative approximations
 forward = (ynp1 - yn)/deltax
 central = (ynp1 - ynm1)/(2.0*deltax)

 #display the results
 print("Forward approximation = ", forward,"\nrelative error = ", (yprime - forward)/yprime)
 print("Central approximation = ", central,"\nrelative error = ", (yprime - central)/yprime)
 print(f"Forward approximation = {forward:.4f}")
 print(f"relative error = {(yprime - forward)/yprime:.4f}")
 print(f"Central approximation = {central:.4f}")
 print(f"relative error = {(yprime - central)/yprime:.4f}")
main()

