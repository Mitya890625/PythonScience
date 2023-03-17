def fact_for(x):
    fact=1
    for i in range(1, x+1):
        fact = fact * i    
    print(fact)
def fact_while(x):
    fact, i_while =1,1
    while i_while <=x:
        fact = fact * i_while
        i_while += 1
    print(fact)
def main():
    fact_for(10)
    fact_while(10)
main()