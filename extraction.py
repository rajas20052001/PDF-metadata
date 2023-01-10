'''
import pdfreader
h = open(r'9782329827179_TXT.pdf', 'rb')
d = pdfreader.PDFDocument(h)
print(d.metadata)
'''
import PyPDF2
import os
location = os.getcwd() + '\\input'
_listDir = os.listdir(location)
_listDir_len = len(_listDir)-1
a = 'filename,pages,pagesize\n'
ii = 0
while(ii<=_listDir_len):
    _file = _listDir[ii]
    pdfFileObj = open(location + '/'+_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj,strict=False)
    try:

        p = pdfReader.getPage(0)

        w_in_user_space_units = p.mediaBox.getWidth()
        h_in_user_space_units = p.mediaBox.getHeight()
        w = int(float(p.mediaBox.getWidth()) * 0.352)+1
        h = int(float(p.mediaBox.getHeight()) * 0.352)+1
        a += str(_listDir[ii]+ ','+str(pdfReader.numPages)+','+str(w) + ' * '+ str(h)+'\n')
    except:
        print(str(_listDir[ii])+'not run the pdf')
        
    ii+=1
with open('properties.csv','w') as b:
    b.write(a)
