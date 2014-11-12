import rpyc

c = rpyc.connect("localhost", 12345) #replacing "localhost" with an ip address 
#will connect to a service at that address
c.root
num =int( input('Type a number to check if its prime '))
print(c.root.is_prime(num)) #calls the service's method is_prime
