from PyPDF2 import PdfFileMerger

pdfs = ['test0.pdf','test1.pdf', 'test2.pdf', 'test3.pdf']

outfile = PdfFileMerger()

for f in pdfs:
    outfile.append(open(f, 'rb'))

outfile.write(open('result.pdf', 'wb'))