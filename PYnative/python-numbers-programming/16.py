# importing library sympy 
from sympy import symbols, Eq, solve 
  
# defining symbols used in equations 
# or unknown variables 
w, h, d= symbols('w, h, d') 
  
# defining equations 
eq1 = Eq((h-w), 5) 
print("Equation 1:") 
print(eq1) 
  
eq2 = Eq((h-5*d), 0) 
print("Equation 2") 
print(eq2) 

eq3 = Eq((d-3), 5) 
print("Equation 3") 
print(eq3) 
  
# solving the equation and printing the  
# value of unknown variables 
print("Values of 3 unknown variable are as follows:") 
print(solve((eq1, eq2, eq3), (w, h, d))) 