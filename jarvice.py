import datetime
import os
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import wikipedia

# Speak using gTTS
def speak(audio):
    try:
        tts = gTTS(text=audio, lang='en')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        # Add delay to avoid file access error
        time.sleep(0.5)
        os.remove("voice.mp3")
    except Exception as e:
        print("Speak Error:", e)

# Wish the user
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning...")
    elif 12 <= hour < 18:
        speak("Good Afternoon...")
    else:
        speak("Good Evening...")
    speak("How can I help you?")

# Recognize speech input
def voice_recognition():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        speak("Sorry, I can't reach the speech service.")
    except Exception as e:
        print("Voice Recognition Error:", e)
        speak("Something went wrong while listening.")
    return None

# Main execution
if __name__ == "__main__":
    speak("Hi sir, welcome...")
    wish()
    while True:
        query = voice_recognition()

        if query:
            if "wikipedia" in query:
                speak("Searching Wikipedia...")
                try:
                    query = query.replace("wikipedia", "").strip()
                    result = wikipedia.summary(query, sentences=2)
                    speak("Here is what I found.")
                    speak(result)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("That is too ambiguous. Can you be more specific?")
                except wikipedia.exceptions.PageError:
                    speak("I couldn't find anything on Wikipedia.")
                except Exception as e:
                    print("Wikipedia error:", e)
                    speak("An error occurred while searching Wikipedia.")

            elif "exit" in query or "stop" in query or "bye" in query:
                speak("Goodbye, sir!")
                break
