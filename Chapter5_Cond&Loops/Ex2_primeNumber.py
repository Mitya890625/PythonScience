def prime_numbers(x):
    i = 2
    while x%i !=0:
        i +=1
    if x/i == 1:
        print("{0:d} is a prime number".format(x)) 
    else:
        print("{0:d} is not a prime number".format(x))
    print("the smallest factor of {0:d} is {1:d}".format(x,i))
def main():
    prime_numbers(947431)
main()