import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init() 
# convert this text to speech
text = "¿Te caíste?"
engine.setProperty("rate", 150)
engine.say(text)
# play the speech
engine.runAndWait()