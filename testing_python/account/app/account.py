#!/usr/bin/env python

import requests

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
   
    def get_current_balance(self, id_num):
       return requests.get("http://some-account-uri/"+id_num)
