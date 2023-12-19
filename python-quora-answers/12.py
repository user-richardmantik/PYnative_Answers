# importing library sympy 
from sympy import symbols, Eq, solve 
  
# defining symbols used in equations 
# or unknown variables 
x, y= symbols('x,y') 
  
# defining equations 
eq1 = Eq((x-6*y), 5) 
print("Equation 1:") 
print(eq1) 
  
eq2 = Eq((y-8), 1) 
print("Equation 2") 
print(eq2) 
  
# solving the equation and printing the  
# value of unknown variables 
print("Values of 2 unknown variable are as follows:") 
print(solve((eq1, eq2), (x, y))) 