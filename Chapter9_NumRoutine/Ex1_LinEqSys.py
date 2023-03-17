import scipy.linalg as sclin

def linear_equation():
    A = [[1,-2, 9, 13], [-5,1,6,-7], [4,8,-4,-2], [8,5,-7,1]]
    b = [1,-3,-2,5]
    sol = sclin.solve(A,b)
    print(sol)
    
linear_equation()