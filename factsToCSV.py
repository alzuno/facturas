#Alvaro Zuno
#January 22nd 2017
#Use this to rename electronic invoices from Ecuador
#To use, run: python renameFact.py \folder\where\the\invoices\are outputfile.csv

import os,glob,sys,re,csv
input_folder=sys.argv[1]
output_file=sys.argv[2]
os.chdir(input_folder)

#Print the current directory
current_dir = os.getcwd()
print "Current working directory %s" % current_dir
print "Current output file %s" % output_file

#Find the 'Razon Social' and full invoice number

pattern = re.compile("<razonSocial>(.*?)<\/razonSocial>[\s\S]*<estab>(.*?)<\/estab>[\s\S]*<ptoEmi>(.*?)<\/ptoEmi>[\s\S]*<secuencial>(.*?)<\/secuencial>",re.DOTALL|re.MULTILINE|re.IGNORECASE)

with open(output_file, 'w') as csv_output_file:
    for files in glob.glob("*.xml"):
        data=open(files).read()
        if pattern.search(data):
            invoice_data = pattern.findall(data)[0] #get the new file name
            try:
                filewriter = csv.writer(csv_output_file)
                filewriter.writerow(invoice_data)
            except Exception,e:
                print e
            else:
                print "%s added to %s" %(files,output_file)
