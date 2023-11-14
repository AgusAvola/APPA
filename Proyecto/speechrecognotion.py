import speech_recognition as sr  
r = sr.Recognizer()
r.dynamic_energy_threshold = False
mic = sr.Microphone(#device_index=
)
try:
    with mic as source:
        print("Speak:")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout= 10.0)  
        print("You said " + r.recognize_google(audio, language="es-ES"))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.WaitTimeoutError:
    print("Im calling an ambulance")
