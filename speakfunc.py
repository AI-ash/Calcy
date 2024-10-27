import pyttsx3
def s():
    print()
def speak(audio):
     engine = pyttsx3.init('sapi5')
     voices = engine.getProperty('voices')
     #print(voices[1].id)
     engine.setProperty('voice',voices[1].id)
     engine.setProperty('rate', 175)
     #speak function
     engine.say(audio)
     print(audio)
     engine.runAndWait()

def speak1(audio):
     engine = pyttsx3.init('sapi5')
     voices = engine.getProperty('voices')
     #print(voices[1].id)
     engine.setProperty('voice',voices[0].id)
     engine.setProperty('rate', 175)
     #speak function
     engine.say(audio)
     engine.runAndWait()

if __name__=='__main__':
    s()