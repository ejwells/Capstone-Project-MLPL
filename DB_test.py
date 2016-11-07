# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:22:09 2016

@author: titou
"""

import Database_access


#Test is_patentno_in_db
print("should return true")
print (Database_access.is_patentno_in_db(3858241))
print("should return False")
print (Database_access.is_patentno_in_db(000))

'''
#Test is_owner_in_db
owner="SEC Live, LLC"
print("should return true")
print (Database_access.is_owner_in_db(owner))
print("should return false")
print (Database_access.is_owner_in_db("silhse"))
'''

#test get_data
'''owner="DIL SHAM VENTURES"
patentno=3858241
print Database_access.get_data(patentno)'''