#!/usr/bin/env python

class ConnectionError(Exception):
    pass

class Account(object):
    def __init__(self, data_interface):
       self.di = data_interface

    def get_account(self,id_num):
       try:
          return self.di.get(id_num)
       except ConnectionError:
          result = "Connection error occured. Try Again."
          return result

