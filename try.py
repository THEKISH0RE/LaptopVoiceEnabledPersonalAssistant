import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import sys
import random
import numpy as np
import cv2
from pyautogui import screenshot
from time import sleep
from utils import (
  music_path,
  capture_screenshot
  )

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
chrome_path ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    # Set the maximum recording time to 5 seconds
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=5, phrase_time_limit=5)
  try:
    print("Processing...")
    query = r.recognize_google(audio, language='en-in')
    print("You said:", query)
  except Exception as e:
    print(e)
    # speak("Say that again please")
    query = "Nothing"
  return query


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your laptop voice-enabled personal assistant. How may I assist you?")





if __name__ == "__main__":

  speak("You want to activate voice command.")

  def voice():
    engine.startLoop()

  while True:
          query = takecommand().lower()
          if "activate voice command" in query:
            speak("Activated ")
            wishme()

          while True:
            engine.runAndWait()
            query = takecommand().lower()
            chromeBrowser = webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
            Chrome = webbrowser.get('chrome')

            replay = ["Sure", "All right","Understood ", " Roger", "Fine ", "Very well ", "Got it ", "Alrighty", " Copy that"]


    #  ===== Starting Basic stuff ==========================================

            if "introduce yourself" in query:
              speak("Hi, I'm a laptop voice-enabled personal assistant. I'm a computer program designed to help people with their daily tasks on the laptop. I'm fast, efficient, and can understand English and Tanglish language. I'm friendly and eager to help, so don't hesitate to ask if you need any help!")

            elif "exit" in query:
              speak("Goodbye!")
              exit()

            elif "time" in query:
              time = datetime.datetime.now().strftime("%H:%M")
              speak(f"The time is {time}")
            
            elif any(keyword in query for keyword in ["thanks", "thank you"]):
                replies = ["I'm here for you, always.", "Feeling happy to help you.", "It's okay", "No problem", "The pleasure is mine", "That's my duty, my friend", "I'm happy for you", "No worries", "It's my pleasure", "Oh, come on! That's unnecessary"]
                speak(random.choice(replies))

               #  ===== Ending Basic stuff ==========================================

    #  ===== Starting Destop Control Code==============================
    # music
            elif "what type of music" in query:
              speak("Sure, playing some tunes to lift your spirits! Let's see what we have here. If you need a boost of motivation, I've got just the thing with some motivational songs. Or if you're in the mood for something a little more sentimental, we can go with some friendship songs. And of course, if you're feeling the love, we've got a great selection of love songs. But if you're feeling a bit down, I'm here for you with some sad songs. And if you just want to leave it up to chance, I'll pick a random song for you. Let's get started!")

            elif "play motivational song" in query:
              music_path('motivate song')
              replies = ["Great choice! Let's get motivated with some uplifting tunes.", "Let's kick things into high gear with some motivational songs.", "Your wish is my command - let's play some motivational tracks.", "Sure thing! Let's get pumped up with some inspiring music.", "Get ready to feel motivated! Here come some motivational songs."]
              speak(random.choice(replies))



            elif "play friendship song" in query:
              music_path('friend song')
              replies = ["Get ready to feel the power of true friendship with this song.", "Let this beautiful song remind you of the special people in your life.", "This song is a tribute to the joys of true friendship and camaraderie.", "As the music plays, let your heart be filled with gratitude for your friends.", "Turn up the volume and let this song celebrate the beauty of friendship."]
              speak(random.choice(replies))


            elif "play love song" in query:
              musicdir="D:\\songs\\love song"
              songs=os.listdir(musicdir)
              os.startfile(os.path.join(musicdir, random.choice(songs)))
              replies = ["Get ready to feel the power of love with this beautiful song.", "This song is a perfect tribute to the magic and mystery of love.", "Let the lyrics and melody of this song transport you to a world of pure romance.", "As you listen to this song, let your heart be filled with love and joy.", "Turn up the volume and let this song serenade you into a realm of love and affection."]
              speak(random.choice(replies))

            elif "play sad song" in query:
              musicdir="D:\\songs\\sad song"
              songs=os.listdir(musicdir)
              os.startfile(os.path.join(musicdir, random.choice(songs)))
              replies =["Get ready to feel the emotion and depth of this sad song.", "Let the haunting melody and lyrics of this song stir your soul.", "This song captures the pain and sorrow of heartbreak and loss.", "As you listen to this song, let yourself feel and process your emotions.", "Turn down the lights, and let this sad song help you find solace in your sadness.", "Your wish is my command - let's play some sad tracks."]
              speak(random.choice(replies))

            elif any(keyword in query for keyword in ["play random song", "play any song"]):
              musicdir="D:\\songs"
              songs=os.listdir(musicdir)
              # print(songs)
              os.startfile(os.path.join(musicdir, random.choice(songs))) 
              replies = ["Get ready for a surprise as we play a random song for you.", "Let this random selection take you on a journey of musical discovery.", "This song could be anything - a classic, a hit, or an underground gem.", "As the music plays, let yourself be open to new sounds and genres.", "Get ready to be surprised, inspired and moved by this random song."]
              speak(random.choice(replies))


    # movies

            elif "play asuran movie" in query: 
              speak("sure")
              movie_dir = "D:\\movies"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[15]))
              speak("Get ready to witness Dhanush's powerful performance in Asuran.")

            elif "play love today movie" in query: 
              movie_dir = "D:\\movies"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[100]))
              speak("Love Today's heartwarming story will leave you with a smile on your face.")

            elif any(keyword in query for keyword in ["play random movie", "play any movie"]):
              movie_dir = "D:\\movies"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, random.choice(movies)))
              replies = ["Sit back, relax and let our random movie selection take you on a cinematic journey.", "With these random movies, there's something for everyone's taste."]
              speak(random.choice(replies))

            elif "open movies folder" in query:
              codepath14 = "D:\\movies"
              os.startfile(codepath14)
              speak("okay, this is your movies collection")
    # .................................................................
    # harry potter
            elif "harry potter collection" in query:
              speak(random.choice(replay))             
              codepath7="D:\\movies\\Harry Potter Collection"
              os.startfile(codepath7)

            elif "play harry potter part 1" in query: 
              speak(random.choice(replay))             
              speak("playing part 1")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[0]))

            elif "play harry potter part 2" in query:
              speak(random.choice(replay))             
              speak("playing part 2")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join
              (movie_dir, movies[1]))

            elif "play harry potter part 3" in query: 
              speak(random.choice(replay))             
              speak("playing part 3")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[2]))

            elif "play harry potter part 4" in query: 
              speak(random.choice(replay))             
              speak("playing part 4")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[3]))

            elif "play harry potter part 5" in query:
              speak(random.choice(replay))              
              speak("playing part 5")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[4]))

            elif "play harry potter part 6" in query: 
              speak(random.choice(replay))             
              speak("playing part 6")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[5]))

            elif "play harry potter part 7" in query: 
              speak(random.choice(replay))             
              speak("playing part 7")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[6]))

            elif "play harry potter part 8" in query: 
              speak(random.choice(replay))             
              speak("playing part 8")
              movie_dir = "D:\\movies\\Harry Potter Collection"          
              movies=os.listdir(movie_dir)
              os.startfile(os.path.join(movie_dir, movies[7]))

    # ....................................................................

            elif "open vs code" in query:
              speak(random.choice(replay)) 
              speak("Open Microsoft's Visual Studio Code.")            
              codepath="C:\\Users\\ELCOT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codepath)

            elif "open chrome" in query:
              speak(random.choice(replay))  
              speak("Launching Chrome")
              codepath1="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
              os.startfile(codepath1)

            elif "open zoom" in query:
              speak(random.choice(replay))      
              speak("Open the Zoom application.")       
              codepath2="C:\\Users\\ELCOT\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
              os.startfile(codepath2)

            elif "open notepad" in query:
              speak(random.choice(replay))       
              speak("Loading Notepad")      
              codepath3 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
              os.startfile(codepath3)


            elif "open ms word" in query:
              speak(random.choice(replay))             
              codepath01 = "D:\\AI_word&excel\\msWord.docx"
              os.startfile(codepath01)

            elif "open excel" in query:
              speak(random.choice(replay))             
              codepath02 = "D:\\AI_word&excel\\Excel.xlsx"
              os.startfile(codepath02)

            elif "open download folder" in query:
              speak(random.choice(replay))             
              codepath04 = "C:\\Users\\ELCOT\\Downloads"
              os.startfile(codepath04)

            elif "open command prompt" in query:
              speak(random.choice(replay))             
              codepath05 = "C:\\Users\\ELCOT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
              os.startfile(codepath05)

            elif "open cmd" in query:
              speak(random.choice(replay))             
              codepath05 = "C:\\Users\\ELCOT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
              os.startfile(codepath05)

            elif "open paint" in query:
              speak(random.choice(replay))             
              codepath4 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk"
              os.startfile(codepath4)

            elif "open file explorer" in query:
              speak(random.choice(replay))             
              codepath5 = "C:\\Windows\\explorer.exe"
              os.startfile(codepath5)

            elif "open picture folder" in query:
              speak(random.choice(replay))             
              codepath6 = "C:\\Users\\ELCOT\\Pictures"
              os.startfile(codepath6)

    # .....................................................................
    # screenShot 10 only

            elif "take screenshot" in query:
              capture_screenshot()   
              speak("okay screenshot is taken")

            elif "show my screenshot" in query:
              speak(random.choice(replay))             
              codepath11 = "C:\\Users\\ELCOT\\Desktop\\CLG_Project\\screenshot"
              os.startfile(codepath11)

    #  ===== Ending Destop Control  Code==================================

    #  ===== Starting Web Control Code ===================================

            elif "wikipedia" in query:
              speak("searching in wikipedia")
              query=query.replace("wikipedia","")
              results=wikipedia.summary(query,sentences=2)
              speak("According to wikipedia")
              print(results)
              speak(results)

            elif "ingredient" in query:
              speak("searching ")
              query1=query.replace("wikipedia","")
              results=wikipedia.summary(query1,sentences=3)
              print(results)
              speak(results)
            
            elif "open youtube" in query:
              speak(random.choice(replay))             
              chromeBrowser
              Chrome.open("youtube.com")
              
            elif "open google" in query:
              speak(random.choice(replay))             
              chromeBrowser
              Chrome.open("google.com")

            elif "open stackoverflow" in query:
              speak(random.choice(replay))             
              chromeBrowser
              Chrome.open("stackoverflow.com")


    #  ===== Ending Web Control Code ===================================

    #  ===== Final Code ================================================

            elif "shutdown pc" in query:
              speak(random.choice(replay))             
              os.system("shutdown /s /t 06")
              speak("I am going to shutdown the laptop")
              speak("bye sir, have a good day.")
              sys.exit()

            
            elif "deactivate voice command" in query:
              speak(random.choice(replay))             
              speak("Deactivated")
              exit()