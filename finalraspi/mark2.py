# -*- coding: utf-8 -*-
import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.font
import subprocess
#set GPIO
#set gpioNum with BCM -1 = non set
airPump_relay_gpioNum = 27
led_relay_gpioNum = 23
cooler_relay_gpioNum = 17
led_r_relay_gpioNum = 24


runF2 = subprocess.Popen(['nohup', 'python', '/home/pi/Desktop/final2.py'], stdout=open('/dev/null','w'), stderr = open('logfile.log', 'a'))

#start tk
window = tkinter.Tk()

minuteList = ['00', '01', '02', '03', '04', '05',
              '06', '07', '08', '09', '10', '11',
              '12', '13', '14', '15', '16', '17',
              '18', '19', '20', '21', '22', '23',
              '24', '25', '26', '27', '28', '29',
              '30', '31', '32', '33', '34', '35',
              '36', '37', '38', '39', '40', '41',
              '42', '43', '44', '45', '46', '47',
              '48', '49', '50', '51', '52', '53',
              '54', '55', '56', '57', '58', '59']

hourList = ['00', '01', '02', '03', '04', '05',
            '06', '07', '08', '09', '10', '11',
            '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23']

# title
window.title("온습도 조회")
window.geometry('800x480')
window.resizable(True, True)
# 폰트 설정
fontStyle = tkinter.font.Font(size=24)
buttonStyle = ttk.Style()
buttonStyle.configure('my.TButton', font=(24))

# %% 현 상황 조회창
showTemp = ttk.Label(window, text="현재 온도 : ", font=fontStyle)
showTemp.grid(column=0, row=0)

showHum = ttk.Label(window, text="현재 습도 : ", font=fontStyle)
showHum.grid(column=0, row=1)


def settingActive():
    '''설정 누르면 콤보박스 활성화 필요'''
    # normal disable
    setHumComboBox.configure(state='readonly')
    setTempComboBox.configure(state='readonly')
    setPumpStartTimeHourCombobox.configure(state='readonly')
    setPumpStartTimeMinCombobox.configure(state='readonly')
    setPumpEndTimeHourCombobox.configure(state='readonly')
    setPumpEndTimeMinCombobox.configure(state='readonly')
    setLEDStartTimeHourCombobox.configure(state='readonly')
    setLEDStartTimeMinCombobox.configure(state='readonly')
    setLEDEndTimeHourCombobox.configure(state='readonly')
    setLEDEndTimeMinCombobox.configure(state='readonly')
    setRedLED.configure(state='normal')
    setWhiteLED.configure(state='normal')


settingButton = ttk.Button(window, text="설정", style='my.TButton', command=settingActive)
settingButton.grid(column=5, row=2)

# %%온도 입력
setTempLabel = ttk.Label(window, text="설정 온도 ( *C)", font=fontStyle)
setTempLabel.grid(column=0, row=2)

setTempComboBox = ttk.Combobox(window, width=5)
setTempComboBox['values'] = [x for x in range(10, 31)]
setTempComboBox.grid(column=1, row=2)
setTempComboBox.current(0)

# %%습도 입력
setHumLabel = ttk.Label(window, text="설정 습도 ( % )",font=fontStyle)
setHumLabel.grid(column=0, row=3)

setHumComboBox = ttk.Combobox(window, width=5)
setHumComboBox['values'] = [x for x in range(0, 101)]
setHumComboBox.grid(column=1, row=3)
setHumComboBox.current(50)

# %% 펌프 시간 입력
setPumpTimeLabel = ttk.Label(window, text="펌프 작동시간",font=fontStyle)
setPumpTimeLabel.grid(column=0, row=4)

setPumpStartTimeHourCombobox = ttk.Combobox(window, width=5)
setPumpStartTimeHourCombobox['values'] = hourList
setPumpStartTimeHourCombobox.grid(column=1, row=4)
setPumpStartTimeHourCombobox.current(5)

setPumpStartTimeMinCombobox = ttk.Combobox(window, width=5)
setPumpStartTimeMinCombobox['values'] = minuteList
setPumpStartTimeMinCombobox.grid(column=2, row=4)
setPumpStartTimeMinCombobox.current(29)

setPumpSplitLabel = ttk.Label(window, text="~",font=fontStyle)
setPumpSplitLabel.grid(column=3, row=4)

setPumpEndTimeHourCombobox = ttk.Combobox(window, width=5)
setPumpEndTimeHourCombobox['values'] = hourList
setPumpEndTimeHourCombobox.grid(column=4, row=4)
setPumpEndTimeHourCombobox.current(18)

setPumpEndTimeMinCombobox = ttk.Combobox(window, width=5)
setPumpEndTimeMinCombobox['values'] = minuteList
setPumpEndTimeMinCombobox.grid(column=5, row=4)
setPumpEndTimeMinCombobox.current(29)

# %% 조명 시간 입력

setLEDTimeLabel = ttk.Label(window, text="조명 작동시간",font=fontStyle)
setLEDTimeLabel.grid(column=0, row=5)

setLEDStartTimeHourCombobox = ttk.Combobox(window, width=5)
setLEDStartTimeHourCombobox['values'] = hourList
setLEDStartTimeHourCombobox.grid(column=1, row=5)
setLEDStartTimeHourCombobox.current(5)

setLEDStartTimeMinCombobox = ttk.Combobox(window, width=5)
setLEDStartTimeMinCombobox['values'] = minuteList
setLEDStartTimeMinCombobox.grid(column=2, row=5)
setLEDStartTimeMinCombobox.current(29)

setLEDSplitLabel = ttk.Label(window, text="~",font=fontStyle)
setLEDSplitLabel.grid(column=3, row=5)

setLEDEndTimeHourCombobox = ttk.Combobox(window, width=5)
setLEDEndTimeHourCombobox['values'] = hourList
setLEDEndTimeHourCombobox.grid(column=4, row=5)
setLEDEndTimeHourCombobox.current(18)

setLEDEndTimeMinCombobox = ttk.Combobox(window, width=5)
setLEDEndTimeMinCombobox['values'] = minuteList
setLEDEndTimeMinCombobox.grid(column=5, row=5)
setLEDEndTimeMinCombobox.current(30)

# Define empty variables
var1 = IntVar()
var2 = IntVar()

# %% 조명 선택      ////
setWhiteLED = Checkbutton(window, text='1층', variable=var1, onvalue=1, offvalue=0, font=fontStyle)
setWhiteLED.grid(column=1 , row=6)

setRedLED = Checkbutton(window, text='2층', variable=var2, onvalue=1, offvalue=0, font=fontStyle)
setRedLED.grid(column=2, row=6)

# 초기 상태: normal disable
setHumComboBox.configure(state='disable',font=fontStyle)
setTempComboBox.configure(state='disable',font=fontStyle)
setPumpStartTimeHourCombobox.configure(state='disable',font=fontStyle)
setPumpStartTimeMinCombobox.configure(state='disable',font=fontStyle)
setPumpEndTimeHourCombobox.configure(state='disable',font=fontStyle)
setPumpEndTimeMinCombobox.configure(state='disable',font=fontStyle)
setLEDStartTimeHourCombobox.configure(state='disable',font=fontStyle)
setLEDStartTimeMinCombobox.configure(state='disable',font=fontStyle)
setLEDEndTimeHourCombobox.configure(state='disable',font=fontStyle)
setLEDEndTimeMinCombobox.configure(state='disable',font=fontStyle)
setRedLED.configure(state='disable',font=fontStyle)
setWhiteLED.configure(state='disable',font=fontStyle)


# %% 사용자 설정 반영 버튼
def apply():
    setHumComboBox.configure(state='disable')
    setTempComboBox.configure(state='disable')
    setPumpStartTimeHourCombobox.configure(state='disable')
    setPumpStartTimeMinCombobox.configure(state='disable')
    setPumpEndTimeHourCombobox.configure(state='disable')
    setPumpEndTimeMinCombobox.configure(state='disable')
    setLEDStartTimeHourCombobox.configure(state='disable')
    setLEDStartTimeMinCombobox.configure(state='disable')
    setLEDEndTimeHourCombobox.configure(state='disable')
    setLEDEndTimeMinCombobox.configure(state='disable')
    setRedLED.configure(state='disable')
    setWhiteLED.configure(state='disable')

    # 여기서부터 다른 파일로 전달 혹은 서로 전송 필요
    f = open("info.txt", "w")
    f.write(setHumComboBox.get() + "\n")
    f.write(setTempComboBox.get() + "\n")
    f.write(setLEDStartTimeHourCombobox.get() + setLEDStartTimeMinCombobox.get() + "\n")
    f.write(setLEDEndTimeHourCombobox.get() + setLEDEndTimeMinCombobox.get() + "\n")
    f.write(setPumpStartTimeHourCombobox.get() + setPumpStartTimeMinCombobox.get() + "\n")
    f.write(setPumpEndTimeHourCombobox.get() + setPumpEndTimeMinCombobox.get() + "\n")
    f.write('%s\n' % var1.get())
    f.write('%s\n' % var2.get())

    f.close()


applyButton = ttk.Button(window, text='적용', style='my.TButton', command=apply)
applyButton.grid(column=5, row=6)

def end():
    exit(0)

endButton = ttk.Button(window, text='전체 종료', style='my.TButton', command=end)
endButton.grid(column=5, row=0)

def RPcontrol():
  
    # %% 현재 온습도 조회 , strip사용

    f = open("temphum.txt", 'r')
    lines = f.readlines()
    showTemp.config(text="현재 온도: " + lines[0].strip() +"*C")
    showHum.config(text="현재 습도: " + lines[1] +'%')
    
    f.close()
    window.after(100, RPcontrol)

# %% 최종
RPcontrol()

window.mainloop()




















