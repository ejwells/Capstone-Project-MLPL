import MySQLdb
def connection(organization, patent_id):
    try:
        connection = MySQLdb.connect(
            host = 'rosencrantz.berkeley.edu',
            user = 'uspto',
            passwd = 'ferrisbueller')  #Creates the connection
        #return "Success"
        cursor = connection.cursor() 
        #Gets the assigne_id
        cursor.execute("""SELECT assignee.id, assignee.name_first, assignee.name_last, assignee.organization, patent_assignee.patent_id 
                        FROM uspto.assignee 
                        INNER JOIN uspto.patent_assignee ON assignee.id = patent_assignee.assignee_id 
                        WHERE organization like %s and patent_assignee.patent_id = %s;""", 
                       ('%'+organization+'%', patent_id,))
        tables = cursor.fetchall() 
        if not tables:
            return "Patent ID does not match with organization."
        return tables
    except MySQLdb.Error:
        return "ERROR IN CONNECTION"

print connection("Myriad Genetics, Inc", '5693473')