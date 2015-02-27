#!/usr/bin/env python

class Calculate (object):
  def add(self,x,y):
      """Takes two integers and adds them together to produce
      the result.

      >>> c = Calculate()

      >>> c.add(25,125)
      150

      >>> c.add(1,2)
      3
      """

      if type(x) == int and type(y) ==int:
         return x + y
      else:
         raise TypeError("Invalid type: {} and {}".format(type(x),type(y)))

if __name__=='__main__': #pragma: no cover
  import doctest
  doctest.testmod()
  calc=Calculate()
  result=calc.add(2,2)
  print result
