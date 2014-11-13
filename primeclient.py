####################################################
# RPyC Client Control
# 
# Simple Class designed to "pilot" or 
# RPyC learning, will only work if primeserver
# is running on a computer whether localhost
# or remote location accessible via ip-address
#
#
# designed by Justin Read
#         and Matthew Martorana
#
# For use in OOD Fall 2014
####################################################


# import the RPyC python3.4 plugin
import rpyc

# ask the user where they want to connect
serverAddress = input('Type an ip to connect to ')

# connect to the Service that should be running
c = rpyc.connect(serverAddress, 12345)

# ask the user what number they want to check is prime 
num =int( input('Type a number to check if its prime '))

# this line is where we ask the remote obj or service obj
# if the number that was just input is prime or not
# returns boolean
print(c.root.is_prime(num)) 


# this is where we ask the remote object for a list 
# of all the prime positive numbers up to the selected
# input
print(c.root.get_primes(num))



