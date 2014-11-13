import rpyc
serverAddress = input('Type an ip to connect to ')

c = rpyc.connect(serverAddress, 12345)
c.root
num =int( input('Type a number to check if its prime '))
print(c.root.is_prime(num))
