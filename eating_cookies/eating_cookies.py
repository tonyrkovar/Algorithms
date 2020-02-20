#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, a=1, cache=None,):
  ways = 1
  if n == 0:
    return 1

  combinations = 0

  for i in range(n):
    ways += 1
    
    
    
    
    
    
    
    
    
    
    # for k in range(i):
    #   combinations += 1
    #   print(f"K: {k}, combinations: {combinations}")



  return eating_cookies(n-1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
   


eating_cookies(4)