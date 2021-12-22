import time
import Adafruit_DHT as dht
import RPi.GPIO as GPIO

def checkCurrentHumAndTemp(gpioNum=26):

    f = open("/home/pi/Desktop/temphum.txt", 'r')
    lines = f.readlines()
    humidity,temp = dht.read_retry(dht.DHT22, gpioNum)
    #humidity = 10
    #temp = 25.8
    if humidity != None:
        humidity=round(humidity, 1)
    else:
        humidity = float(lines[1])
    if temp != None:
        temp=round(temp, 1)
    else:
        temp = float(lines[0].strip())
    
    return humidity, temp

def connectRelay(gpioNum, act=True):
    '''
    #every connection of relay is based on NO and COM
    #if act==True it works : connect NO and COM
    #if act==False it doesn't works : connect NC and Com
    '''
    GPIO.setup(gpioNum, GPIO.OUT)
    if act==True:
        GPIO.output(gpioNum, True)
    if act==False:
        GPIO.output(gpioNum, False)



#set gpioNum with BCM -1 = non set
airPump_relay_gpioNum = 27
led_relay_gpioNum = 24
cooler_relay_gpioNum = 17
led_r_relay_gpioNum = 23

#GPIO setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(airPump_relay_gpioNum, GPIO.OUT)
GPIO.setup(led_relay_gpioNum, GPIO.OUT)
GPIO.setup(cooler_relay_gpioNum, GPIO.OUT)
GPIO.setup(led_r_relay_gpioNum, GPIO.OUT)

connectRelay(airPump_relay_gpioNum)
connectRelay(led_relay_gpioNum)
connectRelay(cooler_relay_gpioNum)
connectRelay(led_r_relay_gpioNum)



def checkTime(startTime, endTime):

    currentTime = time.localtime(time.time())
    currentTime = int(currentTime.tm_hour)*100 + int(currentTime.tm_min)
    if startTime == endTime:
        return True
    if startTime <= currentTime and currentTime < endTime:
        return True
    else:
        return False


def readGivenInfo():

    f=open("/home/pi/Desktop/info.txt", "r")
    lines=f.readlines() 
    wanted_hum = int(lines[0])
    wanted_temp = int(lines[1])
    wanted_led_start_time = int(lines[2]) #8:30
    wanted_led_end_time = int(lines[3]) #18:40
    wanted_pump_start_time = int(lines[4]) #8:30
    wanted_pump_end_time = int(lines[5]) #18:40
    wanted_led_on_off = int(lines[6])
    wanted_led2_on_off = int(lines[7])
    f.close()
    return wanted_hum, wanted_temp, wanted_led_start_time, wanted_led_end_time, \
           wanted_pump_start_time,  wanted_pump_end_time, wanted_led_on_off, wanted_led2_on_off

def sendTempHum(c_temp, c_hum):
    f=open("/home/pi/Desktop/temphum.txt",'w')
    f.write(str(c_temp)+"\n")
    f.write(str(c_hum))
    f.close()

while True:
    # get info
    #print("working")
    c_hum, c_temp = checkCurrentHumAndTemp()
    #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(c_temp, c_hum))
    
    sendTempHum(c_temp, c_hum)
    wanted_hum, wanted_temp,wanted_led_start_time, wanted_led_end_time, wanted_pump_start_time, \
    wanted_pump_end_time, wanted_led_on_off, wanted_led2_on_off = readGivenInfo()

    # chcek temp and run cooler
    if c_temp > wanted_temp:
        connectRelay(cooler_relay_gpioNum)
    else:
        connectRelay(cooler_relay_gpioNum, False)

    # check time and run LED
    if checkTime(wanted_led_start_time, wanted_led_end_time):
        if wanted_led_on_off == 1:
            connectRelay(led_relay_gpioNum)
        else:
            connectRelay(led_relay_gpioNum, False)

        if wanted_led2_on_off == 1:
            connectRelay(led_r_relay_gpioNum)
        else:
            connectRelay(led_r_relay_gpioNum, False)
    else:
        connectRelay(led_relay_gpioNum, False)
        connectRelay(led_r_relay_gpioNum, False)

    # check time and run Pump
    if checkTime(wanted_pump_start_time, wanted_pump_end_time):
        connectRelay(airPump_relay_gpioNum)
    else:
        connectRelay(airPump_relay_gpioNum, False)
    time.sleep(1)

