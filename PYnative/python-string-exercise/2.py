import math

s1 = "Ault"
s2 = "Kelly"

output_str = s1[0:math.floor(len(s1)/2)] + s2 + s1[math.floor(len(s1)/2):len(s1)]
print(output_str)