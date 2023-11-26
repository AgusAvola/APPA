import llamar.py
def comunicacion():
    def hablar(a:str):
        text = a
        engine.setProperty("rate", 150)
        engine.say(text)
        engine.runAndWait()

    import speech_recognition as sr  
    import pyttsx3
    from threading import Timer
    delay = 1

    contador:int=0
    engine = pyttsx3.init() 
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    for i in range(2):  
        hablar("¿Puede ser que te hayas caído?")

        mic = sr.Microphone(#device_index=
        )
        try:
            with mic as source:
                print("Speak:")
                audio = r.listen(source, timeout= 5.0)  
                print("You said " + r.recognize_google(audio, language="es-ES"))

                if(str(r.recognize_google(audio, language="es-ES"))=="si"):
                    hablar("Voy a llamar a una ambulancia")
                    import llamar.py
                    break
                if(str(r.recognize_google(audio, language="es-ES"))=="no"):
                    hablar("Perdoneme entonces")
                    t = Timer(delay, comunicacion, [delay])
                    t.start() 
                    break
        except sr.UnknownValueError:
            hablar("no entendi")
            if(i>0):
                hablar("Voy a llamar a una ambulancia")
                llamar()
                break 
        except sr.WaitTimeoutError:
            print("se acabo el tiempo")
            hablar("Voy a llamar a una ambulancia")
            import llamar
            break
comunicacion()