from tkinter import *

from tkinter import filedialog 
import speech_recognition as sr
import pyttsx3

root=Tk()
#root.geometry('500x300')
root.filename = filedialog.askopenfilename(title='Select A File',filetypes=(('wav files', '*.wav'),('all files','*.*')))

# l=Label(root,text=root.filename).pack()
# m=ImageTk.PhotoImage(Image.open(root.filename))
# l1=Label(image=m).pack()



def transcript():
    filename = root.filename
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:    
        audio_data = r.record(source)
        transcript.text = r.recognize_google(audio_data)
        my_text.insert(END,transcript.text)
        
    


def talk():
    

    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(transcript.text)
    engine.runAndWait()
    
    

    
    
    
        

l0 = Label(root, text="Speech to Text").pack()
l1 = Label(root, text="Choose a file").pack()

l2 = Label(root, text=root.filename).pack()


btn1=Button(root,text='transcript',command=transcript).pack()
#print(btn1)
my_text = Text(root)
# text.insert( text)
my_text.pack()


l3 = Label(root, text="Text to Speech").pack()
btn2=Button(root,text='Speak',command=talk).pack()




root.mainloop()
