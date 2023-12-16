# importing library sympy 
from sympy import symbols, Eq, solve 
  
# defining symbols used in equations 
# or unknown variables 
x, y= symbols('x,y') 
  
# defining equations 
eq1 = Eq((x%2-0), 1) 
print("Equation 1:") 
print(eq1) 
  
eq2 = Eq((x%3-0), 2) 
print("Equation 2") 
print(eq2) 

eq3 = Eq((x%4-0), 3) 
print("Equation 3") 
print(eq3) 

eq4 = Eq((x%5-0), 4) 
print("Equation 4") 
print(eq4) 

eq5 = Eq((x%6-0), 5) 
print("Equation 5") 
print(eq5) 

eq6 = Eq((x%7-0), 0) 
print("Equation 6") 
print(eq6) 

  
# solving the equation and printing the  
# value of unknown variables 
print("Values of 1 unknown variable are as follows:") 
print(solve((eq1, eq2, eq3, eq4, eq5, eq6), (x))) 