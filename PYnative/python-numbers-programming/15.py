# importing library sympy 
from sympy import symbols, Eq, solve 
  
# defining symbols used in equations 
# or unknown variables 
x = symbols('x') 
  
# defining equations 
eq1 = Eq((2*x/3), 4) 
print("Equation 1:") 
print(eq1) 
  
# solving the equation and printing the  
# value of unknown variables 
print("Values of 1 unknown variable are as follows:") 
print(solve((eq1), (x))) 