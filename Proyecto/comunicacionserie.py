import time
import serial
import twiliomessage
def comunicacionserial(a:str):
    print('Running')
    with serial.Serial("COM11",9600, timeout=1) as arduino:
        time.sleep(0.1)
        if arduino.isOpen():
            print("{} connected!".format(arduino))
            cmd=a
            try:
                while True:
                    final=a
                    arduino.write(cmd.encode())
                    answer=arduino.readline()
                    print(answer)
                    if answer==b"Termino\r\n":
                        cmd="avanzar"
                    if answer==b"retroceder\r\n":
                        cmd="salir"
                    if answer== b"esperar a que tome la pastilla\r\n":
                        cmd="entrar"
                    if answer==b"cajon adentro\r\n":
                        cmd="volver"
                    if answer==b"girar\r\n":
                        cmd="pastilla"
                    if answer==b"Sin objeto\r\n":
                        twiliomessage.sms(final)
                    if answer==b"Sin objeto\r\n" or answer==b"Objeto detectado\r\n": 
                        if final=="1":
                            cmd="volverUnPaso"
                        if final=="2":
                            cmd="volverDosPasos"
                        if final=="3":
                            cmd="volverTresPasos"
                        if final=="4":
                            cmd="volverCuatroPasos"
                        if final=="4":
                            cmd="volverCincoPasos"
                        if final=="6":
                            cmd="volverSeisPasos"
                        if final=="7":
                            cmd="volverSietePasos"
                        if final=="8":
                            cmd="volverOchoPasos"
                        if final=="9":
                            cmd="volverNuevePasos"
                        if final=="10":
                            break
                    if answer==b"Acabar\r\n":
                        break
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
