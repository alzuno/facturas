#alzuno
#February 5th 2017
#Use this to rename electronic invoices from Ecuador
#To use, run: python renameFacts.py /folder/where/the/invoices/are

import os,glob,sys,re
folder=sys.argv[1]
os.chdir(folder)

#Print the current directory
retval = os.getcwd()
print "Current working directory %s" % retval

#Find the Razon Social ,full invoice number and invoice date.

pattern = re.compile("<razonSocial>(.*?)<\/razonSocial>[\s\S]*<estab>(.*?)<\/estab>[\s\S]*<ptoEmi>(.*?)<\/ptoEmi>[\s\S]*<secuencial>(.*?)<\/secuencial>[\s\S]*<fechaEmision>(.*?)<\/fechaEmision>[\s\S]*",re.DOTALL|re.MULTILINE|re.IGNORECASE)

for files in glob.glob("*.xml"):
    data=open(files).read()
    if pattern.search(data):
        #get the data from the pattern
        patternData = pattern.findall(data)[0]
        #get the newfilename 'Date + Razon Social + NumFact'
        filename = patternData[4].replace("/", "-") + ' - ' + patternData[0] + ' - Fact ' + patternData[1] + '-' + patternData[2] + '-' + patternData[3]
        try:
            os.rename(files,os.path.join(folder,filename+".xml"))
        except Exception,e:
            print e
        else:
            print "%s renamed to %s.xml" %(files,filename)
