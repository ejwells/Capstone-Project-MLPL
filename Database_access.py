# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:10:00 2016

@author: titou
"""

import MySQLdb
#MySQL host: rosencrantz.berkeley.edu
#user: uspto
#password: ferrisbueller
#port: 3306
connection = MySQLdb.connect(
                host = 'rosencrantz.berkeley.edu',
                user = 'uspto',
                passwd = 'ferrisbueller')  # create the connection
                
cursor=connection.cursor()

#get as input a patent number and return True if it is in the DB
def is_patentno_in_db(patentno):
    cursor.execute("USE uspto") # select the database
    cursor.execute("SELECT * FROM uspto.patent Where number = '"+str(patentno)+"'")
    tables = cursor.fetchall()
    return not(tables==())

#get as input a patent owner and return True if it owns a patent of the DB
def is_owner_in_db(owner):
    cursor.execute("USE uspto") # select the database
    cursor.execute("select * from assignee where organization = '"+owner+"'")
    tables = cursor.fetchall()
    return not(tables==())

#take as input an owner or a patent number and returns all data
def get_data(obj):
    cursor.execute("USE uspto") # select the database
    if(isinstance(obj,str)):
        owner=obj
        cursor.execute("SELECT *FROM patent as p , assignee as a, claim as c WHERE (a.id IN (select assignee_id From patent_assignee as pa,patent as p where p.id=pa.patent_id ) AND (c.uuid IN (select uuid from claim as c, patent as p where p.id=c.patent_id))AND a.organization='"+owner+"')")
    else:
        patentno=str(obj)
        cursor.execute("SELECT *FROM patent as p , assignee as a, claim as c WHERE (a.id IN (select assignee_id From patent_assignee as pa,patent as p where p.id=pa.patent_id ) AND (c.uuid IN (select uuid from claim as c, patent as p where p.id=c.patent_id))AND p.number='"+patentno+"')")
    tables=cursor.fetchall()
    return tables