import PyPDF2
import pyttsx3
path = open('file.pdf', 'rb')
read = PyPDF2.PdfReader(path)

# the page with which you want to start
# this will read the page of 25th page.
page = read.pages[1]

# extracting the text from the PDF
text = page.extract_text()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
