import numpy as np
def box():
    a_box = np.zeros((8,8), dtype=int)
    a_box[0,:] = 1
    a_box[:,0] = 1
    a_box[7,:] = 1
    a_box[:,7] = 1
    print(a_box.size, a_box.shape, a_box.mean(), a_box.std())
    print(a_box)
def checkerboard():
    b_checkerboard = np.zeros((8,8), dtype=int)
    b_checkerboard[1::2,::2] = 1
    b_checkerboard[::2,1::2] = 1
    print(b_checkerboard)
    print(b_checkerboard.size, b_checkerboard.shape, b_checkerboard.mean(), b_checkerboard.std())
def negNotdiv3():
    c = np.arange(2, 50, 5)
    c[c%3!=0] = -c[c%3!=0]
    print(c)
    print(c.size, c.shape, c.mean(), c.std())
def main():
    box()
    checkerboard()
    negNotdiv3()
main()