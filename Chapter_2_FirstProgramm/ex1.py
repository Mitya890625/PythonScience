def find_h_and_v(g, h0, v0, t):
    print("Initial height is = " + str(h0) + " m")
    print("Initial velocity is = " + str(v0) + " m/s")
    h = h0 + v0*t - (0.5*(g*(t*t)))
    v = v0 - g*t
    print("Height is = " + str(h) + " m")
    print("Velocity is = " + str(v) + " m/s") 
def main():
    find_h_and_v(9.8, 1.6, 14.2, 2)
main()