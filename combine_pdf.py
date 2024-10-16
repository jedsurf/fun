# Script to combine pdf files into one, assuming all are in same directory.
# I made this to combine STAT201A notes located in the same directory as the script;
# just uploading here to have record of how to work w pdf files
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os

files = [i for i in os.listdir() if ".pdf" in i]
files = sorted([i for i in files if ("slides" not in i) and ("lec01" not in i)])
# print(files)
writer = PdfWriter()
ct = 0 
for f in files:
    pdfFileObj = open(f, "rb")
    reader = PdfReader(pdfFileObj)
    for page in reader.pages:
        # media_box = page.mediabox
        # width = float(media_box.width)
        # height = float(media_box.height)
        # print(width, height)
        if ct >= 3: # The first 3 pages of lec02 notes are just a practice problem
            writer.add_page(page)
        ct += 1
        # pageObj = pdfReader.pages[pageNum] # Reads only those that are in the varaible.
        # pdfWriter.add_page(pageObj) # Adds each of the PDFs it's read to a new page.
    pdfFileObj.close()
pdfOutput = open("MT1_combined_lec02-13_notes.pdf", "wb")
writer.write(pdfOutput)
pdfOutput.close()
