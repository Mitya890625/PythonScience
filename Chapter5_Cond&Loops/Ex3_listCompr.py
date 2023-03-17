def matrix(x):
    for a in x:  
        print(a[2], end=' ')
    print()
    c2 = [a[2] for a in x]
    print(c2)
    c1_quadr = [2*(a[1]**2) for a in x]
    print(c1_quadr)
    for a in x:
        print(a[1]*a[1]*2, end=' ')
def main():
    matrix( [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
main()