import pyodbc as odbc
#print (odbc.drivers())

def connect_sql():
    driver_name= 'ODBC Driver 17 for SQL Server'
    server_name='DESKTOP-RQ7K6LL\SQLEXPRESS'
    database_name='collegedb'
    connection_string = f"""DRIVER={{{driver_name}}};
    SERVER={server_name};
    DATABASE={database_name};
    trusted_connection=yes;
    encrypt=no"""
    try:
        CONNECTION= odbc.connect(connection_string)
        print("successfully connected")

    except:
        print("error connecting!")

    return CONNECTION
