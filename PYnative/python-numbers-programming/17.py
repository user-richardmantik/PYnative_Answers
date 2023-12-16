# importing library sympy 
from sympy import symbols, Eq, solve 
  
# defining symbols used in equations 
# or unknown variables 
w, d= symbols('w, d')
  
# defining equations 
eq1 = Eq((w-3*d), 0) 
print("Equation 1:") 
print(eq1) 
  
eq2 = Eq(((w-6)*(d-6)), 180) 
print("Equation 2:") 
print(eq2) 
  
# solving the equation and printing the  
# value of unknown variables 
print("Values of 2 unknown variable are as follows:") 
print(solve((eq1, eq2), (w, d))) 