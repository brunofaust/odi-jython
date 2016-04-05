"""
Author = laercio.serra@gmail.com
Search records rejects during the load process
10-12-2015 > Laercio Serra > First Version 
15-12-2015 > Laercio Serra > Logical change
"""

<@
 
import java.sql.Connection;
import java.sql.Statement;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
 
conn=odiRef.getJDBCConnection("SRC");
Statement stmt=conn.createStatement();
String result="";
 
// Please change the delimiter here,i.e just change the number
// TAB - 9
// COMMA 44
// GET THE CODING LIST AT http://www.zytrax.com/tech/codes.htm

char delimiter=(char)44;
 
my_query="SELECT 
			ODI_ERR_MESS ERRO, 
			ODPH_NR_PHONE  TELEFONE,
			ODPH_NM_USERNAME  USUARIO,
			ODPH_DS_DIRECTION DEPARTAMENTO,
			ODPH_DS_SUBSCRIPTION PLANO_ASSOCIADO,
			ODPH_DS_STATUS STATUS 
		FROM 
			E$_ODS_PHONE 
		ORDER BY 
			ODPH_NR_PHONE ";
 
// Either provide the columns or select * from all columns
 
ResultSet rs=stmt.executeQuery(my_query);
ResultSetMetaData md=rs.getMetaData();
int numColumns =md.getColumnCount();
 
// Fetch column names
for (int i=1; i<numColumns+1; i++) {
 String columnName = md.getColumnName(i)+ delimiter;
 result+=columnName;
 }
 
result=result.substring(0,result.length()-1);
result+=(char)10;
 
int times=result.length();
 
for (int i=1; i<times ;i++){
 result+="-";
 }
 
result+=(char)10;
 
// Fetching Rows
 
result=result.substring(0,result.length()-1);
result+=(char)10;
 
while (rs.next()) {
 for (int i=1; i<numColumns+1; i++) {
 String  output=rs.getString(md.getColumnName(i))+ delimiter;
 result+=output;
 }
result=result.substring(0,result.length()-1);   
result+=(char)10;
 }
 
// Close Connection
 
stmt.close();
conn.close();
@>