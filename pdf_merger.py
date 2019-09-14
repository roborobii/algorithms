from PyPDF2 import PdfFileMerger

pdfs = ['recursion2.pdf', 'recursion3.pdf', 'recursion4.pdf', 'recursion5.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()