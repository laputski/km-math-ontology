#Work with PDF
from cStringIO import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import pdfminer.layout
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


def pdf2txt(filename):
    fp= open(filename,'rb')
    doc=PDFDocument(PDFParser(fp))
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    codec='utf-8'
    device=TextConverter(rsrcmgr,retstr,codec=codec,laparams=laparams)
    interpreter=PDFPageInterpreter(rsrcmgr,device)
    lines=""
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
        rstr=retstr.getvalue()
    
        if len(rstr.strip())>0:
            lines+="".join(rstr)
    return lines
    
