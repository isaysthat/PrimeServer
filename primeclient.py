import rpyc

c = rpyc.connect("localhost", 12345)
c.root
num =int( input('Type a number to check if its prime '))
print(c.root.is_prime(num))
