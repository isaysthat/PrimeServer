import rpyc
import math

from rpyc.utils.server import ThreadedServer
class primeserver(rpyc.Service):
	def on_connect(self):

		pass

	def on_disconnect(self):

		pass

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
if __name__ == "__main__":
	t = ThreadedServer(primeserver, port = 12345)
	t.start()
		
