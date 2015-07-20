#Начальный шаблон для поиска теорем
import re
from pdfconverter import*
#Функция извлекает блоки из текста, которые начинаются "названия" теоремы, 
#например, "Theorem 1.1." и заканчиваются "Proof."
def extract(filename):
    text=pdf2txt(filename)
    patt1=r'Theorem [0-9]\.[0-9]\..*?Proof\.'
    blocks=re.findall(patt1, text, re.S)
    return blocks