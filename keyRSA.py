from math import gcd

def isPrime(n):
    if n==2 or n==3:
        return True

    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    
    return True

def generateKey(p, q):
    n= p*q            
    phi= (p-1)*(q-1)  

    for e in range(2, phi): 
        if gcd(e, phi)== 1: 
            break              

    for d in range(1, phi):
        if (d*e)%phi == 1:  
            break

    return n, e, d

def main():
    p, q = map(int, input("Enter two prime number p and q: ").split())

    if isPrime(p) and isPrime(q) == False:
        return print("Please enter prime numbers.")

    n, e, d = generateKey(p, q)

    print("Public key(n, e) is ({}, {})".format(n, e))
    print("Private key(n, d) is ({}, {})".format(n, d))

if __name__== "__main__":
    main()