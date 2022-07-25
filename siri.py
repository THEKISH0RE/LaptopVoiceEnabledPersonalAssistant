import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import sys




engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices') #print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishme():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("iinddrraya kaalai vanakam BOSS")
  elif hour>=12 and hour<16:
    speak("good afternoon BOSS")
  else:
    speak("good evening BOSS")

  speak("I am back boss..")

def takecommand():
  r=sr.Recognizer()
  with sr.Microphone() as sourse:
    print("listening...")
    r.pause_threshold=1
    audio=r.listen(sourse)
  try:
    print("Wait for few moments")
    query=r.recognize_google(audio,language='en-in')
    print("You said",query)
  except Exception as e:
    print(e)
    speak("Say that again please")
    query="Nothing"
  return query
  

if __name__ == "__main__":
  # wishme()

  while True:
    query=takecommand().lower()
    if "wake up siri" in query:
      wishme()
      speak("Ongalukaga naa enna pannanum")

      while True:
        query=takecommand().lower()

        if "wikipedia" in query:
          speak("searching in wikipedia")
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)

        elif "open youtube" in query:
          webbrowser.open("youtube.com")
          
        elif "open google" in query:
          webbrowser.open("google.com")

        elif "open stackoverflow" in query:
          webbrowser.open("stackoverflow.com")

        elif "play music" in query:
          musicdir="D:\\Krishna\\shivan songs"
          songs=os.listdir(musicdir)
          print(songs)
          os.startfile(os.path.join(musicdir,songs[0]))

        elif "play song" in query:
          musicdir="D:\\Krishna\\shivan songs"
          songs=os.listdir(musicdir)
          print(songs)
          os.startfile(os.path.join(musicdir,songs[0])) 

        elif "open vs code" in query:
          speak("Ok sir")
          codepath="C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)

        elif "open chrome" in query:
          speak("Ok boss")
          codepath1="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
          os.startfile(codepath1)

        elif "open zoom" in query:
          speak("Ok boss")
          codepath1="C:\\Users\\ELCOT\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
          os.startfile(codepath1)

        elif "time" in query:
          time=datetime.datetime.now().strftime("%H:%M")
          speak(time)
          print(time)
        
        elif "shutdown pc" in query:
          speak("okay boss")
          os.system("shutdown /s /t 06")
          speak("I am going to shutdown the computer boss")
          speak("bye sir, have a good day.")
          sys.exit()

        elif "thanks" in query:
          speak("ok boss")
          exit()

        elif "thank you" in query:
          speak("ok boss")
          exit()

        elif "tell your lover name" in query:
          speak("my lover name kishore ")

        elif "tell your boyfriend name" in query:
          speak("my boyfriend name is kishore ")

        elif "boyfriend birthday date" in query:
          speak("18 april 2002")

        elif "siri tell your phone number" in query:
          speak("7010028358...this is my boyfriend number..if want my number go and ask my boyfriend")

        elif "tell your phone number siri" in query:
          speak("7010028358...this is my boyfriend number..if want my number go and ask my boyfriend")
        
        elif "love you siri" in query:
          speak("i like you")

        elif "introduce yourself" in query:
          speak("hey there! i'm siri. build by kishore and i like watching, and my favorite cartoon character is doraemon")
         
        elif "How are you" in query:
          speak("i am fine. what about you ?")

        elif "i am fine" in query:
          speak("ok nice..")




      






