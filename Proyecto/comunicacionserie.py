import time
import serial
def comunicacionserial(a:str):
    print('Running')
    with serial.Serial("COM3",9600, timeout=1) as aduino:
        time.sleep(0.1)
        if arduino.isOpen():
            print("{} connected!".format(arduino))
            try:
                while True:
                    cmd=a
                    final=a
                    arduino.write(cmd.encode())
                    answer=arduino.readLine()
                    print(answer)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")