import numpy as np

def perimeter_of_figure(d, n1, n2, n3, n4, n5, n6):
    p1 = n1 * d * np.sin(np.pi/n1)
    p2 = n2 * d * np.sin(np.pi/n2)
    p3 = n3 * d * np.sin(np.pi/n3)
    p4 = n4 * d * np.sin(np.pi/n4)
    p5 = n5 * d * np.sin(np.pi/n5)
    p6 = n6 * d * np.sin(np.pi/n6)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
def main():
    perimeter_of_figure(1, 3, 4, 5, 100, 10000, 100000)
main()