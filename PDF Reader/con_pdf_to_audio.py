import pyttsx3
import PyPDF2

file = open("news.pdf", mode="rb")
pdf_reder = PyPDF2.PdfReader(file)
pages = pdf_reder.numPages
print(pages)

roni = pyttsx3.init()

for i in range(1,pages):

    page = pdf_reder.getPage(2)
    text = page.extractText()
    voices = roni.getProperty('voices')

    # changing index, changes voices. 1 for female or 0 for male
    roni.setProperty('voice', voices[1].id)

    roni.say(text)
    roni.runAndWait()