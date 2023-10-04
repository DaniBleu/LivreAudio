import pyttsx3
import PyPDF3


droid = pyttsx3.init()
droid.say("good morning Daniel, i am a droid to thirtien generation, and my name is nepturne")


livre = open('Bronte-Les_Hauts_de_Hurle-vent.pdf','rb')
lecture = PyPDF3.PdfFileReader(livre)
pages = lecture.numPages
print(pages)
debutLecture = lecture.getPage(0)
texte = debutLecture.extractTexte()
droid.say(texte)

droid.runAndWait()