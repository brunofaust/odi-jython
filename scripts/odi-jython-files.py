"""
PART 1
Read From and Write to a File
The SRC_AGE_GROUP.txt file contains records where the columns are separated by ; 
The following example transforms the SRC_AGE_GROUP.txt file into a new file,
SRC_AGE_GROUP_NEW.txt using tabulations as separators.
This example uses the split() string methods to determine the list of fields 
separated by ; and join() to rebuild a new string separated by tabulations ('\t').
"""
fsrc = open('c:/odi/demo/file/SRC_AGE_GROUP.txt', 'r')
ftrg = open('c:/odi/demo/file/SRC_AGE_GROUP_NEW.txt', 'w')
try:
    for lsrc in fsrc.readlines():
        # get the list of values separated by ;
        valueList = lsrc.split(';')
        # transform this list of values to a string separated by a tab ('\t')
        ltrg = '\t'.join(valueList)
        # write the new string to the target file
        ftrg.write(ltrg)
finally:
    fsrc.close()
    ftrg.close()

"""
PART 2
The method readlines() in the above example loads the entire file into memory. 
It should only be used for small files. For larger files, use the readline() 
method as in the following example. 
readline() will read the lines one by one.
"""
fsrc = open('c:/odi/demo/file/SRC_AGE_GROUP.txt', 'r')
ftrg = open('c:/odi/demo/file/SRC_AGE_GROUP_NEW.txt', 'w')
try:
    lsrc=fsrc.readline()
    while (lsrc):
        valueList = lsrc.split(';')
        ltrg = '\t'.join(valueList)
        ftrg.write(ltrg)
        lsrc=fsrc.readline()
finally:
fsrc.close()
ftrg.close()