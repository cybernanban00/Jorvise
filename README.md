Jorvise – Python Voice Assistant
Jorvise is a lightweight desktop voice assistant built with Python. It greets the user based on the time of day, listens for voice commands through the microphone, and responds with natural speech. Jorvise can search Wikipedia and read short summaries aloud, making it a simple but effective demonstration of speech recognition and text-to-speech technology.

Key Features

Speech Input & Output: Uses the SpeechRecognition library for capturing voice commands and Google Text-to-Speech (gTTS) for spoken responses.

Context-Aware Greeting: Automatically says “Good Morning,” “Good Afternoon,” or “Good Evening” depending on the current time.

Wikipedia Search: Fetches concise, two-sentence summaries from Wikipedia and reads them out loud.

Robust Error Handling: Handles network issues, ambiguous queries, and recognition errors gracefully.

Tech Stack

Python 3

gTTS for text-to-speech

SpeechRecognition with PyAudio for voice input

playsound for audio playback

Wikipedia API

This project demonstrates real-time voice interaction in Python and can be extended with additional commands, APIs, or smart-home integrations.
