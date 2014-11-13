#!/usr/bin/python3.4

###################################################
# primeserver class created by Jusin Read
#                   edited by Matt Martorana
#
# Server to be used in conjuction with any 
# client computer that has reason to need 
# to figure out prime numbers. 
#
# For use in OOD Fall 2014
###################################################


# proper imports
import rpyc
import math
from rpyc.utils.server import ThreadedServer

# create primeserver Class 
class primeserver(rpyc.Service):
    
    # Method used if we wanted to contact client first thing 
    def on_connect(self):

        pass
    # Method used if we wanted to contact client on disconnect
    def on_disconnect(self):

        pass


    # Method to determine wether or not number given is prime
    # 
    # @params self, int 
    # @return boolean
    def exposed_is_prime(self,x):
        if x == 1:	
            return False
        if x == 2:
            return True
        prime = True
        for n in range (2,x):
            if x%n ==0:
                prime = False
        return prime
    
    # Method used to return a list that has all prime numers
    # from 2 all the way up to the integer given
    #
    # @params self, int 
    # @return array
    def exposed_get_primes(self, x): # this is an exposed method
        
        primeList = []
        
        # trivial cases
        if x == 1:	
            return primeList
        if x == 2:
            primeList.append(x)
            return primeList
        
        # Logic used below:
        #
        # 1) We are to put every integer from 2->x into a list
        # 2) The outside loop loops through all numbers 2->x
        # 3) The inside loop loops from 2->(wherever the outside
        #     loop is at the current moment) to check if outside 
        #     loop number is not prime by the mod if statement
        # 4) If the if statement returns true then remove that 
        #     number from the list and break out of inner loop
        # 5) Once all not primes are removed then we return a list 
        #     to the client
        #

        for c in range(2,x):
            primeList.append(c)
        
        for i in range (2,x):
            for j in range (2,i):
                if (i%j) == 0:
                    primeList.remove(n)
                    break
        return primeList

# needed code to instantiate simple server
if __name__ == "__main__":
    t = ThreadedServer(primeserver, port = 12345)
    t.start()
		
