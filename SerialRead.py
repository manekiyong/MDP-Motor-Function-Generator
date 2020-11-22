import pandas as pd
import serial
import sys
import glob


#s = serial.Serial('COM6')
def setupSerial(comPort):
    try:
        s=serial.Serial(comPort)
        print(comPort, "Connected Successfully!")
        return s
    except:
        print('Connection Failed!')
        return -1

def read_serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def readArduino(comPort):
    column_names = ["LeftF", "RightF", "SpeedF", "Empty", "LeftR", "RightR", "SpeedR"]
    df = pd.DataFrame(columns = column_names)
    FRes = ""
    RRes = ""
    s = setupSerial(comPort)
    if s == -1:
        print("No serial connection established!")
        return False
    while(True):
        FRes = s.readline().decode("utf-8")
        if("Done" in FRes):
            break
        txtarr = FRes.split('\t')
        FresInput = float(txtarr[0])
        FleftOutput = float(txtarr[1])
        FrightOutput = float(txtarr[2])
        print(FRes)
        RRes = s.readline().decode("utf-8")
        txtarr = RRes.split('\t')
        RresInput = float(txtarr[0])
        RleftOutput = float(txtarr[1])
        RrightOutput = float(txtarr[2])
        print(RRes)
        new_row = {'LeftF':FleftOutput, 'RightF':FrightOutput, 'SpeedF':FresInput, 'LeftR':RleftOutput, 'RightR':RrightOutput, 'SpeedR':-RresInput}
        df = df.append(new_row, ignore_index=True)

    print(df)
    df.to_excel("output.xlsx", index = False)  
    return True