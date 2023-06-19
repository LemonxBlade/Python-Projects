
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
PDF_reader = PyPDF2.PdfFileReader(book)
pages = PDF_reader.numPages

for num in range(0, pages ):
    page = PDF_reader.getPage(num)
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()