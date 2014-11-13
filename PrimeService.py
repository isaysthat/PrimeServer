#!/usr/bin/python3.4

############################################################
#
# PrimeService class is used to return a list of prime numbers
# from 2->x 
#
# Created by Matt Martorana
# 
############   NOTE   #############
# not commented below due to replacement
# primeserver.py
# USE AT YOUR OWN RISK
###################################
#
# 1st draft - rejected and replaced by primeserver.py
# For use in OOD Fall 2014
#
############################################################

import rpyc
import math
from rpyc.utils.server import ThreadedServer

class PrimeService(rpyc.Service):
    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass
 
    

    def exposed_test_prime(self, x): # this is an exposed method
        
        primeList = []


        if x == 1:	
            return primeList
        if x == 2:
            primeList.append(x)
            return primeList

        for c in range(2,x):
            primeList.append(c)
        

        for n in range (2,x):
            for j in range (2,n):
                if (n%j) == 0:
                    primeList.remove(n)
                    break
        return primeList

if __name__ == '__main__':
   s = ThreadedServer(PrimeService, port=12345)
   s.start()
   
