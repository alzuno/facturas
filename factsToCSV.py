#Alvaro Zuno
#January 22nd 2017
#Use this to rename electronic invoices from Ecuador
#To use, run: python renameFact.py \folder\where\the\invoices\are

import os,glob,sys,re
folder=sys.argv[1]
os.chdir(folder)

#Print the current directory
retval = os.getcwd()
print "Current working directory %s" % retval

#Find the 'Razon Social' and full invoice number

pattern = re.compile("<razonSocial>(.*?)<\/razonSocial>[\s\S]*<estab>(.*?)<\/estab>[\s\S]*<ptoEmi>(.*?)<\/ptoEmi>[\s\S]*<secuencial>(.*?)<\/secuencial>",re.DOTALL|re.MULTILINE|re.IGNORECASE)

for files in glob.glob("*.xml"):
    data=open(files).read()
    if pattern.search(data):
        newfilename = pattern.findall(data)[0] #get the new file name
        newestfilename = newfilename[0] + ' ' + newfilename[1] + '-' + newfilename[2] + '-' + newfilename[3]
        try:
            os.rename(files,os.path.join(folder,newestfilename+".xml"))
        except Exception,e:
            print e
        else:
            print "%s renamed to %s.xml" %(files,newestfilename)
