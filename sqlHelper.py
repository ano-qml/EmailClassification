import MySQLdb

def sqlConnect():
    DB = 'fit_emails'
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '123456'
    conn = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD)
    return conn

def sql_query(query):
    conn = sqlConnect()
    cursor = conn.cursor()
    sql = """%s"""%(query)
    cursor.execute(sql)
    cursor.close()
    conn.close()
    return

def sql_queryRows(table, condition):
    conn = sqlConnect()
    cursor = conn.cursor()
    sql = 'SELECT * FROM %s %s'
    cursor.execute(sql %(table, condition))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def sql_queryRow(table, id):
    conn = sqlConnect()
    cursor = conn.cursor()
    sql = 'select * from %s where id = %s'
    cursor.execute(sql %(table, id))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def sql_insert(table, fields, values):
    conn = sqlConnect()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO %s(%s) VALUES(%s)""",(table, fields, ','.join(values)))
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    return

def sql_update():
    return

def sql_delete():
    return

def mySQLtest():
    cursor = sqlConnect()
    sql = """show tables;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results