import math
#Definisi fungsi ln(x)
def func_e(x, n):
    l_n = 0
    for i in range(n):
        l_n += x**i/math.factorial(i)

    return l_n

x = 1.5

for i in range(1,11):
    l_n = func_e(x,i)
    e_exp = math.ln(x)
    l_error = abs(l_n - e_exp)

print(l_n)
