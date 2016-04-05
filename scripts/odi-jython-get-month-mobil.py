"""
Author = laercio.serra@gmail.com
Get the curent month of the billing mobil
10-12-2015 > Laercio Serra > First Version 
"""

import os
import re
import string

# WIN LOCAL_FILE_INPUT
# file_in='C:\Integracao\TELECOM\MOVEL\CLARO_PG1.txt'
# LINUX LOCAL_FILE_INPUT
file_in='/u01/integracao/TELECOM/MOVEL/utf8-CLARO_PG1.txt'

# Abre o arquivo para leitura
srcfile=open(file_in,'r')

# Arquivo de output que conterá os campos de competência
# WIN LOCAL_FILE_OUTPUT
#file_out='C:\Integracao\TELECOM\MOVEL\CLARO_COMPETENCIA.txt'
# LINUX LOCAL_FILE_OUTPUT
file_out='/u01/integracao/TELECOM/MOVEL/DATA_VENCIMENTO.txt'

# Abre o arquivo para gravação
tgtfile=open(file_out,'w')

i=0
numb=0
line=srcfile.readline()

while line:
	list1=line.split(' ') 
	if list1[0]=='Data':
		ltrg='\t'.join(list1)
		tgtfile.write(ltrg)
		break
	else:
		numb=0  

	i+=1
	line=srcfile.readline()

#Fecha os arquivos
srcfile.close()
tgtfile.close()