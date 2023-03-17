import numpy as np

def quadratic_eq(a, b, c):
    a = a+0j
    x1 = (-b + np.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (-b - np.sqrt((b*b)-(4*a*c)))/(2*a)
    print("x1 is = " + str(x1))
    print("x2 is = " + str(x2))
def main():
    quadratic_eq(1.0, 2, 3)
main()