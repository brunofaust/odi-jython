"""
Pull the *.txt files from /home/odi of the server 
ftp.myserver.com into the local directory c:\temp
"""

import snpsftp

ftp = snpsftp.SnpsFTP('ftp.myserver.com', 'mylogin', 'mypasswd')

try:
    ftp.setmode('ASCII')
    ftp.mget('/home/odi', '*.txt', 'c:/temp')
finally:
    ftp.close()
    
    
"""
Push the files *.zip from C:\odi\lib onto ftp.myserver.com in the remote directory
/home/odi/lib
"""

import snpsftp

ftp = snpsftp.SnpsFTP('ftp.myserver.com', 'mylogin', 'mypasswd')

try:
    ftp.setmode('BINARY')
    ftp.mput('C:/odi/lib', '*.zip', '/home/odi/lib')
finally:
    ftp.close()        