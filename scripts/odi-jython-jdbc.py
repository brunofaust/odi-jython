"""
The following example shows how to use the JDBC API to connect to a database, 
to run a SQL query and write the result into a file.
"""
import java.sql as sql
import java.lang as lang

def main():
    driver, url, user, passwd = ('oracle.jdbc.driver.OracleDriver',
                                'jdbc:oracle:thin:@myserver:1521:mysid',
                                'myuser', 'mypasswd')
    ##### Register Driver
    lang.Class.forName(driver)
    ##### Create a Connection Object
    myCon = sql.DriverManager.getConnection(url, user, passwd)
    f = open('c:/temp/jdbc_res.txt', 'w')
    try:
        ##### Create a Statement
        myStmt = myCon.createStatement()
        ##### Run a Select Query and get a Result Set
        myRs = myStmt.executeQuery("select TABLE_NAME, OWNER from ALL_TABLES
        where TABLE_NAME like 'SNP%'")
        ##### Loop over the Result Set and print the result in a file
        while (myRs.next()):
            print >> f , "%s\t%s" %(myRs.getString("TABLE_NAME"),
            myRs.getString("OWNER") )
    finally:
        myCon.close()
        f.close()
### Entry Point of the program
if __name__ == '__main__':
    main()