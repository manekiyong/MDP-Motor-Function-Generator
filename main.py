import numpy as np
import pandas as pd

import LinReg
import SerialRead



def optOne():   
    availPorts = SerialRead.read_serial_ports()
    comPortSelect = -1
    if(len(availPorts)==0):
        print("No COM Port available!")
        return
    while(comPortSelect<=0 or comPortSelect>count):
        count = 1
        print("\nSelect COM Port:")
        for i in availPorts:
            print(str(count)+": "+ str(i))
            count+=1
        print(str(count)+": Return")
        comPortSelect=int(input())
    if(comPortSelect==count):
        return
    else:
        selectedPort = availPorts[comPortSelect-1]

    if(SerialRead.readArduino(selectedPort)==False):
        return
    LinReg.predictor("output.xlsx")

def optTwo():
    fileName = input("Input filename (with file extension, i.e. output.xlsx): ")
    LinReg.predictor(fileName)

if __name__ == "__main__":

    while(True):
        userInput = -1
        while(userInput<=0 or userInput >=4):
            print("\nSelect Option:")
            print("1. Read from Arduino+Produce Function")
            print("2. Produce Function from Spreadsheet")
            print("3. Terminate")
            try:
                userInput = int(input())
            except:
                userInput = -1
        if userInput==1:
            optOne()
        elif userInput==2:
            optTwo()
        else:
            exit()