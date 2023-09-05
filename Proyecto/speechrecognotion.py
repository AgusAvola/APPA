import speech_recognition as sr  
r = sr.Recognizer()
r.dynamic_energy_threshold = False
mic = sr.Microphone(#device_index=
)
try:
    with mic as source:
        print("Speak:")
        audio = r.listen(source, timeout= 2.0)  
        print("You said " + r.recognize_google(audio, language="es-ES"))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.WaitTimeoutError:
    print("Im calling an ambulance")
