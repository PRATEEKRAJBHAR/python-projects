from plyer import notification
import time  #its use to time delay
if __name__=="__main__":  # its use to seperate our code
    while True: #it use to infinite loop time
        notification.notify(title="***Take Rest***",message="rest is very important for everyone because rest feel relax",timeout=5)
        time.sleep(20)
